# Student setup and run instructions

## 1. Install Anaconda or Miniconda

Use an existing Anaconda installation or install a current Anaconda/Miniconda distribution for your operating system.

## 2. Open a terminal in the repository root

You should be in the directory containing `environment.yml`, `student/`, `data/`, `models/`, and `assets/`.

## 3. Create the dedicated environment

```bash
conda env create -f environment.yml
conda activate europlanet-lab
```

If the environment already exists and you want to update it:

```bash
conda env update -f environment.yml --prune
conda activate europlanet-lab
```

## 4. Register the Jupyter kernel

```bash
python -m ipykernel install --user \
  --name europlanet-lab \
  --display-name "EUROPLANET Lab"
```

## 5. Verify the Python interpreter

```bash
which python
python -c "import sys, torch; print(sys.executable); print(torch.__version__)"
```

The Python path should contain something similar to:

```text
.../anaconda3/envs/europlanet-lab/bin/python
```

## 6. Start JupyterLab

```bash
jupyter lab
```

Open:

```text
student/Europlanet_Research_Lab_90min.ipynb
```

Choose **Kernel → Change Kernel → EUROPLANET Lab**.

## 7. Run the notebook

For a clean start use **Kernel → Restart Kernel and Run All Cells**. The notebook automatically locates the project root from either the repository root or the `student/` directory.

## 8. ExoMiner++ note

The notebook can run without a live ExoMiner++ container. The official-pipeline segment is a showcase that uses cached official outputs when available. Instructors should pre-run the official NASA pipeline before class if they want live/cached ExoMiner++ predictions.

## Common problems

### `ModuleNotFoundError: torch`
The notebook is using the wrong Jupyter kernel. Select **EUROPLANET Lab** and verify `sys.executable`.

### `ModuleNotFoundError: europlanet_lab_utils`
Open the notebook from inside this repository and run the setup cell first. The notebook's root-detection code should locate `europlanet_lab_utils.py` automatically.

### Missing asset/data file
Do not move the notebook out of the repository. Keep `student/`, `data/`, `models/`, and `assets/` together.
