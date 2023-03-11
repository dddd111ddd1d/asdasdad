import requests

class Person:
  def __init__(self):
    r = requests.get("https://randomuser.me/api/")
    res = r.json()
    self.name = res["results"][0]["name"]["first"]
    self.surname = res["results"][0]["name"]["last"]
    self.age = res["results"][0]["dob"]["age"]

random_person = Person()
print(random_person.name)
print(random_person.surname)