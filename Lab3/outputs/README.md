# Lab 3: AI Programming Frameworks & Data Preparation

## Overview

This lab focuses on Python libraries and techniques used for data preparation, preprocessing, analysis, and visualization in Artificial Intelligence and Machine Learning.

The practical work is implemented using **Jupyter Notebook** and popular Python libraries such as NumPy, Pandas, Matplotlib, and Scikit-learn.

## Objectives

- Understand numerical computing using NumPy.
- Perform data manipulation and analysis using Pandas.
- Explore datasets using Exploratory Data Analysis (EDA).
- Identify and handle missing values and duplicate records.
- Apply different data encoding techniques.
- Perform feature engineering and feature selection.
- Understand train-test splitting.
- Explore basic Scikit-learn preprocessing techniques.

## Technologies Used

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Practical Topics Covered

| No. | Topic                           | Description                                                                    |
| --- | ------------------------------- | ------------------------------------------------------------------------------ |
| 1   | NumPy Fundamentals              | Arrays, indexing, slicing, mathematical operations, and statistical functions. |
| 2   | Pandas                          | Series, DataFrames, filtering, sorting, and data manipulation.                 |
| 3   | Exploratory Data Analysis (EDA) | Dataset exploration, statistical summaries, grouping, and visualization.       |
| 4   | Data Cleaning                   | Handling missing values, duplicate records, inconsistent values, and outliers. |
| 5   | Data Encoding                   | Label Encoding, Ordinal Encoding, and One-Hot Encoding.                        |
| 6   | Feature Engineering             | Creating new features from existing dataset columns.                           |
| 7   | Feature Selection               | Selecting relevant features using statistical methods and feature importance.  |
| 8   | Train-Test Split                | Dividing datasets into training and testing subsets using Scikit-learn.        |
| 9   | Scikit-learn                    | Introduction to machine learning preprocessing using StandardScaler.           |

## Project Structure

```text
Lab3/
├── outputs/
│   ├── DataCleaningFinalOutput.png
│   ├── DataCleaningMissingValues.png
│   ├── DataCleaningOriginalOutput.png
│   ├── DataEncodingOriginalOutput.png
│   ├── EDACGPADistribution.png
│   ├── EDACorrelationHeatmap.png
│   ├── EDAPlacementDistribution.png
│   ├── EDAScatterPlot.png
│   ├── EDASummary.png
│   ├── FeatureEngineeringOriginalOutput.png
│   ├── FeatureEngineeringOutput.png
│   ├── FeatureImportanceGraph.png
│   ├── FeatureSelectionFinalOutput.png
│   ├── LabelEncodingOutput.png
│   ├── NumPyStudentMarksOutput.png
│   ├── OneHotEncodingOutput.png
│   ├── OrdinalEncodingOutput.png
│   ├── PandasStudentAnalysisOutput.png
│   ├── ScikitLearnStandardScalerOutput.png
│   ├── SelectKBestOutput.png
│   ├── StudentPlacementEncodingOutput.png
│   └── TrainTestSplitOutput.png
├── CleanedStudentDataset.csv
├── DataPreprocessing.ipynb
├── EncodedStudentDataset.csv
├── FeatureEngineeredDataset.csv
├── SelectedFeaturesDataset.csv
├── StudentPerformance.csv
└── students.csv
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd IC2K2305-AI-Abdul_Rehman
```

### 3. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install required libraries

```bash
python -m pip install numpy pandas matplotlib scikit-learn jupyter
```

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open `Lab3/DataPreprocessing.ipynb` and execute the cells sequentially.

## Output Screenshots

All practical execution screenshots and visualizations are stored in the `outputs/` directory.

The notebook also generates CSV files containing cleaned, encoded, and feature-engineered datasets.

## Conclusion

This lab provided practical experience with essential Python libraries and data preparation techniques used in Artificial Intelligence and Machine Learning.

It covered the process of exploring, cleaning, transforming, visualizing, and preparing datasets for machine learning tasks. It also introduced feature engineering, feature selection, train-test splitting, and basic Scikit-learn preprocessing.
