from price_service import PriceService

class ItemService:
    def __init__(self):
        self.price_service = PriceService()

    def get_item_total(self, item_name, qty):
        return self.price_service.get_price(item_name) * qty
