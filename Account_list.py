# import account_data.json
# list the accounts in the json file
# and print the account_type, normal_balance, account_balance

import json

with open('account_data.json') as f:
    data = json.load(f)

# Support both {"accounts": [...]} and [...] JSON structures.
if isinstance(data, dict):
    accounts = data.get('accounts', [])
elif isinstance(data, list):
    accounts = data
else:
    accounts = []

for account in accounts:
    print("Name:", account.get('name', account.get('account_name', 'Unknown')))
    print("Account Type:", account.get('account_type', 'Unknown'))
    print("Normal Balance:", account.get('normal_balance', 'Unknown'))
    print("Account Balance:", account.get('account_balance', account.get('balance', 'Unknown')))
    print()
    