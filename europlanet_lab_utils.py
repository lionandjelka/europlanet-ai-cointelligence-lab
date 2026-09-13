from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt, torch
from models.panopticon_unet3plus_1d import PanopticonUNet3Plus1D
CLASS_LABELS={0:'Quiet star, no planet',1:'Active star, no planet',2:'Planet + mild activity',3:'Planet + strong activity'}

def load_tables(root='.'):
    root=Path(root); meta=pd.read_csv(root/'data/student_metadata.csv'); bls=pd.read_csv(root/'data/student_bls_results.csv'); pan=pd.read_csv(root/'data/panopticon_scores.csv')
    quiet_thr=float(np.percentile(bls.loc[bls.label==0,'bls_power'],95))
    df=bls.merge(meta,on='file_id',suffixes=('','_meta')).merge(pan,on='file_id')
    df['bls_power_ratio']=df.bls_power/quiet_thr; df['bls_flag_recalc']=df.bls_power>quiet_thr
    return meta,bls,pan,df,quiet_thr

def load_panopticon(root='.'):
    root=Path(root); ck=torch.load(root/'models/panopticon_classroom_weights.pt',map_location='cpu',weights_only=False)
    model=PanopticonUNet3Plus1D(ck['base'],ck['k'],ck['dilation'],ck['cat_ch']); model.load_state_dict(ck['state_dict']); model.eval(); return model,ck

def show_window(t,x,mask=None,prob=None,title=''):
    fig,ax=plt.subplots(2 if (mask is not None or prob is not None) else 1,1,figsize=(10,4.8),sharex=True)
    if not isinstance(ax,np.ndarray): ax=np.array([ax])
    ax[0].plot(t,x,lw=1); ax[0].set_ylabel('robust-normalized flux'); ax[0].set_title(title)
    if len(ax)>1:
        if mask is not None: ax[1].fill_between(t,0,mask,alpha=.25,label='truth mask')
        if prob is not None: ax[1].plot(t,prob,lw=1.5,label='PANOPTICON probability')
        ax[1].set_ylim(-.03,1.03); ax[1].set_ylabel('event'); ax[1].legend(loc='upper right')
    ax[-1].set_xlabel('time [d]'); plt.tight_layout(); return fig

def find_exominer_predictions(root='.'):
    root=Path(root)/'exominer_official'/'outputs'
    names = [
        'predictions_spoc-tces_set.csv',      # current official pipeline docs
        'predictions_outputs.csv',            # older/alternate release
        'ranked_predictions_predictset.csv',  # older/alternate release
    ]
    hits = []
    for name in names:
        hits.extend(root.rglob(name))
    return sorted(set(hits))
