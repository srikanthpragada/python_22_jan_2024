import requests

code = input("Enter country code :")
resp = requests.get(f"https://restcountries.com/v3.1/alpha/{code}")

if resp.status_code != 200:  # success
    print("Sorry! Could not get details of country with code", code)
    exit()

details = resp.json()[0]  # first element from list of dict

print(f"Name       : {details['name']['common']}")
print(f"Capital    : {details['capital'][0]}")
print(f"Region     : {details['region']}")
print(f"Area       : {details['area']}")
print(f"Population : {details['population']}")
