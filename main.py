import requests

class Person:
  def __init__(self):
    r = requests.get("https://randomuser.me/api/")
    res = r.json()
    print(res["result"])