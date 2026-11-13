from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username: str, email: str):
        self._username = username  # Encapsulated attribute
        self._email = email

    @property
    def username(self) -> str:
        return self._username

    @abstractmethod
    def get_role_description(self) -> str:
        pass


class StudentUser(User):
    def __init__(self, username: str, email: str, monthly_budget: float, campus_location: str):
        super().__init__(username, email)
        self._monthly_budget = monthly_budget
        self._campus_location = campus_location

    @property
    def monthly_budget(self) -> float:
        return self._monthly_budget

    @monthly_budget.setter
    def monthly_budget(self, amount: float):
        if amount < 0:
            raise ValueError("Budget cannot be negative.")
        self._monthly_budget = amount

    def get_role_description(self) -> str:
        return f"Student User at {self._campus_location} with a monthly budget of ${self._monthly_budget:.2f}"