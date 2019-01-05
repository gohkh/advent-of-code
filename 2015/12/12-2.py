import json

with open("12.txt", 'r') as f:
    document = f.readlines()[0]

document = json.loads(document)

def json_sum(document):
    if type(document) == int:
        return document
    elif type(document) == str:
        return 0
    elif type(document) == dict:
        document = list(document.items())
        for pair in document:
            if "red" in pair:
                return 0

    if type(document) == list or type(document) == tuple:
        return sum(json_sum(thing) for thing in document)

print(json_sum(document))
