# Publish this repository to GitHub

The public ZIP is already cleaned of instructor solutions and hidden truth.

## Command-line route

1. Create an empty GitHub repository, for example `europlanet-ai-cointelligence-lab`.
2. In Terminal, enter the unzipped public repository directory.
3. Run:

```bash
git init
git add .
git status
git commit -m "Initial release: EUROPLANET AI co-intelligence lab"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/europlanet-ai-cointelligence-lab.git
git push -u origin main
```

Before `git commit`, inspect `git status` and confirm that no instructor answer key or hidden truth is listed.

## Current file sizes

The prepared teaching files are small enough for ordinary Git. Git LFS is **not required** for the current public package.

If you later add the original large HDF5 simulation files or other large binaries, use Git LFS or an external data archive instead of ordinary Git.

## Recommended repository settings

- Add a short description: `Planetary-science AI co-intelligence lab: BLS, local event detection, ExoMiner++, Neural Processes, and follow-up decisions.`
- Enable Issues only if you want students to report setup problems there.
- Add the topics: `exoplanets`, `planetary-science`, `machine-learning`, `ai`, `neural-processes`, `education`, `europlanet`.
- Create a tagged release such as `v1.0.0` after the school material is frozen.
