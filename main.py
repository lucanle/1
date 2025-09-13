# type: ignore
import asyncio
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from ai_quant_system.core import ai_controller  # noqa  # type: ignore

def main():
    """系统主入口"""
    # 初始化控制器
    controller = ai_controller.AICentralController(
        strategy_pool=[],
        data_provider=None,
        compound_engine=None,
        model_manager=None
    )
    
    # 示例：启动实时交易
    symbols = ['BTCUSDT', 'ETHUSDT']
    asyncio.run(controller.start_real_time(symbols))

if __name__ == '__main__':
    main()