from abc import ABC, abstractmethod
from typing import List, Optional


class PantryItem:
    """Represents an individual food item or grocery entry."""
    
    def __init__(self, name: str, cost: float, days_until_expiration: int, quantity: int):
        self._name = name
        self._cost = cost
        self._days_until_expiration = days_until_expiration
        self._quantity = quantity

    @property
    def name(self) -> str:
        return self._name

    @property
    def cost(self) -> float:
        return self._cost

    @property
    def days_until_expiration(self) -> int:
        return self._days_until_expiration

    @property
    def quantity(self) -> int:
        return self._quantity

    def consume(self, qty: int) -> None:
        """Deducts quantity from the pantry item."""
        if qty >= self._quantity:
            self._quantity = 0
        else:
            self._quantity -= qty

    def is_expiring_soon(self) -> bool:
        """Alert threshold rule: expiring within 3 days."""
        return self._days_until_expiration <= 3 and self._quantity > 0


class User(ABC):
    """Abstract Base Class for Application Users."""
    
    def __init__(self, username: str, email: str, password: str | None = None):
        self._username = username
        self._email = email
        self._password = password

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    def authenticate(self, password: str) -> bool:
        return self._password is not None and self._password == password

    @abstractmethod
    def get_role_description(self) -> str:
        """Polymorphic method required for concrete user subclasses."""
        pass


class StudentUser(User):
    """Concrete User class inheriting from User with budget capabilities."""
    
    def __init__(self, username: str, email: str, monthly_budget: float, campus_location: str, password: str | None = None):
        super().__init__(username, email, password)
        self._monthly_budget = monthly_budget
        self._campus_location = campus_location
        self._total_spent = 0.0

    @property
    def email(self) -> str:
        return self._email

    @property
    def campus_location(self) -> str:
        return self._campus_location

    @property
    def monthly_budget(self) -> float:
        return self._monthly_budget

    @property
    def total_spent(self) -> float:
        return self._total_spent

    @property
    def remaining_budget(self) -> float:
        return self._monthly_budget - self._total_spent

    def add_expense(self, amount: float) -> None:
        self._total_spent += amount

    def get_role_description(self) -> str:
        return f"Student User at {self._campus_location} with a monthly budget of ${self._monthly_budget:.2f}"


class PantryModel:
    """Model managing application inventory data and state."""
    
    def __init__(self):
        self._current_user: Optional[StudentUser] = None
        self._inventory: List[PantryItem] = []

    def set_user(self, user: StudentUser) -> None:
        self._current_user = user

    def get_user(self) -> Optional[StudentUser]:
        return self._current_user

    def add_item(self, name: str, cost: float, exp_days: int, qty: int) -> PantryItem:
        item = PantryItem(name, cost, exp_days, qty)
        self._inventory.append(item)
        if self._current_user:
            self._current_user.add_expense(cost * qty)
        return item

    def get_inventory(self) -> List[PantryItem]:
        return self._inventory

    def consume_item(self, index: int, qty: int) -> bool:
        if 0 <= index < len(self._inventory):
            self._inventory[index].consume(qty)
            return True
        return False