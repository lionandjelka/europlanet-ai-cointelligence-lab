import torch
import torch.nn as nn

class ConvBNReLU(nn.Module):
    def __init__(self,cin,cout,k=11,dilation=3):
        super().__init__(); pad=dilation*(k-1)//2
        self.net=nn.Sequential(nn.Conv1d(cin,cout,k,padding=pad,dilation=dilation),nn.BatchNorm1d(cout),nn.ReLU())
    def forward(self,x): return self.net(x)

class PanopticonUNet3Plus1D(nn.Module):
    """Paper-faithful classroom reimplementation of Vivien et al. (2025).
    Architecture/task faithful; training recipe and weights are classroom-specific.
    This is NOT official author code or official PANOPTICON weights.
    """
    def __init__(self,base=8,k=11,dilation=3,cat_ch=8):
        super().__init__(); ch=[base,base*2,base*4,base*8,base*16]
        self.enc=nn.ModuleList(); cin=1
        for c in ch: self.enc.append(ConvBNReLU(cin,c,k,dilation)); cin=c
        self.pool=nn.MaxPool1d(2); self.ch=ch; self.cat_ch=cat_ch
        self.proj=nn.ModuleDict(); self.dec=nn.ModuleDict()
        for level in [3,2,1,0]:
            for src in range(5): self.proj[f'e{src}to{level}']=nn.Conv1d(ch[src],cat_ch,1)
            self.dec[str(level)]=ConvBNReLU(cat_ch*5,cat_ch,k=3,dilation=1)
        self.out=nn.Conv1d(cat_ch,1,1)
    def _resize(self,x,n): return nn.functional.interpolate(x,size=n,mode='linear',align_corners=False)
    def forward(self,x):
        es=[]; z=x
        for i,b in enumerate(self.enc):
            z=b(z); es.append(z)
            if i<4: z=self.pool(z)
        ds={}
        for level in [3,2,1,0]:
            n=es[level].shape[-1]; parts=[]
            for src,e in enumerate(es):
                q=e if e.shape[-1]==n else self._resize(e,n)
                parts.append(self.proj[f'e{src}to{level}'](q))
            ds[level]=self.dec[str(level)](torch.cat(parts,1))
        return self.out(ds[0])
