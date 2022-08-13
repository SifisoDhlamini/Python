import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
while True:
    try:
        response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        sys.exit("Error making request")
    else:
        try:
            multiple = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            price = float(response["bpi"]["USD"]["rate_float"])
            amount = price * multiple
            print(f"${amount:,.4f}")
            break



