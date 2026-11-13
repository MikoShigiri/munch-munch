from datetime import date, timedelta
from users import StudentUser
from pantry import Inventory, FoodItem
from budget import BudgetManager
from views import ConsoleView

class MunchMunchController:
    def __init__(self):
        # Initialize default mock data for demonstration
        self.user = StudentUser("alex_student", "alex@uni.edu", 300.0, "Main Campus Dorms")
        self.inventory = Inventory()
        self.budget_manager = BudgetManager(self.user.monthly_budget)
        self.view = ConsoleView()

        # Seed initial data
        self._load_initial_data()

    def _load_initial_data(self):
        self.inventory.add_item(FoodItem("Milk", 1, date.today() + timedelta(days=1), 2.50))
        self.inventory.add_item(FoodItem("Eggs", 12, date.today() + timedelta(days=4), 4.00))
        self.inventory.add_item(FoodItem("Spinach", 1, date.today() + timedelta(days=2), 1.80))
        self.budget_manager.add_expense("Campus Cafeteria Lunch", 6.50)

    def run(self):
        while True:
            choice = self.view.display_main_menu(self.user.username)
            
            if choice == "1":
                self.show_dashboard()
            elif choice == "2":
                self.handle_add_item()
            elif choice == "3":
                self.handle_log_meal()
            elif choice == "4":
                self.handle_recipe_recommendations()
            elif choice == "5":
                self.view.display_message("Logging out. Have a great study session!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.")

    def show_dashboard(self):
        spent = self.budget_manager.get_total_spent()
        remaining = self.budget_manager.get_remaining_budget()
        expiring = self.inventory.get_expiring_items()
        alert = self.budget_manager.check_threshold_alert()

        self.view.display_dashboard(
            user_desc=self.user.get_role_description(),
            total_budget=self.user.monthly_budget,
            spent=spent,
            remaining=remaining,
            expiring_items=expiring,
            budget_alert=alert
        )

    def handle_add_item(self):
        name, qty, days_to_expiry, cost = self.view.get_new_item_input()
        expiry = date.today() + timedelta(days=days_to_expiry)
        item = FoodItem(name, qty, expiry, cost)
        self.inventory.add_item(item)
        self.view.display_message(f"Successfully added {name} to your pantry inventory!")

    def handle_log_meal(self):
        item_name, cost = self.view.get_meal_log_input()
        try:
            self.budget_manager.add_expense(f"Meal: {item_name}", cost)
            self.inventory.remove_item(item_name, 1)
            self.view.display_message(f"Logged meal! Spent ${cost:.2f} and updated pantry.")
        except ValueError as e:
            self.view.display_message(str(e))

    def handle_recipe_recommendations(self):
        expiring = self.inventory.get_expiring_items()
        self.view.display_recipes(expiring)