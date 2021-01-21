from bs4 import BeautifulSoup
import requests
# search = input("Enter search term: ")
# params = {"q":search}

#import pdb;pdb.set_trace()
ro = requests.get("https://www.google.com/search?q=pizza")

# print(r.text)

#print(r.text)

soup = BeautifulSoup(ro.text,features="html.parser")
results = soup.find("div",attrs={"class":"yuRUbf"})
# links = soup.findAll("li",{"class":"b_algo"})
# print(links)
print(results)

# print(soup.prettify())