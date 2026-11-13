class BudgetManager:
    def __init__(self, total_budget: float):
        self._total_budget = total_budget
        self._expenses = []  # List of dicts or transaction objects

    def add_expense(self, description: str, amount: float):
        if amount > self.get_remaining_budget():
            raise ValueError("Warning: Expense exceeds remaining budget limit!")
        self._expenses.append({"description": description, "amount": amount})

    def get_total_spent(self) -> float:
        return sum(exp["amount"] for exp in self._expenses)

    def get_remaining_budget(self) -> float:
        return self._total_budget - self.get_total_spent()

    def check_threshold_alert(self, warning_percentage: float = 0.8) -> bool:
        """Returns True if spending has exceeded the warning percentage of the budget."""
        return self.get_total_spent() >= (self._total_budget * warning_percentage)