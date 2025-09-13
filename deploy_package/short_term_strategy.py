from typing import List, Dict
from technical_indicators import TechnicalIndicators

class ShortTermStrategy:
    def __init__(self):
        """初始化策略参数"""
        self.params = {
            # 基础参数
            'rsi_period': 14,
            'macd_fast': 12,
            'macd_slow': 26,
            'macd_signal': 9,
            'entry_threshold': 0.7,
            
            # 新增参数
            'volume_weight': 0.3,  # 成交量权重
            'timeframe_multiplier': 2,  # 多时间框架倍数
            'min_volume': 1000  # 最小成交量阈值
        }

    def analyze(self, candles: List[Dict[str, float]]) -> List[int]:
        """30分钟短线交易策略 (高级版)
        Args:
            candles: K线数据列表，需包含close,volume字段
        Returns:
            交易信号列表 (1:买入, -1:卖出, 0:持有)
        """
        # 参数验证
        required_fields = {'close', 'volume'}
        if not candles or any(field not in candles[0] for field in required_fields):
            return []
            
        min_bars = max(
            self.params['rsi_period'], 
            self.params['macd_slow'],
            self.params['timeframe_multiplier'] * 5
        )
        if len(candles) < min_bars:
            return []
            
        # 准备数据
        closes = [float(c['close']) for c in candles]
        volumes = [float(c['volume']) for c in candles]
        
        # 计算基础指标
        rsi = TechnicalIndicators.calculate_rsi(
            closes,
            int(self.params['rsi_period'])
        )
        
        # 计算成交量加权价格
        vwap = []
        for i in range(len(closes)):
            start = max(0, i - self.params['rsi_period'])
            period_closes = closes[start:i+1]
            period_volumes = volumes[start:i+1]
            if sum(period_volumes) > 0:
                vwap.append(
                    sum(p*v for p,v in zip(period_closes, period_volumes)) / 
                    sum(period_volumes)
                )
            else:
                vwap.append(closes[i])
        
        # 多时间框架分析
        multi_tf_signal = 0
        if len(closes) >= self.params['timeframe_multiplier'] * self.params['rsi_period']:
            multi_tf_closes = closes[::self.params['timeframe_multiplier']]
            multi_tf_rsi = TechnicalIndicators.calculate_rsi(
                multi_tf_closes,
                int(self.params['rsi_period'])
            )
            if multi_tf_rsi:
                last_rsi = multi_tf_rsi[-1]
                if last_rsi > self.params['entry_threshold'] * 100:
                    multi_tf_signal = 1
                elif last_rsi < (1 - self.params['entry_threshold']) * 100:
                    multi_tf_signal = -1
        
        signals = []
        for i in range(1, len(rsi)):
            # 基础信号
            signal = 0
            if volumes[i] < self.params['min_volume']:
                signals.append(0)
                continue
                
            if rsi[i] > self.params['entry_threshold'] * 100:
                signal = 1
            elif rsi[i] < (1 - self.params['entry_threshold']) * 100:
                signal = -1
                
            # 成交量确认
            volume_confirmation = (
                volumes[i] > self.params['volume_weight'] * sum(volumes[max(0,i-5):i])
            )
            
            # 多时间框架确认
            timeframe_confirmation = (
                multi_tf_signal == 0 or 
                multi_tf_signal == signal
            )
            
            if signal != 0 and volume_confirmation and timeframe_confirmation:
                signals.append(signal)
            else:
                signals.append(0)
                
        return signals