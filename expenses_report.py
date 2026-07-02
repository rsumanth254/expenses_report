# This project builds a Personal Expense Tracker — that records daily expenses, saves them to a CSV file, and produces a clean summary report.
# Adds expense records — date, description, category, and amount
# Saves all records to a CSV file so data persists between runs
# Reads the CSV back and displays a formatted expenses table
# Shows a category-wise spending summary with totals
# Finds and displays the single highest expense

import csv
import os
from datetime import date
# 1 Create the csv file
FILENAME = "expenses.csv"


def setup_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME,mode='w',newline='')as file:
         writer = csv.writer(file)
         writer.writerow(['Date','Category','Description','Amount'])
        print (f"created new file : {FILENAME}")

# 2 add new expenses 

def add_expense (description,category,amount):
      # description (str) 
       # category    (str)
        #amount      (float)
    if amount<= 0:
        print("Amount must be greater than zero")
        return
    today = date.today().strftime("%d-%m-%y")
    with open (FILENAME,mode='a',newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([today,category,description,amount])
    print(f"Added:{description:<20} |  {category:<14} |  {amount:<7.2f} on {today}")
    
# 3 Read all expenses from file 

def load_expenses():
    expenses = []
    with open (FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader :
            row["Amount"] = float(row["Amount"])
            expenses.append(row)
    return expenses


# 4 Display all expenses and categories
def show_all_expenses(expenses):
    
    if not expenses:
        print("No expenses recorded yet.")
        return

    print()
    print("-" * 55)
    print(f"{'Date':<12} {'Description':<18} {'Category':<10} {'Amount':>8}")
    print("-" * 55)

    for expense in expenses:
        print(
            f"{expense['Date']:<12} "
            f"{expense['Description']:<18} "
            f"{expense['Category']:<10} "
            f"Rs.{expense['Amount']:>6.2f}"
        )

    print("-" * 55)

#5 show a summary by category

def show_summary(expenses):
    if not expenses :
        print ("No expenses to summerize")
        return
    category_totals = {}
    for expense in expenses :
        category = expense["Category"]
        amount = expense["Amount"]
        if category in category_totals:
            category_totals[category] += amount
        else :
            category_totals[category] = amount
    grand_total =sum(category_totals.values())

    print ()
    print (" Summary by category")
    print("-"*30)
    for category,total in category_totals.items():
         print(f"{category:<15} Rs.{total:>7.2f}")
    print ("-"*30)
    print(f"{'Total':<15} Rs.{grand_total:>7.2f}")
    print ()



# 6 Show the most expensive item

def show_highest_expense(expenses):
    if not expenses :
        return
    highest = expenses [0]
    for expense in expenses :
        if expense ["Amount"] > highest["Amount"]:
            highest = expense
    print(f"Highest expense :{highest['Description']} - Rs.{highest['Amount']:.2f}")


def main ():
    setup_file()

    add_expense("Groceries",         "Food",      850.00)
    add_expense("Bus pass",          "Travel",    500.00)
    add_expense("Electricity bill",  "Bills",     1200.00)
    add_expense("Lunch",             "Food",      180.00)
    add_expense("Notebook",          "Study",     120.00)
    add_expense("Auto ride",         "Travel",    90.00)
    add_expense("Internet bill",     "Bills",     699.00)
    add_expense("Coffee",            "Food",      60.00)
    
    expenses = load_expenses()


    print("\nAll Expenses")
    show_all_expenses(expenses)
    show_summary(expenses)
    show_highest_expense(expenses)

if __name__ =="__main__":
 main()
