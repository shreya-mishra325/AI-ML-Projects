from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("house_model.pkl")

class HouseInput(BaseModel):
    area: int
    bedrooms: int

@app.post("/predict")
def predict(data: HouseInput):
    price = model.predict([[data.area, data.bedrooms]])
    return {"predicted_price": float(price[0])}