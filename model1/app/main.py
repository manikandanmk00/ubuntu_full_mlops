
from fastapi import FastAPI
from app.schemas import HouseFeatures
from app.predict import make_prediction

app = FastAPI()

@app.get("/")
def root():
    return {"message": "House price prediction API is running."}

@app.post("/predict")
def predict_price(data: HouseFeatures):
    prediction = make_prediction(data.dict())
    return {"predicted_price": prediction}
