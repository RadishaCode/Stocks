from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf

app = FastAPI(title="Stock Terminal Pro")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"status":"Stock Terminal Pro Running"}

@app.get("/stock/{ticker}")
def stock(ticker:str):
    data=yf.Ticker(ticker.upper()+".JK")
    history=data.history(period="1d")
    if history.empty:
        return {"error":"No data"}
    return {
        "ticker":ticker.upper(),
        "price":float(history["Close"].iloc[-1])
    }
