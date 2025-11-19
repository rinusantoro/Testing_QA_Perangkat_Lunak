import pytest
from unittest.mock import MagicMock

from shopping_cart import ShoppingCart
from item_service import ItemService
from price_service import PriceService

# ---------------------------------------
# Tahap 1: Test modul TOP dengan mock ItemService
# ---------------------------------------
def test_step1_cart_with_mock_item_service():
    cart = ShoppingCart()

    # mock item_service
    cart.item_service = MagicMock()

    # mock memperhitungkan qty → 1000 per unit
    cart.item_service.get_item_total.side_effect = lambda item, qty: 1000 * qty

    items = [("apple", 2), ("banana", 1)]

    total = cart.total_cart(items)

    # apple = 2 * 1000 = 2000
    # banana = 1 * 1000 = 1000
    assert total == 3000


# ---------------------------------------
# Tahap 2: Integrasi ShoppingCart + ItemService (PriceService di-mock)
# ---------------------------------------
def test_step2_cart_with_real_item_service_and_mock_price():
    item_service = ItemService()

    # mock price service → harga tetap 2000 untuk item apapun
    item_service.price_service = MagicMock()
    item_service.price_service.get_price.return_value = 2000

    cart = ShoppingCart()
    cart.item_service = item_service

    total = cart.total_cart([("apple", 2)])

    # total = 2000 * 2 qty
    assert total == 4000


# ---------------------------------------
# Tahap 3: Full Integration (semua modul asli)
# ---------------------------------------
def test_step3_full_integration():
    cart = ShoppingCart()

    items = [("apple", 2), ("banana", 3)]
    result = cart.total_cart(items)

    # harga asli:
    # apple = 5000 → 5000*2 = 10000
    # banana = 3000 → 3000*3 = 9000
    assert result == 19000
