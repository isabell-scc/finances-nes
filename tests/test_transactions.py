from finances import Transaction
from finances.transaction import CATEGORIES
from datetime import datetime

DEFAULT_AMOUNT = 100.0
DEFAULT_CATEGORY = 1
DEFAULT_DESCRIPTION = "Transação de teste"
def get_transaction():
    return Transaction(DEFAULT_AMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)

def test_transaction_instance():
    """Testa instanciação de transações"""
    tr = get_transaction()
    assert isinstance(tr, Transaction), "Falha ao instanciar um objeto Transaction"

def test_transaction_cat():
    "Testa se as categorias são válidas"
    tr = get_transaction()
    assert tr.category in CATEGORIES.keys()

def test_transaction_atributes():
    """Testa os tipo e valores dos atributos"""
    tr = get_transaction()
    #checa os tipos
    assert type(tr.amount) is float
    assert type(tr.date) is datetime
    assert type(tr.category) is int
    assert type(tr.description) is str
    #Checa os valores
    assert tr.amount == DEFAULT_AMOUNT
    assert tr.category == DEFAULT_CATEGORY
    assert tr.description == DEFAULT_DESCRIPTION

