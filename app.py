import requests
import urllib.request
from bs4 import BeautifulSoup
import json
from PIL import Image


def main():
    username = input("Enter username: ")
    url      = f'https://www.instagram.com/{username}/' 

    try:
        page     = requests.get(url)
        soup     = BeautifulSoup(page.content, 'html.parser')

        scripts  = soup.find_all("script", type = "text/javascript")

        script = scripts[3].get_text()

        new_string = script[21:-1]

        json_text = json.loads(new_string)

        url  = json_text['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd'] 
        name = json_text['entry_data']['ProfilePage'][0]['graphql']['user']['full_name'] 

        r = requests.get(url)

        with open(f'images/{name}.jpg', 'wb') as f:
            f.write(r.content)
    except:
        print("Error")

if __name__ == "__main__":
    main()