# display.py
# Functions that print menus, tables and summaries using plain ASCII borders

LINE_WIDTH = 60


def print_line(char="="):
    print(char * LINE_WIDTH)


def print_title(title):
    print()
    print_line("=")
    print(title.center(LINE_WIDTH))
    print_line("=")


def show_main_menu():
    print_title("PERSONAL EXPENSE & BUDGET TRACKER")
    print("  1. Add Expense")
    print("  2. Add Income")
    print("  3. View Summary")
    print("  4. Category Breakdown")
    print("  5. View All Transactions")
    print("  6. Delete Transaction")
    print("  7. Set Budget")
    print("  8. Export to CSV")
    print("  9. Save & Exit")
    print_line("-")


def show_transactions_table(transactions):
    if len(transactions) == 0:
        print("\nNo transactions to show.")
        return

    print()
    print_line("=")
    # header row
    print("{:<4} {:<11} {:<8} {:<13} {:>9}  {}".format(
        "ID", "Date", "Type", "Category", "Amount", "Description"))
    print_line("-")

    for t in transactions:
        # cut long descriptions so the table doesn't get messy
        desc = t.description
        if len(desc) > 18:
            desc = desc[:15] + "..."

        cat = t.category
        if len(cat) > 13:
            cat = cat[:10] + "..."

        print("{:<4} {:<11} {:<8} {:<13} {:>9.2f}  {}".format(
            t.id, t.date, t.trans_type, cat, t.amount, desc))

    print_line("=")
    print("Total transactions: " + str(len(transactions)))


def show_summary(total_income, total_spending, balance, period_label):
    print_title("SUMMARY (" + period_label + ")")
    print("  Total Income   : {:>12.2f}".format(total_income))
    print("  Total Spending : {:>12.2f}".format(total_spending))
    print_line("-")
    if balance >= 0:
        print("  Balance        : {:>12.2f}".format(balance))
    else:
        print("  Balance        : {:>12.2f}  (you are in the negative!)".format(balance))
    print_line("=")


def show_category_breakdown(cat_totals, percentages):
    print_title("CATEGORY BREAKDOWN")

    if len(cat_totals) == 0:
        print("  No expenses recorded yet.")
        print_line("=")
        return

    print("  {:<15} {:>10} {:>8}   {}".format("Category", "Spent", "Share", "Bar"))
    print_line("-")

    for cat in cat_totals:
        # draw a simple bar, 1 star for every 5 percent
        num_stars = int(percentages[cat] / 5)
        bar = "*" * num_stars

        name = cat
        if len(name) > 15:
            name = name[:12] + "..."

        print("  {:<15} {:>10.2f} {:>7.1f}%   {}".format(
            name, cat_totals[cat], percentages[cat], bar))

    print_line("=")


def show_budget_status(budget, cat_totals, total_spent):
    print_title("CURRENT BUDGET")

    if budget.total_limit > 0:
        remaining = budget.total_limit - total_spent
        print("  Overall limit  : {:>10.2f}".format(budget.total_limit))
        print("  Spent so far   : {:>10.2f}".format(total_spent))
        print("  Remaining      : {:>10.2f}".format(remaining))
    else:
        print("  No overall limit has been set.")

    print_line("-")

    if len(budget.category_limits) == 0:
        print("  No category budgets set.")
    else:
        print("  {:<15} {:>10} {:>10}".format("Category", "Limit", "Spent"))
        for cat in budget.category_limits:
            spent = 0.0
            if cat in cat_totals:
                spent = cat_totals[cat]
            print("  {:<15} {:>10.2f} {:>10.2f}".format(cat, budget.category_limits[cat], spent))

    print_line("=")


def show_warnings(warnings):
    if len(warnings) == 0:
        return

    print()
    print_line("!")
    for w in warnings:
        print("  " + w)
    print_line("!")


def show_message(message):
    print("\n>> " + message)
