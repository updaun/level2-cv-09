import requests
import json

def clean_data():
  r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
  response = json.loads(r.text)

  rm_list = list()
  for k, v in response.items():
    if k in ['name', 'education']:
      for kk, vv in v.items():
        if vv in ['', '-', 'N/A']:
          rm_list.append([k, kk])

    if k in ['age', "DOB"]:
      if v in ['', '-', 'N/A']:
        rm_list.append([k])
    
    if k in ['hobbies']:
      temp = list()
      for x in v:
        if x not in ['', '-', 'N/A']:
          temp.append(x)
      if temp:
        response[k] = temp
      else:
        rm_list.append([k])
  
  for rm in rm_list:
    if len(rm) == 2:
      del(response[rm[0]][rm[1]])
    else:
      del(response[rm[0]])

  return response

print(clean_data())