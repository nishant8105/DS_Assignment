# Titanic Survival Prediction using Naive Bayes

This project implements a machine learning pipeline to predict passenger survival on the Titanic using the **Naive Bayes** algorithm. It covers the full data science workflow from data exploration and preprocessing to model training and evaluation.

## Project Structure

- `naive_bayes_titanic.ipynb`: The main Jupyter Notebook containing the implementation.
- `titanic.csv`: The dataset containing passenger information (features and survival labels).
- `README.md`: Project documentation.

## Features Used

The model utilizes the following features from the dataset:
- `Pclass`: Passenger class (1st, 2nd, or 3rd).
- `Sex`: Gender of the passenger (Encoded: Male=0, Female=1).
- `Age`: Age of the passenger (Missing values imputed with the median).
- `SibSp`: Number of siblings/spouses aboard.
- `Parch`: Number of parents/children aboard.
- `Fare`: Ticket price.
- `Embarked`: Port of embarkation (Encoded: Cherbourg=0, Queenstown=1, Southampton=2).

## Methodology

1.  **Exploratory Data Analysis (EDA)**: Inspection of data types, summary statistics, and identifying missing values.
2.  **Data Preprocessing**:
    *   **Imputation**: Missing `Age` values were filled with the median; missing `Embarked` values were filled with the mode.
    *   **Encoding**: Categorical variables (`Sex`, `Embarked`) were converted into numerical formats.
    *   **Feature Selection**: Selection of relevant features for prediction.
3.  **Model Training**:
    *   Split the data into training (80%) and testing (20%) sets using stratification.
    *   Implemented the `GaussianNB` classifier from `scikit-learn`.
4.  **Evaluation**:
    *   The model's performance was evaluated using Accuracy, a Confusion Matrix, and a detailed Classification Report (Precision, Recall, F1-Score).

## Results

- **Accuracy**: Approximately **77-80%**.
- **Insights**: The model confirms that gender (`Sex`) and socio-economic status (`Pclass`) were primary factors in survival probability, aligning with historical "women and children first" protocols.

## Requirements

To run this notebook, you need the following libraries:
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`

You can install them via pip:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Usage

1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook naive_bayes_titanic.ipynb
   ```
2. Run all cells to see the exploration, training, and results.
