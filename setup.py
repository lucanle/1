from setuptools import setup, find_packages

setup(
    name="ai_quant_system",
    version="0.1",
    packages=find_packages(include=['ai_quant_system*']),
    package_dir={'': '.'},
    install_requires=[
        'numpy',
        'pandas',
        'websockets'
    ],
)