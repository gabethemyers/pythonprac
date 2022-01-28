import requests

# for api_key
import config

# this section gets me json of valid currencies and some attributes about them
url = f'https://free.currconv.com/api/v7/currencies?apiKey={config.api_key}'

r = requests.get(url)
package_json = r.json()
    
data = package_json['results']
valid_currencies = data.keys()

# logic for inputs, checking if they want the list of currencies and if it is in the list of currencies
while True:
    first = input('Enter Currency ID to convert from, if you would like a list of valid IDs enter "curr_ids": ')
    if first == 'curr_ids':
        print('ID', ' Name')
        for i in valid_currencies:
            print(i, data[i]["currencyName"])
    if first.upper() in valid_currencies:
        break
while True:
    second = input('Enter Currency ID to convert to: ')
    if second.upper() in valid_currencies:
        break

# gets amount to convert and makes sure its a number
while True:
    try:
        amount = int(input("Enter amount to convert: "))
    except ValueError:
        print('Sorry, that is not a number')
    else:
        break

# this requests the conversion rate between two given currencies in json format
conversion_url = f"https://free.currconv.com/api/v7/convert?q={first.upper()}_{second.upper()}&compact=ultra&apiKey={config.api_key}"
r = requests.get(conversion_url)
conversion = r.json()

# getting symbol for the currency we are converting to. Some dont have one so used try except block
symbol = ''
try:
    symbol = data[second.upper()]['currencySymbol']
except:
    pass
    
# final result is concatinated and printed 
conversion = list(conversion.values())
print("Your converted amount is: " + symbol + str(conversion[0] * amount))




