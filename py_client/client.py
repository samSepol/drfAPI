import requests 
import json 

URL = "http://127.0.0.1:8000/codersapi/"

def get_coder(id=None):
    data={}
    if id is not None:
        data={'id':id}
        # convert data into json
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

# get_coder()

def post_coder():
    data={
        'name':'paul allen',
        'domain':'Basic',
        'company':'Microsoft',
        'salary':90000000
    }

    # convert data into json

    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

# post_coder()


# update coder 

def update_coder():
    data={
        'id':13,
        'company':'Microsoft'
        
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

# update_coder()

def delete_coder():
    data={
        'id':8,
        }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

delete_coder()

