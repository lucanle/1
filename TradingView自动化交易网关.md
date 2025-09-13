# 零成本自动化交易系统部署指南

## 1. 基础设施准备
- [x] GitHub账号注册
- [x] Vercel账号注册
- [x] Supabase账号注册
- [x] TradingView Pro账号（免费版可用）

## 2. 数据库配置
```sql
-- 创建表结构（见上文）
```

## 3. 后端部署
1. 安装Vercel CLI
```bash
npm install -g vercel
```

2. 部署命令
```bash
vercel --prod
```

## 4. 前端部署
1. 构建生产包
```bash
npm run build
```

2. 部署到Vercel
```bash
vercel --prod
```

## 5. 系统验证
1. Webhook测试
```bash
curl -X POST [你的URL] -d '{"symbol":"BTCUSDT","direction":"BUY","price":50000}'
```

2. 数据检查
```sql
SELECT * FROM signals LIMIT 5;
```

## 6. 监控系统访问
访问Vercel提供的域名查看实时交易面板