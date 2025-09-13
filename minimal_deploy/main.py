from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import datetime
import random
# 内存数据库
trades_db = []
market_data = {
    "BTCUSDT": 50000.0,
    "ETHUSDT": 3000.0
}



class Trade(BaseModel):
    symbol: str
    side: str  # buy/sell
    amount: float
    price: float
    timestamp: str

app = FastAPI()

# 允许所有HTTP方法
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 显式添加HEAD路由
@app.api_route("/", methods=["HEAD"])
async def head_root():
    return {"message": "OK"}

@app.get("/")
async def root():
    return {"message": "AI量化交易系统"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# 用户认证端点
@app.post("/token")
async def login_for_access_token():
    # 实际项目中应实现完整认证流程
    return {"access_token": "fake-super-secret-token", "token_type": "bearer"}

# 市场数据端点
@app.get("/market")
async def get_market():
    price = round(50000 + random.uniform(-1000, 1000), 2)
    market_data["BTCUSDT"] = price
    return {
        "symbol": "BTCUSDT",
        "price": price,
        "timestamp": datetime.datetime.now().isoformat()
    }

# 交易执行端点
@app.post("/trade")
async def execute_trade(trade: Trade):
    trade_data = {
        "symbol": trade.symbol,
        "side": trade.side,
        "amount": trade.amount,
        "price": trade.price,
        "timestamp": datetime.datetime.now().isoformat(),
        "status": "executed"
    }
    trades_db.append(trade_data)
    return {
        "status": "success",
        "order_id": f"ORD-{random.randint(10000,99999)}",
        "executed_price": trade.price * (1 + random.uniform(-0.01, 0.01))
    }

# 获取交易历史
@app.get("/trades")
async def get_trade_history():
    return trades_db