import requests

from colorama import Fore

class Person:
  
  def __init__(self):
    r = requests.get("https://randomuser.me/api/")
    res = r.json()
    self.name = res["results"][0]["name"]["first"]
    self.surname = res["results"][0]["name"]["last"]
    self.age = res["results"][0]["dob"]["age"]
    self.isMale = res["results"][0]["gender"] == "male"
    


random_person = Person()
if random_person.isMale:
  print(Fore.CYAN)
else:
  print(Fore.MAGENTA)
print(random_person.name)
print(random_person.surname)
print(random_person.age)
print(random_person.isMale)
person2 = Person()