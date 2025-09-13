from typing import List, Dict, Tuple, Any
import threading

class SimplifiedMetrics:
    _numpy_available: bool = False
    _lock = threading.Lock()
    
    @classmethod
    def _init_numpy(cls):
        """初始化numpy状态"""
        with cls._lock:
            if not hasattr(cls, '_numpy_initialized'):
                try:
                    import numpy as np  # type: ignore
                    cls.np = np  # type: ignore
                    cls._numpy_available = True
                except ImportError:
                    cls.np = None  # type: ignore
                    cls._numpy_available = False
                cls._numpy_initialized = True
    
    def __init__(self):
        self._init_numpy()
    @classmethod
    def calculate_rsi(cls, prices: List[float], period: int = 14) -> List[float]:
        """RSI计算 (支持numpy和纯Python实现)"""
        if len(prices) < period:
            return []
            
        avg_gain: float = 0.0
        avg_loss: float = 0.0
        
        if cls._numpy_available and hasattr(cls, 'np') and cls.np is not None:
            np = cls.np  # type: ignore
            try:
                deltas = np.diff(prices)  # type: ignore
                gains = np.where(deltas > 0, deltas, 0)  # type: ignore
                losses = np.where(deltas < 0, -deltas, 0)  # type: ignore
                avg_gain = float(np.mean(gains[:period]))  # type: ignore
                avg_loss = float(np.mean(losses[:period]))  # type: ignore
            except Exception:
                with cls._lock:
                    cls._numpy_available = False
                # 回退到纯Python实现
                deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
                gains = [d if d > 0 else 0 for d in deltas]
                losses = [-d if d < 0 else 0 for d in deltas]
                avg_gain = sum(gains[:period]) / period
                avg_loss = sum(losses[:period]) / period
        else:
            deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
            gains = [d if d > 0 else 0 for d in deltas]
            losses = [-d if d < 0 else 0 for d in deltas]
            avg_gain = sum(gains[:period]) / period
            avg_loss = sum(losses[:period]) / period
            
        rs = avg_gain / avg_loss if avg_loss != 0 else 0
        return [100 - (100 / (1 + rs))] * len(prices)

    @staticmethod 
    def get_institutional_metrics() -> Dict[str, float]:
        """机构级指标简化版"""
        return {
            "mfi": 0.0,  # 资金流指标
            "oi": 0.0    # 持仓量变化
        }