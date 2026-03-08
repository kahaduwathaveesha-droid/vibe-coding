def budget_tracker():
    try:
        # 1. Asks for the total budget.
        total_budget = float(input("Enter your total monthly budget (LKR): "))
        current_balance = total_budget
        
        print("\nEnter up to 3 expenses (or type 'done' to finish early):")
        
        # 2. Allows entering 3 expenses OR stopping early with "done"
        for i in range(1, 4):
            entry = input(f"Enter expense {i}: ").strip().lower()
            
            if entry == 'done':
                break
                
            try:
                expense = float(entry)
                current_balance -= expense
            except ValueError:
                print("Invalid input. Skipping this entry.")
        
        # 3. Finally, displays the remaining amount from the budget.
        print(f"\nRemaining amount from the budget: {current_balance:.2f} LKR")
        
        # 4. Shows the "Warning: Low Funds" message if below 500 LKR
        if current_balance < 500:
            print("Warning: Low Funds")
            
    except ValueError:
        print("Invalid input. Please enter a numerical value for the budget.")

if __name__ == "__main__":
    budget_tracker()
