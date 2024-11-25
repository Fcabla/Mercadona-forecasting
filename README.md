
# 📈 forecast-exercise

## Objective
The objective of this exercise is to evaluate the developer skills in time series analysis and forecasting using Machine Learning techniques. The developer is expected to demonstrate proficiency in data handling, predictive modeling, model validation, and interpretation of results.

## Exercise Description
Develop a predictive model to forecast the daily sales of a retail store chain from a provided time series. The task includes the following steps:
1. **🔍 Data Exploration:** Understand the dataset, identify trends, seasonality, and any anomalies.
2. **🧹 Data Cleaning:** Handle missing values, outliers, and perform any necessary data preprocessing.
3. **🎯 Feature Selection:** Select relevant features that could improve the predictive power of the model.
4. **🤖 Modeling:** Develop a predictive model using appropriate Machine Learning techniques.
5. **✅ Validation:** Validate the model using appropriate metrics and validation techniques.
6. **📊 Presentation of Results:** Interpret the results and present the findings in a clear and concise manner.

## Requirements
Use the dependency manager (and/or virtual environment) of your choice for this exercise. The following requirements are an example of proposal. Use any other relevant libraries for time series analysis and machine learning you need.

- python 3.10+
- pandas
- scikit-learn
- plotly

To reproduce the environment used for this project, please refer to the `requirements.txt` file, which contains all the necessary package installations.

## Directory Structure
```
forecast-exercise/
├── README.md
├── app
│   └── main.py
├── data
│   ├── calendar.csv
│   ├── ipc_history.csv
│   ├── sales_test_submission.csv
│   └── sales_train_dataset.csv
└── notebooks
    ├── 1-data-preparation.ipynb
    └── 2-model-training.ipynb
```

Inside the `data` folder, you will find a file named `sales_predictions_2019.csv`, which contains the "submission" results.

In the `app` folder, you will find:
- `app.py`: The API implementation.
- `test.py`: A sample API call for testing.
- The trained model from notebook 2 (model training) saved in pickle format.