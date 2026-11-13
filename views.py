from pantry import FoodItem

class ConsoleView:
    def display_main_menu(self, username: str) -> str:
        print("\n" + "="*40)
        print(f" 🍎 MUNCH MUNCH — Student Meal Tracker ({username})")
        print("="*40)
        print("1. View Dashboard & Alerts")
        print("2. Add Item to Pantry")
        print("3. Log Meal / Expense")
        print("4. Get Pantry-to-Plate Recipes (Expiring Soon)")
        print("5. Exit")
        return input("Select an option (1-5): ").strip()

    def display_dashboard(self, user_desc: str, total_budget: float, spent: float, 
                          remaining: float, expiring_items: list[FoodItem], budget_alert: bool):
        print("\n--- DASHBOARD SUMMARY ---")
        print(f"Profile: {user_desc}")
        print(f"Monthly Budget: ${total_budget:.2f}")
        print(f"Total Spent:    ${spent:.2f}")
        print(f"Remaining:      ${remaining:.2f}")
        
        if budget_alert:
            print("⚠️ ALERT: You have used 80% or more of your monthly budget!")

        print("\nItems Expiring Soon (Next 3 Days):")
        if not expiring_items:
            print("  None! Your pantry is fresh.")
        else:
            for item in expiring_items:
                print(f"  - {item.name} (Qty: {item.quantity}) expires on {item.expiry_date}")

    def get_new_item_input(self) -> tuple[str, int, int, float]:
        print("\n--- ADD PANTRY ITEM ---")
        name = input("Item name: ").strip()
        qty = int(input("Quantity: ").strip())
        days_to_expiry = int(input("Days until expiration: ").strip())
        cost = float(input("Estimated cost ($): ").strip())
        return name, qty, days_to_expiry, cost

    def get_meal_log_input(self) -> tuple[str, float]:
        print("\n--- LOG CONSUMED MEAL ---")
        item_name = input("Pantry ingredient used: ").strip()
        cost = float(input("Out-of-pocket meal cost ($): ").strip())
        return item_name, cost

    def display_recipes(self, expiring_items: list[FoodItem]):
        print("\n🍳 PANTRY-TO-PLATE RECOMMENDATIONS")
        if not expiring_items:
            print("No items are expiring urgently. Cook whatever you like!")
            return
        
        print("Use these expiring ingredients before they spoil:")
        names = [item.name for item in expiring_items]
        print(f" -> Ingredients to prioritize: {', '.join(names)}")
        print("\n💡 Suggestion: Quick Dorm-Friendly Frittata or Stir-fry using your " + ' & '.join(names) + "!")

    def display_message(self, message: str):
        print(f"\n[INFO] {message}")