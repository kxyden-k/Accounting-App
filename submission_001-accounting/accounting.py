from user import authentication
from transactions import journal
import banking
import sys
import requests



if __name__ == "__main__":
    """ calls functions that were imported from other packages and modules"""
    a = sys.argv[1:]
    for x in range(len(a)): 
        print(a[x]),
    authentication.authenticate_user()
    journal.receive_income(100)
    journal.pay_expense(100)
    banking.do_reconciliation()
    
    #help("modules")