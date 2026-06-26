#!/usr/bin/env bash
set -euo pipefail

echo "Installing dependencies..."
python -m pip install -r requirements.txt

mkdir -p executed

NB_LIST=(
  "1_Data_Preprosessing.ipynb"
  "2_multi_models_stacking.ipynb"
  "3_CNN_Visualization.ipynb"
)

for nb in "${NB_LIST[@]}"; do
  echo "Executing $nb..."
  jupyter nbconvert --to notebook --execute "$nb" --output "executed/$nb"
done

echo "All notebooks executed. Outputs saved under executed/"
