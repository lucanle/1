import numpy as np
from typing import List, NamedTuple

class Order(NamedTuple):
    price: float
    amount: float
    is_bid: bool
    order_id: str

class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []
    
    def add_order(self, order: Order):
        if order.is_bid:
            self.bids.append(order)
            self.bids.sort(key=lambda x: -x.price)
        else:
            self.asks.append(order)
            self.asks.sort(key=lambda x: x.price)
    
    def cancel_order(self, order_id: str):
        self.bids = [o for o in self.bids if o.order_id != order_id]
        self.asks = [o for o in self.asks if o.order_id != order_id]
    
    @property
    def best_bid(self) -> float:
        return self.bids[0].price if self.bids else 0.0
    
    @property
    def best_ask(self) -> float:
        return self.asks[0].price if self.asks else 0.0