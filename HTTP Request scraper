
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

search = input('Download images of: ')
counter = 0

number_of_images = int(input("Please enter the number of images you wish to download: "))




params = {"q": search}  ## get variable of q
r = requests.get("https://www.bing.com/images/search", params=params, verify= False)

soup = BeautifulSoup(r.text,"html.parser")  ## default but sometimes we need the parameters because it might show a warning message
##print(soup.prettify())

links = soup.findAll("a", {"class": "thumb"})


for item in links:
    if counter < number_of_images:
        img_obj = requests.get(item.attrs["href"],verify= False)
        print('Getting:',item.attrs["href"])
        title = item.attrs["href"].split("/")[-1]
        try:

            img = Image.open(BytesIO(img_obj.content))
            img.save("./images/" + title, img.format)
            counter+=1
            print(counter)

        except OSError:
            print('Error')

            continue
print("Done, Found", counter, "relevant items.")
