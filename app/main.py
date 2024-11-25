"""
##################################################################
#                                                                #
#                      MAIN REST API FILE                        #
#                                                                #
##################################################################

This file will be the main file of your REST API.
Use it to add an endpoint /predict that will be used to ask your model
for predictions.

You can use any technology you find suitable to develop your REST API, but make sure
to explain how to make it work.
"""
import pickle

import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException, Request

#from pydantic import BaseModel
# We could define a pydantic datamodel (useful for data validation)
#class PredictionInput(BaseModel):


# Load model
with open('forecast-exercise/app/complete_model.pkl', 'rb') as file:
    model = pickle.load(file)

app = FastAPI()

@app.post('/predict')
async def predict(request: Request):
    """
    Endpoint to get sales predictions.
    Expects a JSON payload with necessary features.
    """
    try:
        # Get JSON data from the request
        data = await request.json()
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {e}")

    # Convert JSON data to DataFrame
    input_data = pd.DataFrame([data])
    
    # Ensure that all required features are present
    required_features = [
        # Lag features
        'SALES_LAG_1', 'SALES_LAG_2', 'SALES_LAG_3', 'SALES_LAG_4',
        'SALES_LAG_5', 'SALES_LAG_6', 'SALES_LAG_7', 'SALES_LAG_364',
        'sales_roll_mean_7', 'sales_roll_mean_30',

        # Date features
        'MONTH', 'WEEKDAY', 'DAY_OF_YEAR', 'DAY_OF_MONTH', 'quarter',
        'is_weekend', 'is_saturday', 'is_sunday', 'is_december',

        # Calendar variables
        'num_STATE_A', 'num_STATE_C', 'num_STATE_FA', 'num_STATE_FM',
        'num_STATE_CR', 'stores_open', 'stores_closed',
        'mean_OPENING_TIME_MIN', 'mean_CLOSING_TIME_MIN', 'mean_DURATION_MIN',

        # IPC variables
        'IPC_VALUE', 'IPC_LAG_1', 'IPC_LAG_2'
    ]

    # Check if all required features are in the input data
    missing_features = [feat for feat in required_features if feat not in input_data.columns]
    if missing_features:
        raise HTTPException(status_code=400, detail=f"Missing features: {missing_features}")

    # Fill missing values if necessary (e.g., with zeros or mean values)
    input_data = input_data.fillna(0)

    # Ensure the order of columns matches the training data
    input_data = input_data[required_features]

    # Make prediction
    try:
        prediction = model.predict(input_data)[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")

    # Return the prediction as a JSON response
    return {'predicted_sales': prediction}

if __name__ == '__main__':
    # Run the FastAPI app
    print("🌐 Your awesome REST API")
    uvicorn.run(app, host='0.0.0.0', port=8000)
