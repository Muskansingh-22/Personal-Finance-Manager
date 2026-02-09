1.menu.py 
- Creates and displays menu items
- Handles user choices
- Routes user actions to appropriate functions

2. file_manager.py
- Handles CSV file operations
- Functions include:
    Read expenses from CSV
    Write expenses to CSV
    Append new records
- Uses Python's built-in csv module

3. expense.py 
- Core logic for managing expenses
- Functions include:
    Add expense
    Read and display expenses
    Search expenses
    Generate summary data
- Uses Expense attributes:
    Amount
    Category
    Date
    Description

4. reports.py
- Generates analytical reports
- Calculates:
    Total expenses
    Average expenses
    Category-wise totals

5. utils.py 
- Utility functions
- Handles:
    Backup of CSV data
    Restore from backup
