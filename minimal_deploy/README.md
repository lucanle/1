# AI量化交易系统部署指南

## 环境变量配置
在部署前请设置以下环境变量：
```bash
export SUPABASE_URL="您的Supabase项目URL"
export SUPABASE_KEY="您的Supabase匿名密钥"
```

## API端点
- POST /token - 获取访问令牌
- GET /market - 获取市场数据
- POST /trade - 执行交易
- GET /trades - 获取交易历史

## 本地运行
```bash
pip install -r requirements.txt
uvicorn main:app --reload