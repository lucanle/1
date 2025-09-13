#!/bin/bash
echo "启动AI量化交易系统(CloudStudio版)"

# 检查Python版本
python3 check_environment.py || exit 1

# 安装依赖
pip install -r requirements.txt || {
    echo "依赖安装失败"
    exit 1
}

# 启动主程序
python3 main.py --mode cloud