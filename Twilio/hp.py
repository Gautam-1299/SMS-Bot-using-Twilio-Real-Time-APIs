import urllib.request
import json 
import random 


def get_char():
  url='https://hp-api.onrender.com/api/characters'

  request = urllib.request.urlopen(url)
  result = json.loads(request.read())


  #print(result)
  char = random.randint(1,40)

  if result[char]["wizard"] == True:
    return f"Your random Harry Potter Character is {result[char]['name']} played by actor {result[char]['actor']}, and is in the house {result[char]['house']}; image{result[char]['image']}"
  else:
    return f"Your random Harry Potter character {result[char]['name']} is not in house wizard and it is played by actor {result[char]['actor']}, image{result[char]['image']}"