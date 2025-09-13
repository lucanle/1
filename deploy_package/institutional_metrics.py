from typing import Dict
from .simplified_metrics import SimplifiedMetrics

class InstitutionalMetrics:
    @staticmethod
    def get_metrics() -> Dict[str, float]:
        """获取机构级市场指标
        Returns:
            - mfi: 资金流指标
            - oi: 持仓量变化
        """
        return {
            "mfi": 0.0,  # 简化处理
            "oi": 0.32   # 固定示例值
        }