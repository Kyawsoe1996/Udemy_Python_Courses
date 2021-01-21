import requests
'''
#Part 1
r = requests.get("https://www.google.com/")
print("Status :",r.status_code)
print(r.url)
# print(r.text)

f = open("./page.html","w+")
f.write(r.text)

'''

params = {"q":"pizza"}
r = requests.get("https://www.google.com/search",params=params)
print(r.url)
print(r.headers)

f= open("./page.html","w+")
f.write(r.text)
