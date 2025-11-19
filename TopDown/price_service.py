class PriceService:
    def get_price(self, item_name):
        price_list = {
            "apple": 5000,
            "banana": 3000,
            "milk": 10000
        }
        return price_list.get(item_name, 0)
