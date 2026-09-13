#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:-$HERE/outputs}"
mkdir -p "$OUT"

if ! command -v podman >/dev/null 2>&1; then
  echo "ERROR: Podman is not installed. Install/start Podman before the school demo." >&2
  exit 2
fi

# Official NASA ExoMiner container and current documented pipeline interface.
# Documentation: https://github.com/nasa/ExoMiner/tree/main/docs
# Pre-pull before class:
#   podman pull ghcr.io/nasa/exominer

podman run --rm   --pids-limit=-1   --shm-size=16g   -e OPENBLAS_NUM_THREADS=1   -e OMP_NUM_THREADS=1   -e MKL_NUM_THREADS=1   -e VECLIB_MAXIMUM_THREADS=1   -e NUMEXPR_NUM_THREADS=1   -e TF_NUM_INTRAOP_THREADS=1   -e TF_NUM_INTEROP_THREADS=1   -v "$HERE/tics_table.csv:/tics_tbl.csv:Z"   -v "$OUT:/outputs:Z"   ghcr.io/nasa/exominer   --tic_ids_fp=/tics_tbl.csv   --output_dir=/outputs   --data_collection_mode=2min   --num_processes=1   --num_jobs=2   --get_mast_urls_dv_reports=true   --stellar_parameters_source=tess-spoc   --ruwe_source=unavailable   --task=planet-validation   --exominer_model=single   --max_model_workers=1   --plot_inputs_to_model

echo "Official ExoMiner++ output should now be under: $OUT"
find "$OUT" -type f \( -name 'predictions_spoc-tces_set.csv' -o -name '*prediction*.csv' \) -print || true
