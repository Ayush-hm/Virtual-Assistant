from googlesearch import search

query = "what is a computer"

for result in search(query, num=20, stop=10):
    print(result)