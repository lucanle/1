from feast import FeatureStore, Entity, FeatureView
from datetime import timedelta
import pandas as pd

# 定义实体
ticker = Entity(name="ticker", join_keys=["ticker"])

# 定义特征视图
ticker_features = FeatureView(
    name="ticker_features",
    entities=[ticker],
    ttl=timedelta(days=1),
    online=True,
    batch_source=...,  # 替换为实际数据源
    features=[
        Field(name="price", dtype=Float32),
        Field(name="volume", dtype=Float32),
        Field(name="sma_10", dtype=Float32),
    ]
)