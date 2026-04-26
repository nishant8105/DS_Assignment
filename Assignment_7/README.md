# Cardiac Disease Diagnosis Analysis

This project provides a comprehensive machine learning pipeline to diagnose heart disease using patient clinical data. It features advanced preprocessing, multiple model comparisons, and deep clinical insights.

## Project Structure
- `cardiac.ipynb`: The main analysis notebook.
- `heart.csv`: The dataset containing 303 medical records.

## Features
- **Exploratory Data Analysis**: 
  - Univariate analysis (histograms for numerical features, countplots for categorical features)
  - Bivariate analysis (pairplot)
  - Correlation analysis
  - Detailed statistical summaries (mean, median, Q1, Q3)
  - Missing value and duplicate detection

- **Data Preprocessing**:
  - One-hot encoding for categorical variables (cp, restecg, thal)
  - Type conversion for binary features
  - Train-test split with stratification (80-20)

- **Model Comparison**:
  - K-Nearest Neighbors (KNN) with StandardScaler pipeline
  - Support Vector Machine (SVM) with StandardScaler pipeline
  - Decision Tree
  - Random Forest

- **Hyperparameter Tuning**:
  - GridSearchCV with StratifiedKFold cross-validation
  - Optimized for **Recall** to prioritize detecting heart disease cases

- **Evaluation Metrics**:
  - Accuracy, Precision, Recall, F1-Score
  - Classification reports

## Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

### Installation
1. Clone the repository or download the project files.
2. Ensure `heart.csv` is in the same directory as the notebook.
3. Install dependencies:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```

### Usage
1. Open the `cardiac.ipynb` notebook.
2. Run all cells to reproduce the analysis.

## Model Selection Notes
- All models are optimized for **Recall** using GridSearchCV
- KNN and SVM use StandardScaler pipelines for feature normalization
- Decision Tree and Random Forest use criterion (gini/entropy) and depth parameters
- The notebook evaluates models on both training and test sets



