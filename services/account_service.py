

from  database.db import get_connection
from models.account import Account
from models.transaction import Transaction, TransactionType

def get_account_by_card_id(card_id):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("SELECT * FROM accounts WHERE card_id=?",
                   (card_id,))
    account=cursor.fetchone()
    con.close()
    return account




def get_balance(card_id):
    accounts=get_account_by_card_id(card_id)
    if accounts is None:
        return None
    return accounts["balance"]




def withdraw(card_id, amount):
    account=get_account_by_card_id(card_id)
    if account is None:
        return None
    if account["balance"]<amount:
        return  None
    new_balance=account["balance"]-amount
    con=get_connection()
    cursor=con.cursor()
    cursor.execute(
       "UPDATE accounts SET balance=? WHERE card_id=?",
        (new_balance,card_id)
    )
    con.commit()
    con.close()
    return new_balance

def deposit(card_id,amount):
     account=get_account_by_card_id(card_id)
     if account is None:
         return None
     if amount<0:
         return None
     new_balance=account["balance"]+amount
     con=get_connection()
     cursor=con.cursor()
     cursor.execute(
         "UPDATE accounts SET balance=? WHERE card_id=?",
         (new_balance,card_id)
     )
     con.commit()
     con.close()
     return new_balance

