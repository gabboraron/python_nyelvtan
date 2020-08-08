import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    closematches = get_close_matches(word,data.keys())
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(closematches) > 0 :
        print("Did you mean %s instead"%closematches[0])
        decide = input("press y/n\t")
        if decide == "y":
            return data[closematches[0]]
    else:
        print("ERROR: Not in dictionary")

print()
word = input("Search term: ")
try:
    output = translate(word)
    if type(output) == list:
        for idx in output:
            print("\t+\t"+str(idx))
    else:
        print(output)
    print("")
except Exception as e:
    raise
