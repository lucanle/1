import asyncio
import websockets
from typing import Optional

class WebSocketManager:
    def __init__(self):
        self._connections = {}

    async def connect(self, url: str, timeout: float = 10.0, retries: int = 3) -> Optional[websockets.WebSocketClientProtocol]:
        for attempt in range(1, retries + 1):
            try:
                return await asyncio.wait_for(
                    websockets.connect(url),
                    timeout=timeout
                )
            except Exception as e:
                if attempt == retries:
                    raise
                await asyncio.sleep(1)
        return None

    async def close_all(self):
        for ws in self._connections.values():
            await ws.close()
        self._connections.clear()