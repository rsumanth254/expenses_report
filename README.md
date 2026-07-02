# Personal Expense Tracker

A beginner Python project that records, saves, and summarises personal expenses using CSV files.


---

## What This Project Does

- Adds expense records with date, description, category, and amount
- Saves all records to a CSV file so data is not lost when the program closes
- Displays all expenses in a formatted table
- Shows a category-wise spending summary
- Finds the highest expense

---

## Concepts Used

- Functions and docstrings
- File handling with CSV
- Dictionaries and loops
- The `datetime` module
- `os` module for file checks

---

## How to Run

**Step 1 — Make sure Python is installed**
```
python --version
```

**Step 2 — Clone or download this repository**
```
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

**Step 3 — Run the script**
```
python expense_tracker.py
```

**Step 4 — View the output**

The program will print a table of expenses, a category summary, and the highest expense. It will also create an `expenses.csv` file in the same folder.

---

## Project Structure

```
expense-tracker/
│
├── expense_tracker.py   # Main Python script
├── expenses.csv         # Auto-generated when you run the script
└── README.md            # This file
```

---

## Sample Output

```
Added:Groceries            |  Food           |  850.00  on 02-07-26
Added:Bus pass             |  Travel         |  500.00  on 02-07-26
Added:Electricity bill     |  Bills          |  1200.00 on 02-07-26
Added:Lunch                |  Food           |  180.00  on 02-07-26
Added:Notebook             |  Study          |  120.00  on 02-07-26
Added:Auto ride            |  Travel         |  90.00   on 02-07-26
Added:Internet bill        |  Bills          |  699.00  on 02-07-26
Added:Coffee               |  Food           |  60.00   on 02-07-26
...

All Expenses

-------------------------------------------------------
Date         Description        Category     Amount
-------------------------------------------------------
02-07-26     Groceries          Food       Rs.850.00
02-07-26     Bus pass           Travel     Rs.500.00
02-07-26     Electricity bill   Bills      Rs.1200.00
02-07-26     Lunch              Food       Rs.180.00
02-07-26     Notebook           Study      Rs.120.00
02-07-26     Auto ride          Travel     Rs. 90.00
02-07-26     Internet bill      Bills      Rs.699.00
02-07-26     Coffee             Food       Rs. 60.00
-------------------------------------------------------

Summary by category
------------------------------
Food            Rs.1090.00
Travel          Rs. 590.00
Bills           Rs.1899.00
Study           Rs. 120.00
------------------------------
Total           Rs.3699.00

Highest expense: Electricity bill — Rs.1200.00
```

---

## Customising

Open `expense_tracker.py` and edit the `main()` function to add your own expenses:

```python
add_expense("Your item", "Category", amount)
```

Valid categories: Food, Travel, Bills, Study, Other — or create your own.

---

Sumanth Rajavarapu

