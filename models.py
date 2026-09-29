class Transaction:
    def __init__(self, trans_id, date, category, amount, description, trans_type="expense"):
        self.id = trans_id
        self.date = date                  # stored as YYYY-MM-DD string
        self.category = category
        self.amount = amount              # always a positive float
        self.description = description
        self.trans_type = trans_type      # "expense" or "income"

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
            "type": self.trans_type
        }

    @staticmethod
    def from_dict(data):
        trans_type = data.get("type", "expense")
        return Transaction(
            data["id"],
            data["date"],
            data["category"],
            data["amount"],
            data["description"],
            trans_type
        )

    def __str__(self):
        return "[" + str(self.id) + "] " + self.date + " | " + self.category + " | " + str(self.amount)


class Budget:
    def __init__(self, total_limit=0.0, category_limits=None):
        self.total_limit = total_limit
        if category_limits is None:
            self.category_limits = {}
        else:
            self.category_limits = category_limits

    def set_total_limit(self, amount):
        self.total_limit = amount

    def set_category_limit(self, category, amount):
        self.category_limits[category] = amount

    def get_category_limit(self, category):
        if category in self.category_limits:
            return self.category_limits[category]
        return 0.0

    def to_dict(self):
        return {
            "total_limit": self.total_limit,
            "category_limits": self.category_limits
        }
    @staticmethod
    def from_dict(data):
        total_limit = data.get("total_limit", 0.0)
        category_limits = data.get("category_limits", {})
        return Budget(total_limit, category_limits)
