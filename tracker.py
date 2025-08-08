import csv
import matplotlib.pyplot as plt

class Expense:
    def __init__(self, amount, category, date, description=""):
        self.amount = amount
        self.category = category
        self.note = description
        self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.filename = "my_expenses.csv"
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader) 
                for row in reader:
                    amount, category, note, date = row
                    self.expenses.append(Expense(float(amount), category, date, note))
        except (FileNotFoundError, StopIteration):
            self.expenses = []

    def save_data(self):
        with open(self.filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['amount', 'category', 'note', 'date'])
            for exp in self.expenses:
                writer.writerow([exp.amount, exp.category, exp.note, exp.date])

    def add_expense(self):
        print("\n-- ADD YOUR NEW EXPENSE --")
        try:
            amount = float(input("Enter the amount of money you spend : "))
            category = input("enter category: ").lower()
            date = input("Enter the date: ")
            note = input("Add a note (optional): ")
            
            new_expense = Expense(amount, category, date, note)
            self.expenses.append(new_expense)
            self.save_data()
            
            print(f"\n✅ Added ₹{amount:.2f} to '{category}'!")
        except ValueError:
            print("\n❌ Invalid input. Please enter a valid number for the amount.")

    def show_all(self):
        if not self.expenses:
            print("\nNo expenses found. Try adding one first!")
            return    
        print("\n-- ALL EXPENSES --")
        sorted_expenses = sorted(self.expenses, key=lambda x: x.date, reverse=True)
        for i, exp in enumerate(sorted_expenses, 1):
            print(f"{i}. ₹{exp.amount:<7.2f} - {exp.category.capitalize()}")
            if exp.note:
                print(f"   Note: {exp.note}")
            print(f"   Date: {exp.date}\n")

    def chart_summary(self):
        if not self.expenses:
            print("\nNo data to summarize. Please add an expense first.")
            return

        categories = {}
        for exp in self.expenses:
            categories[exp.category] = categories.get(exp.category, 0) + exp.amount
            
        if not categories:
            print("\nNo categories to plot.")
            return

        labels = list(categories.keys())
        totals = list(categories.values())
        fig, ax = plt.subplots()
        ax.pie(totals, labels=labels, startangle=90)
        ax.set_title("Expense Summary by Category")
        ax.axis('equal')  
        print("\n processing your spending summary chart..")
        plt.show()

    def graph_summary(self):
        if not self.expenses:
            print("\nNo data to summarize. Please add an expense first.")
            return
        categories = {}
        for exp in self.expenses:
            categories[exp.category] = categories.get(exp.category, 0) + exp.amount
            
        if not categories:
            print("\nNo categories to plot.")
            return

        labels = list(categories.keys())
        totals = list(categories.values())
        plt.figure(figsize=(10, 6)) 
        plt.bar(labels, totals, color='red')
        plt.xlabel("Category")
        plt.ylabel("Amount Spent (₹)")
        plt.title("Expense Summary by Category")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout() 
        print("\n📊 Generating your spending summary bar chart...")
        plt.show()



def main():
    print("Welcome to Expense Tracker")
    tracker = ExpenseTracker()
    
    while True:
        print("\n--- MENU ---")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Show spending summary chart")
        print("4. Show spending summary graph")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.show_all()
        elif choice == '3':
            tracker.chart_summary()
        elif choice == '4':
            tracker.graph_summary()
        elif choice == '5':
            print("\nGoodbye! Your data has been saved.")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        if choice in ['1', '2', '3']:
             input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
