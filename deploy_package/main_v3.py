from fastapi import FastAPI, Request, Response, Form
import time
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import io
import asyncio
import signal
import uvicorn
import os
import base64
import hashlib
import hmac
import requests

# 导入自定义模块
from http_poller import HTTPPoller
from ai_quant_system.core.ai_controller import AICentralController
from deploy_package.institutional_metrics import InstitutionalMetrics
from technical_indicators import TechnicalIndicators
from short_term_strategy import ShortTermStrategy

# 初始化应用
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 初始化服务
okx = OKXService()
short_term_strategy = ShortTermStrategy()

# [其余保持原有路由和功能实现...]

if __name__ == "__main__":
    asyncio.run(main())