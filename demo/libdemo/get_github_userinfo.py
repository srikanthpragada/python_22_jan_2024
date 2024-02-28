import requests

username = input("Enter username :")
resp = requests.get(f"https://api.github.com/users/{username}")
if resp.status_code == 404: # username not found
    print("Username not found!")
    exit()

details = resp.json()

print(f"Name        : {details['name']}")
print(f"Company     : {details['company']}")
print(f"Repos Count : {details['public_repos']}")

