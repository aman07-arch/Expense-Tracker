# main.py
# Entry point for the Personal Expense & Budget Tracker
# Run with: python main.py

import storage
import budget_manager
import helpers
import display


def add_expense_flow(transactions, budget):
    display.print_title("ADD EXPENSE")
    date = helpers.get_valid_date("Date (YYYY-MM-DD, press enter for today): ")
    category = helpers.get_non_empty_string("Category (e.g. Food, Transport): ")
    amount = helpers.get_positive_float("Amount: ")
    description = helpers.get_non_empty_string("Description: ")

    # store categories in Title Case so "food" and "Food" are the same
    category = category.title()

    new_trans = budget_manager.add_transaction(transactions, date, category, amount, description, "expense")
    display.show_message("Expense added with ID " + str(new_trans.id))

    # check if this expense pushed the user over a budget limit
    warnings = budget_manager.check_budget(transactions, budget)
    display.show_warnings(warnings)


def add_income_flow(transactions):
    display.print_title("ADD INCOME")
    date = helpers.get_valid_date("Date (YYYY-MM-DD, press enter for today): ")
    category = helpers.get_non_empty_string("Source (e.g. Salary, Freelance): ")
    amount = helpers.get_positive_float("Amount: ")
    description = helpers.get_non_empty_string("Description: ")

    category = category.title()

    new_trans = budget_manager.add_transaction(transactions, date, category, amount, description, "income")
    display.show_message("Income added with ID " + str(new_trans.id))


def view_summary_flow(transactions, budget):
    month = helpers.get_month_string("Month to view (YYYY-MM), or press enter for all time: ")
    period_transactions = budget_manager.filter_by_month(transactions, month)

    if month == "":
        period_label = "All Time"
    else:
        period_label = month

    total_income = budget_manager.get_total_income(period_transactions)
    total_spending = budget_manager.get_total_spending(period_transactions)
    balance = budget_manager.get_balance(period_transactions)

    display.show_summary(total_income, total_spending, balance, period_label)

    # also show budget warnings under the summary
    warnings = budget_manager.check_budget(period_transactions, budget)
    display.show_warnings(warnings)


def category_breakdown_flow(transactions):
    month = helpers.get_month_string("Month to view (YYYY-MM), or press enter for all time: ")
    period_transactions = budget_manager.filter_by_month(transactions, month)

    cat_totals = budget_manager.get_category_totals(period_transactions)
    percentages = budget_manager.get_category_percentages(cat_totals)

    display.show_category_breakdown(cat_totals, percentages)

    top_cat = budget_manager.get_top_category(cat_totals)
    if top_cat is not None:
        print("  Highest spending category: " + top_cat)


def delete_flow(transactions):
    if len(transactions) == 0:
        display.show_message("There are no transactions to delete.")
        return

    display.show_transactions_table(transactions)
    trans_id = helpers.get_menu_choice("Enter the ID to delete (0 to cancel): ", 0, 999999)

    if trans_id == 0:
        display.show_message("Delete cancelled.")
        return

    sure = helpers.get_yes_no("Are you sure you want to delete transaction " + str(trans_id) + "? (y/n): ")
    if sure:
        deleted = budget_manager.delete_transaction(transactions, trans_id)
        if deleted:
            display.show_message("Transaction deleted.")
        else:
            display.show_message("No transaction found with that ID.")
    else:
        display.show_message("Delete cancelled.")


def set_budget_flow(transactions, budget):
    # show what is currently set first
    cat_totals = budget_manager.get_category_totals(transactions)
    total_spent = budget_manager.get_total_spending(transactions)
    display.show_budget_status(budget, cat_totals, total_spent)

    print("  1. Set overall spending limit")
    print("  2. Set a category budget")
    print("  3. Back to main menu")
    choice = helpers.get_menu_choice("Choose an option: ", 1, 3)

    if choice == 1:
        amount = helpers.get_positive_float("New overall limit: ")
        budget.set_total_limit(amount)
        display.show_message("Overall limit set to " + str(amount))
    elif choice == 2:
        category = helpers.get_non_empty_string("Category name: ").title()
        amount = helpers.get_positive_float("Budget for " + category + ": ")
        budget.set_category_limit(category, amount)
        display.show_message("Budget for " + category + " set to " + str(amount))
    else:
        return


def export_flow(transactions):
    if len(transactions) == 0:
        display.show_message("Nothing to export yet.")
        return

    success = storage.export_to_csv(transactions)
    if success:
        display.show_message("Exported " + str(len(transactions)) + " transactions to expenses_export.csv")


def run_menu(transactions, budget):
    # the main menu loop, runs until the user picks Save & Exit
    while True:
        display.show_main_menu()

        try:
            user_choice = int(input("Enter your choice (1-9): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        if user_choice == 1:
            add_expense_flow(transactions, budget)
            storage.save_data(transactions, budget)
        elif user_choice == 2:
            add_income_flow(transactions)
            storage.save_data(transactions, budget)
        elif user_choice == 3:
            view_summary_flow(transactions, budget)
        elif user_choice == 4:
            category_breakdown_flow(transactions)
        elif user_choice == 5:
            display.show_transactions_table(transactions)
        elif user_choice == 6:
            delete_flow(transactions)
            storage.save_data(transactions, budget)
        elif user_choice == 7:
            set_budget_flow(transactions, budget)
            storage.save_data(transactions, budget)
        elif user_choice == 8:
            export_flow(transactions)
        elif user_choice == 9:
            storage.save_data(transactions, budget)
            print("\nData saved. Goodbye!")
            break
        else:
            print("Please choose a number between 1 and 9.")


def main():
    # load saved data (or start fresh if there is none)
    transactions, budget = storage.load_data()
    print("Welcome! Loaded " + str(len(transactions)) + " saved transactions.")

    try:
        run_menu(transactions, budget)
    except (KeyboardInterrupt, EOFError):
        # user pressed Ctrl+C or Ctrl+D, save what we have and quit nicely
        print("\n\nProgram interrupted. Saving your data...")
        storage.save_data(transactions, budget)
        print("Data saved. Goodbye!")


if __name__ == "__main__":
    main()
