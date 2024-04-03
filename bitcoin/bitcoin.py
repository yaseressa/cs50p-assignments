import sys
import requests
if len(sys.argv) < 2:
    sys.exit('Missing command-line argument')
else:
    try:
        coin = float(sys.argv[1])
        rate = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate']
        print(f'${(coin * float(rate.replace(',', ''))):,.4f}')
    except ValueError:
        sys.exit('Command-line argument is not a number')
