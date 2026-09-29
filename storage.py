# storage.py
# Handles saving and loading data from expenses.json

import json
import os

from models import Transaction, Budget

DATA_FILE = "expenses.json"


def load_data():
    # load saved JSON data or initialize empty list if file doesn't exist
    transactions = []
    budget = Budget()

    if not os.path.exists(DATA_FILE):
        return transactions, budget

    try:
        file = open(DATA_FILE, "r")
        raw_data = json.load(file)
        file.close()
    except (json.JSONDecodeError, OSError):
        # file is empty, corrupted, or can't be read
        print("Warning: could not read " + DATA_FILE + ". Starting with empty data.")
        return transactions, budget

    # rebuild the transaction objects
    for item in raw_data.get("transactions", []):
        try:
            transactions.append(Transaction.from_dict(item))
        except KeyError:
            # skip any broken entries instead of crashing
            print("Warning: skipped a broken transaction entry.")

    budget = Budget.from_dict(raw_data.get("budget", {}))

    return transactions, budget


def save_data(transactions, budget):
    # convert everything to dictionaries first, then write to file
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
    # extra feature: export all transactions to a csv file
    try:
        file = open(filename, "w")
        file.write("id,date,type,category,amount,description\n")
        for t in transactions:
            # remove commas from description so the csv doesn't break
            clean_desc = t.description.replace(",", " ")
            line = (str(t.id) + "," + t.date + "," + t.trans_type + "," +
                    t.category + "," + str(t.amount) + "," + clean_desc + "\n")
            file.write(line)
        file.close()
        return True
    except OSError:
        print("Error: could not write " + filename)
        return False
