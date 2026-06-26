Param()

Write-Host "Installing dependencies..."
python -m pip install -r requirements.txt

if (-Not (Test-Path -Path executed)) {
    New-Item -ItemType Directory -Path executed | Out-Null
}

$notebooks = @(
    '1_Data_Preprosessing.ipynb',
    '2_multi_models_stacking.ipynb',
    '3_CNN_Visualization.ipynb'
)

foreach ($nb in $notebooks) {
    Write-Host "Executing $nb..."
    jupyter nbconvert --to notebook --execute $nb --output "executed/$nb"
}

Write-Host "All notebooks executed. Outputs saved under executed/"
