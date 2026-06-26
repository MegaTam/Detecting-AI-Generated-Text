# Advanced Machine Learning — Course Project

This folder contains Jupyter Notebooks for experiments and analysis on distinguishing human-written texts from AI-generated texts.

**Contents**
- `1_Data_Preprosessing.ipynb`: Data preprocessing and cleaning (tokenization, tokenization to vectors, etc.).
- `2_multi_models_stacking.ipynb`: Building and evaluating multiple models (KNN, Random Forest, stacking ensemble, etc.).
- `3_CNN_Visualization.ipynb`: Text-CNN implementation and visualization (filters / feature maps).

**Quick Start**
1. Install dependencies (use a virtual environment):

	```bash
	pip install -r requirements.txt
	```

2. Open and run the notebooks in order: `1_Data_Preprosessing.ipynb`, then `2_multi_models_stacking.ipynb`, and finally `3_CNN_Visualization.ipynb`.

**Data**
- Source: Kaggle competition (processed CSV included in the project). 
- Example size: ~29,133 English texts (see notebooks for exact splits and files). 
- Labels: `0` = human-written, `1` = LLM-generated.

**Models & Methods**
- Traditional ML: KNN and Random Forest as base learners, Logistic Regression as a meta-learner for stacking.
- Deep Learning: Text-CNN (Embedding → Conv → Pool → Dense) for end-to-end training and visualization.
- Text processing: tokenization, frequency-based tokenizers, and vectorization methods to transform text into numerical features.

**Sample Results**
- Logistic Regression: Accuracy ≈ 0.60
- KNN: Accuracy ≈ 0.67
- Random Forest: Accuracy ≈ 0.72
- Stacking: Accuracy ≈ 0.71
- Text-CNN: Accuracy ≈ 0.66

(For detailed experimental settings, hyperparameters and evaluation metrics, see the experiment sections inside each notebook.)

**Environment Recommendations**
- Python 3.8+. Use a virtual environment (`venv` or `conda`).
- If using a GPU, install a compatible deep learning framework (TensorFlow or PyTorch) and CUDA drivers.

**Requirements Check & Example Run Scripts**

This project includes a small helper script to verify that packages listed in `requirements.txt` are installed with compatible versions, plus example scripts to execute the notebooks end-to-end.

- `check_requirements.py`: Verify installed packages against `requirements.txt` and report missing or incompatible packages.
- `run_all_notebooks.sh`: Bash script to install deps and execute all notebooks (creates `executed/` outputs).
- `run_all_notebooks.ps1`: PowerShell equivalent for Windows users.

Usage examples:

1) Quick requirements check (preferred before running notebooks):

```bash
python check_requirements.py
```

2) Run all notebooks (bash):

```bash
bash run_all_notebooks.sh
```

3) Run all notebooks (PowerShell):

```powershell
.\run_all_notebooks.ps1
```

Notes:
- The run scripts use `jupyter nbconvert --execute` to run notebooks non-interactively and save executed copies under the `executed/` folder.
- Running the notebooks may take time and may require additional system resources (RAM/GPU) depending on model choices.

---

*This project is a CUHKSZ-DDA4210 course assignment.*

