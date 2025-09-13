from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
import numpy as np
from ai_quant_system.ai_controller import AICentralController
from auth import (
    User, Token, authenticate_user,
    create_access_token, get_current_active_user,
    has_permission, oauth2_scheme
)
from datetime import timedelta

app = FastAPI()
model = AICentralController(
    strategy_pool=[],
    data_provider=None,
    compound_engine=None,
    model_manager=None
)

@app.get("/")
@app.head("/")
def read_root():
    return {"message": "AI Quant System API"}

@app.get("/health") 
@app.head("/health")
def health_check():
    return {"status": "OK"}

from fastapi import HTTPException
from pydantic import BaseModel

class PredictRequest(BaseModel):
    data: List[float]
    min_length: int = 10
    max_length: int = 100

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/predict")
async def predict(
    request: PredictRequest,
    current_user: User = Depends(get_current_active_user)
):
    if not has_permission(current_user, "user"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions"
        )
    try:
        if not hasattr(model, 'generate_combined_signal'):
            raise AttributeError("Model missing required method")
            
        if len(request.data) < request.min_length:
            raise ValueError(f"Input too short (min {request.min_length})")
            
        if len(request.data) > request.max_length:
            raise ValueError(f"Input too long (max {request.max_length})")
            
        X = np.array(request.data, dtype=np.float32)
        preds = model.generate_combined_signal(X)
        return {
            "status": "success",
            "predictions": preds,
            "model": model.__class__.__name__
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )