from fastapi import FastAPI
from services.auth_service import authenticate
from services.account_service import get_balance, withdraw, deposit
app=FastAPI()
@app.post("/auth/login")
def login(card_number: str, pin: str):
    card = authenticate(card_number, pin)
    if card is None:
        return {"status": "error", "message": "Login failed"}
    return {"status": "success", "card": card}
@app.get("/account/balance")
def balance(card_id: str):
    result = get_balance(card_id)
    if result is None:
        return {"status": "error", "message": "Account not found"}
    return {"status": "success", "balance": result}
@app.post("/account/withdraw")
def withdraw_money(card_id: str, amount: float):
    result = withdraw(card_id, amount)
    if result is None:
        return {"status": "error", "message": "Withdrawal failed"}
    return {"status": "success", "new_balance": result}
@app.post("/account/deposit")
def deposit_money(card_id: str, amount: float):
    result = deposit(card_id, amount)
    if result is None:
        return {"status": "error", "message": "Deposit failed"}
    return {"status": "success", "new_balance": result}
