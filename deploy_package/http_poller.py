import asyncio
import aiohttp
from typing import Optional, Dict, Any

class HTTPPoller:
    def __init__(self, base_url: str = "https://api.binance.com"):
        self.session = aiohttp.ClientSession()
        self.base_url = base_url

    async def fetch_data(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        try:
            async with self.session.get(
                f"{self.base_url}{endpoint}",
                params=params
            ) as response:
                return await response.json()
        except Exception as e:
            print(f"HTTP请求失败: {str(e)}")
            return None

    async def close(self):
        await self.session.close()