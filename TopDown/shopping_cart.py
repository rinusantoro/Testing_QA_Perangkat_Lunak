from item_service import ItemService

class ShoppingCart:
    def __init__(self):
        self.item_service = ItemService()

    def total_cart(self, items):
        total = 0
        for item_name, qty in items:
            total += self.item_service.get_item_total(item_name, qty)
        return total
