import asyncio
from typing import List, Dict, Any

class AIController:
    def __init__(self):
        self._polling_task = None
        self._symbols = []

    def on_data_received(self, data: Dict[str, Any]):
        """处理接收到的市场数据"""
        print(f"收到数据: {data}")

    async def start_polling(self, poller, symbols: List[str]):
        """启动HTTP轮询模式"""
        self._symbols = symbols
        
        async def fetch_data():
            while True:
                try:
                    for symbol in self._symbols:
                        data = await poller.fetch_data(
                            "/api/v3/ticker/price",
                            params={"symbol": symbol}
                        )
                        if data:
                            self.on_data_received(data)
                    await asyncio.sleep(5)  # 5秒轮询间隔
                except Exception as e:
                    print(f"轮询异常: {str(e)}")
                    await asyncio.sleep(10)  # 异常后等待10秒

        self._polling_task = asyncio.create_task(fetch_data())

    async def stop_real_time(self):
        """停止轮询"""
        if self._polling_task:
            self._polling_task.cancel()
            try:
                await self._polling_task
            except asyncio.CancelledError:
                pass
            self._polling_task = None