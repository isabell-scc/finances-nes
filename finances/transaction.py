from datetime import datetime

CATEGORIES = {
    1: "Pagamento",
    2: "Depósito",
    3: "Transferência",
}

class Transaction:
    def __init__(self, amount: float, category: int, description: str = "") -> None:
        if category not in CATEGORIES.keys():
            raise ValueError("Categoria Inválida.")
        self.amount = amount
        self.date = datetime.now()
        self.category = category
        self.description = description