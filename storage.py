import json
import os

from models import Transaction, Budget
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "expenses.json")

def save_expenses(expenses):
  # 1. Create parent folders if they don't exist
  folder = os.path.dirname(DATA_FILE)
  if folder:
    os.makedirs(folder, exist_ok=True)

  # 2. Write/create expenses.json
  with open(DATA_FILE, "w") as f:
    json.dump(expenses, f, indent=4)

def load_data():
    transactions = []
    budget = Budget()

    if not os.path.exists(DATA_FILE):
        return transactions, budget

    try:
        file = open(DATA_FILE, "r")
        raw_data = json.load(file)
        file.close()
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read " + DATA_FILE + ". Starting with empty data.")
        return transactions, budget

    for item in raw_data.get("transactions", []):
        try:
            transactions.append(Transaction.from_dict(item))
        except KeyError:
            print("Warning: skipped a broken transaction entry.")

    budget = Budget.from_dict(raw_data.get("budget", {}))

    return transactions, budget


def save_data(transactions, budget):
    trans_list = []
    for t in transactions:
        trans_list.append(t.to_dict())

    all_data = {
        "transactions": trans_list,
        "budget": budget.to_dict()
    }

    try:
        file = open(DATA_FILE, "w")
        json.dump(all_data, file, indent=4)
        file.close()
        return True
    except OSError:
        print("Error: could not save data to " + DATA_FILE)
        return False


def export_to_csv(transactions, filename="expenses_export.csv"):
    try:
        file = open(filename, "w")
        file.write("id,date,type,category,amount,description\n")
        for t in transactions:
            clean_desc = t.description.replace(",", " ")
            line = (str(t.id) + "," + t.date + "," + t.trans_type + "," +
                    t.category + "," + str(t.amount) + "," + clean_desc + "\n")
            file.write(line)
        file.close()
        return True
    except OSError:
        print("Error: could not write " + filename)
        return False
