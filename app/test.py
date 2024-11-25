"""
Example of a request to the predict API
"""

import requests

URL = 'http://127.0.0.1:8000/predict'

def main():
    data = {
        "SALES_LAG_1": 10000.0,
        "SALES_LAG_2": 9800.0,
        "SALES_LAG_3": 9700.0,
        "SALES_LAG_4": 9600.0,
        "SALES_LAG_5": 9500.0,
        "SALES_LAG_6": 9400.0,
        "SALES_LAG_7": 9300.0,
        "SALES_LAG_364": 9100.0,
        "sales_roll_mean_7": 9614.29,
        "sales_roll_mean_30": 9700.0,
        "MONTH": 1,
        "WEEKDAY": 2,
        "DAY_OF_YEAR": 15,
        "DAY_OF_MONTH": 15,
        "quarter": 1,
        "is_weekend": 0,
        "is_saturday": 0,
        "is_sunday": 0,
        "is_december": 0,
        "num_STATE_A": 1600,
        "num_STATE_C": 30,
        "num_STATE_FA": 5,
        "num_STATE_FM": 3,
        "num_STATE_CR": 0,
        "stores_open": 1608,
        "stores_closed": 38,
        "mean_OPENING_TIME_MIN": 480.0,
        "mean_CLOSING_TIME_MIN": 1260.0,
        "mean_DURATION_MIN": 780.0,
        "IPC_VALUE": 1.5,
        "IPC_LAG_1": 1.4,
        "IPC_LAG_2": 1.3
    }
    response = requests.post(URL, json=data)
    print(response.json())

if __name__ == '__main__':
    main()
