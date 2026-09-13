import shutil, subprocess, sys, pathlib
print('EUROPLANET ExoMiner++ preflight')
print('podman:', shutil.which('podman') or 'MISSING')
if shutil.which('podman'):
    try:
        r=subprocess.run(['podman','image','exists','ghcr.io/nasa/exominer'],capture_output=True)
        print('NASA ExoMiner image pre-pulled:', r.returncode==0)
    except Exception as e: print('Podman check failed:',e)
print('input table:', pathlib.Path(__file__).with_name('tics_table.csv').read_text())
print('Targets: TIC 261136679 = pi Mensae c (confirmed planet); TIC 167526485 S6 = published EB case.')
