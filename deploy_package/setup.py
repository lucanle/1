from setuptools import setup, find_packages

setup(
    name="deploy_package",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        # 添加其他依赖
    ],
)