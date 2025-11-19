import unittest
from shopping_cart import ShoppingCart

# -------- STUB (lapisan bawah belum diimplementasikan) --------
class ItemServiceStub:
    def get_item_total(self, item_name, qty):
        return 1000 * qty  # nilai dummy


class ShoppingCartStub(ShoppingCart):
    def __init__(self):
        self.item_service = ItemServiceStub()


class TestTopDownIntegration(unittest.TestCase):

    # Tahap 1: Test module TOP dengan stub
    def test_step1_top_with_stub(self):
        cart = ShoppingCartStub()
        items = [("apple", 2), ("banana", 1)]
        result = cart.total_cart(items)
        self.assertEqual(result, 3000)  # 1000*2 + 1000*1

    # Tahap 2: Test integrasi ShoppingCart + ItemService asli
    def test_step2_with_real_item_service(self):
        from item_service import ItemService
        cart = ShoppingCart()
        cart.item_service = ItemService()  # pakai modul asli

        items = [("apple", 2)]  # harga asli apple = 5000
        result = cart.total_cart(items)
        self.assertEqual(result, 10000)

    # Tahap 3: Test integrasi semua modul (full integration)
    def test_step3_full_integration(self):
        cart = ShoppingCart()
        items = [("apple", 2), ("banana", 3)]
        result = cart.total_cart(items)
        # 5000*2 + 3000*3 = 10000 + 9000
        self.assertEqual(result, 19000)


if __name__ == "__main__":
    unittest.main()
