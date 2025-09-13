import numpy as np
from model import TradingModel

# 生成测试数据
X_train = np.random.rand(100, 10)  # 100个样本，10个特征
y_train = np.random.randint(0, 2, 100)  # 二分类标签

# 初始化并训练模型
model = TradingModel(input_size=10)
model.model.fit(X_train, y_train)

# 测试预测
X_test = np.random.rand(5, 10)
predictions = model.predict(X_test)

print("测试预测结果:", predictions)
print("结果形状:", predictions.shape)