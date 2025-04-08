# Faire des requêtes HTTP

# Ce programme semble fonctionner, et est validé par Hackinscience
# Toutefois, je ne suis pas convaincu par le résultat.

import requests

try:
    r = requests.get('https://api.github.com/users/python')
    print(r.text)
except:
    print("No internet connectivity.")