import json

def load_data(d):
    with open(d) as t:
        data = json.load(t)
    return data


def save_data(w,d):
    with open(d,'w') as t:
        json.dump(w,t,indent=4)


