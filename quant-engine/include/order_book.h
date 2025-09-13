#pragma once

#include <vector>
#include <string>

namespace QuantEngine {
    class OrderBook {
    public:
        struct Order {
            double price;
            double amount;
            bool is_bid;
            std::string order_id;
        };

        void add_order(const Order& order);
        void cancel_order(const std::string& order_id);
        double get_best_bid() const;
        double get_best_ask() const;

    private:
        std::vector<Order> bids_;
        std::vector<Order> asks_;
    };
}