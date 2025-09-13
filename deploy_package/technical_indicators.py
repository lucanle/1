from typing import List

class TechnicalIndicators:
    @staticmethod
    def calculate_rsi(prices: List[float], period: int = 14) -> List[float]:
        """计算相对强弱指数(RSI)
        Args:
            prices: 价格序列
            period: 计算周期 (默认14)
        Returns:
            RSI值列表
        """
        if len(prices) < period or period <= 0:
            return []
            
        deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        gains = [d if d > 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]
        
        avg_gain = sum(gains[:period]) / period
        avg_loss = sum(losses[:period]) / period
        
        rs = avg_gain / avg_loss if avg_loss != 0 else 0
        return [100 - (100 / (1 + rs))] * len(prices)