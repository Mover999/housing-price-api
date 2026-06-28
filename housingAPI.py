
from fastapi import FastAPI, Form
from pydantic import BaseModel
#from typing import Annotated
from typing_extensions import Annotated
from sklearn.pipeline  import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

from housing_transformer  import HousingFeatEng

import uvicorn

import joblib

loaded_model = joblib.load("lr_model.joblib")

app = FastAPI()


class Housing(BaseModel):
    #username: str
    #password: str
    longitude: float
    latitude : float
    housing_median_age : float
    total_rooms: int
    total_bedrooms : float
    population: int
    households :int
    median_income: float
    ocean_proximity: str

      #==========================================
@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": loaded_model is not None}
    
@app.post("/prediction/")
async def prediction(housing: Annotated[Housing, Form()]):
    print()
   
    print()
    dumped_data = housing.model_dump()

# 2. Pass it as a list to the DataFrame constructor
    df = pd.DataFrame([dumped_data])
    print()
    predictions = loaded_model.predict(df)
      
    #return {"survived": int(predictions[0]), "probability": probs[[0,0]]}
    #predictions = loaded_model.predict(df)
    return {"house_price": float(predictions[0])}

   


