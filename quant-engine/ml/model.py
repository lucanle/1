from sklearn.ensemble import RandomForestClassifier
import numpy as np

class TradingModel:
    def __init__(self, input_size):
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=5,
            random_state=42
        )
        self.input_size = input_size
    
    def predict(self, x):
        if x.ndim == 3:  # 保持LSTM输入格式兼容
            x = x.reshape(-1, self.input_size)
        probs = self.model.predict_proba(x)
        return np.array([p[1] for p in probs], dtype=np.float32)  # 显式指定类型以兼容旧版numpy