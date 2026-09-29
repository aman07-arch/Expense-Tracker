from models import Transaction


def get_next_id(transactions):
    highest = 0
    for t in transactions:
        if t.id > highest:
            highest = t.id
    return highest + 1


def add_transaction(transactions, date, category, amount, description, trans_type="expense"):
    new_id = get_next_id(transactions)
    new_trans = Transaction(new_id, date, category, amount, description, trans_type)
    transactions.append(new_trans)
    return new_trans


def delete_transaction(transactions, trans_id):
    for t in transactions:
        if t.id == trans_id:
            transactions.remove(t)
            return True
    return False


def filter_by_month(transactions, month):
    if month == "":
        return transactions

    filtered = []
    for t in transactions:
        if t.date[:7] == month:
            filtered.append(t)
    return filtered


def get_total_spending(transactions):
    total = 0.0
    for t in transactions:
        if t.trans_type == "expense":
            total += t.amount
    return round(total, 2)


def get_total_income(transactions):
    total = 0.0
    for t in transactions:
        if t.trans_type == "income":
            total += t.amount
    return round(total, 2)


def get_balance(transactions):
    return round(get_total_income(transactions) - get_total_spending(transactions), 2)


def get_category_totals(transactions):
    cat_totals = {}
    for t in transactions:
        if t.trans_type == "expense":
            if t.category in cat_totals:
                cat_totals[t.category] += t.amount
            else:
                cat_totals[t.category] = t.amount

    for cat in cat_totals:
        cat_totals[cat] = round(cat_totals[cat], 2)

    return cat_totals


def get_category_percentages(cat_totals):
    total = 0.0
    for cat in cat_totals:
        total += cat_totals[cat]

    percentages = {}
    for cat in cat_totals:
        if total > 0:
            percentages[cat] = round((cat_totals[cat] / total) * 100, 1)
        else:
            percentages[cat] = 0.0
    return percentages


def get_top_category(cat_totals):
    top_cat = None
    top_amount = 0.0
    for cat in cat_totals:
        if cat_totals[cat] > top_amount:
            top_amount = cat_totals[cat]
            top_cat = cat
    return top_cat


def search_by_category(transactions, category):
    results = []
    for t in transactions:
        if t.category.lower() == category.lower():
            results.append(t)
    return results


def check_budget(transactions, budget):
    warnings = []
    total_spent = get_total_spending(transactions)
    cat_totals = get_category_totals(transactions)

    if budget.total_limit > 0:
        used_percent = (total_spent / budget.total_limit) * 100
        if total_spent > budget.total_limit:
            over_by = round(total_spent - budget.total_limit, 2)
            warnings.append("OVER BUDGET: total spending exceeds the limit by " + str(over_by))
        elif used_percent >= 80:
            warnings.append("WARNING: you have used " + str(round(used_percent, 1)) + "% of your total budget")

    for cat in budget.category_limits:
        limit = budget.category_limits[cat]
        if limit <= 0:
            continue

        spent = 0.0
        if cat in cat_totals:
            spent = cat_totals[cat]

        cat_percent = (spent / limit) * 100
        if spent > limit:
            over_by = round(spent - limit, 2)
            warnings.append("OVER BUDGET in " + cat + " by " + str(over_by))
        elif cat_percent >= 80:
            warnings.append("WARNING: " + cat + " is at " + str(round(cat_percent, 1)) + "% of its budget")

    return warnings
