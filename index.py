import requests
from bs4 import BeautifulSoup
import os

baseurl = input("Enter Your Url:")  

def download_resource(url, local_dir):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(local_dir), exist_ok=True) 
            with open(local_dir, 'wb') as file:
                file.write(response.content)
    except Exception as e:
        print(f"Error while downloading {url}: {e}")

print("Connecting to server")
response = requests.get(baseurl)

if response.status_code == 200:
    html_doc = response.text
    print("Connection Success!")

    try:
        soup = BeautifulSoup(html_doc, 'html.parser')
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print("Initializing Index File")

        # Initialize variables for resources
        img_list = soup.find_all('img')
        css_list = soup.find_all('link', rel='stylesheet')
        js_list = soup.find_all('script', src=True)

        # Get All Images
        print("Process Initiated")
        print("Step 1: Getting all images.")
        for img in img_list:
            img_url = img.get('src')
            if not img_url.startswith(('http', 'https')):
                local_dir = os.path.join('images', os.path.basename(img_url))
                download_resource(baseurl + img_url, local_dir)

        print('============== Done getting images! ==============')

        # Get all CSS
        print("Step 2: Getting all CSS.")
        for css in css_list:
            css_url = css.get('href')
            if not css_url.startswith(('http', 'https')):
                local_dir = os.path.join('css', os.path.basename(css_url))
                download_resource(baseurl + css_url, local_dir)

        print('============== Done getting CSS files! ==============')

        # Get all JS
        print("Step 3: Getting all JS.")
        for script in js_list:
            js_url = script.get('src')
            if not js_url.startswith(('http', 'https')):
                local_dir = os.path.join('js', os.path.basename(js_url))
                download_resource(baseurl + js_url, local_dir)

        print('============== Done getting JS files! ==============')
        print('Script Executed successfully!')

    except Exception as e:
        print("Exception occurred = ", e)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
