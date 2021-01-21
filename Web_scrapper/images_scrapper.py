from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def startSearch():
    # url = 'https://www.bing.com/images/search?q=pizza&first=1&tsc=ImageBasicHover'
    url = 'https://www.bing.com/images/search'

    search = input("Search For :")
    params = {"q":search}

    dir_name = search.replace(" ","_").lower()
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    data  = requests.get(url,params=params)

    soup = BeautifulSoup(data.text,features="html.parser")

    links = soup.findAll("a",{"class":"thumb"})


    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting",item.attrs["href"])
            # #img obj 406 not acceptable phyit yin continue
            # if img_obj.status_code == 406:
            #     continue
            #get title
            title = item.attrs["href"].split("/")[-1]
            #try except for image could not save
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./"+ dir_name +"/" + title , img.format)
            except:
                print("Image Could not save")
        except:
            print("Could not make requests")
    
    
    startSearch()
    
startSearch()

        
        
 
# sample = r'''
#             <html>
#             <body>
#             <p>
#             }"
#             </p>
#             <div class='\"message-container\"' id='\"m154862032\"'>
#             '''
# soup  = BeautifulSoup(sample,features="html.parser")
# result = soup.findAll('div',class_=r'\"message-container\"')
# print(result)