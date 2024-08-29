
def calculate_expenses(file):
    with open(file, 'r') as f:
        next(f)
        next(f)
        expense = 0
        for i in f:
            amt = i.split()
            expense += float(amt[2])
        return expense
    
total_expenses = calculate_expenses('expenses.txt')

print(f'Total Expenses is {total_expenses}')