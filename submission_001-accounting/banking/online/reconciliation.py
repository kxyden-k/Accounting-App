import requests

print("[Module] online.Reconciliation loaded.")


def do_reconciliation():
    """prints doing online bank reconciliation and uses the requests module to get the request from wethinkcode's website"""
    print("Doing Online Bank reconciliation.")
    x = requests.get('https://www.wethinkcode.co.za')
    print(x.status_code)