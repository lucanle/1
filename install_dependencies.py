import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required = [
    "numpy==1.19.5",  # 降级到兼容版本
    "fastapi==0.68.0",
    "uvicorn==0.15.0",
    "pydantic>=1.8.2",
    "python-jose[cryptography]==3.3.0",
    "passlib==1.7.4",
    "python-multipart==0.0.5",
    "dash==2.14.0",
    "dash-bootstrap-components==1.4.0",
    "plotly==5.18.0",
    "websockets==10.4",
    "gunicorn==20.1.0"
]

if __name__ == "__main__":
    for package in required:
        try:
            print(f"正在安装 {package}...")
            install(package)
            print(f"成功安装 {package}")
        except Exception as e:
            print(f"安装 {package} 失败: {str(e)}")
    print("所有依赖安装完成！")