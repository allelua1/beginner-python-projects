
# Store expenses as a list of dictionaries {category, amount, date}
# Functions to: add expense, total by category, show summary
# Use lambda + sorted() to show biggest expenses first
from datetime import date

expenses_list = [
    {"Category": "Food", "Amount": 2000, "Date": date(2026, 8, 24)}
]

def add_expense(expenses_list, category, amount, expense_date):
    expenses_list.append({
        "Category": category,
        "Amount": amount,
        "Date": expense_date
    })
    print(f'"{category}" category has been added successfully.')

def total_by_category(expenses_list):
    totals = {}
    for expense in expenses_list:
        category = expense["Category"]
        totals[category] = totals.get(category, 0) + expense["Amount"]

    print("Total by category:")
    for category, total in totals.items():
        print(f"  {category}: {total}")

def show_summary(expenses_list):
    sorted_expenses = sorted(expenses_list, key=lambda e: e["Amount"], reverse=True)
    print("------------- EXPENSES SUMMARY ------------------")
    print("Category\tAmount\tDate")
    for expense in sorted_expenses:
        print(
            f'{expense["Category"]}\t'
            f'{expense["Amount"]}\t'
            f'{expense["Date"].isoformat()}'
        )

add_expense(expenses_list, "Drinks", 5000, date(2026, 9, 15))
total_by_category(expenses_list)
show_summary(expenses_list)



