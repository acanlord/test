import requests
import json

dog_pic = [] 
   

def dogs():
    response = requests.get("https://random.dog/woof.json")
    #print(response.status_code)
    print(response.json())


def read_files():
	for d in dogs:
	dog_pic.append({"url": url})
	print(doc_pic)

dogs()
read_files()





# {'fileSizeBytes': 45090516, 'url': 'https://random.dog/3254832e-ace1-414c-9d66-e4d968f2928f.gif'}

#https://www.dataquest.io/blog/python-api-tutorial/
