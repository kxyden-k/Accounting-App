print("[Module] Journal loaded.")


def receive_income(amount):
    """formats and prints the amount entered into rands"""
    print("[Journal] Received R"+str(format(amount,".2f")))


def pay_expense(amount):
    """formats and prints the amount entered into rands"""
    print("[Journal] Paid R"+str(format(amount,".2f")))