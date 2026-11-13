from datetime import date, timedelta

class FoodItem:
    def __init__(self, name: str, quantity: int, expiry_date: date, cost: float):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date
        self.cost = cost

    def is_expiring_soon(self, days_threshold: int = 3) -> bool:
        """Returns True if the item expires within the threshold days."""
        today = date.today()
        return 0 <= (self.expiry_date - today).days <= days_threshold

    def is_expired(self) -> bool:
        return date.today() > self.expiry_date


class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item: FoodItem):
        self._items.append(item)

    def remove_item(self, name: str, quantity: int = 1):
        for item in self._items:
            if item.name.lower() == name.lower():
                item.quantity -= quantity
                if item.quantity <= 0:
                    self._items.remove(item)
                return True
        return False

    def get_expiring_items(self) -> list[FoodItem]:
        return [item for item in self._items if item.is_expiring_soon()]

    @property
    def items(self) -> list[FoodItem]:
        return self._items