from database.db import get_connection
from models.card import Card
import bcrypt
def get_card_by_number(card_number):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute(
        "SELECT * FROM  cards WHERE card_number=?",
        (card_number,))

    card=cursor.fetchone()
    con.close()
    return card

def authenticate(card_number, pin):
    card=get_card_by_number(card_number)


    if card is None:
        return None
    if card["is_blocked"]:
        return  None

    if not bcrypt.checkpw(pin.encode('utf-8'), card["pin"]):
        return None

    return card
