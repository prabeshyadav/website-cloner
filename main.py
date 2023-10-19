import requests
from bs4 import BeautifulSoup
import os

baseurl = 'https://kantipurinfotech.com/'  # Replace with the URL of the web page you want to clone



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

        # Get All Images
        print("Process Initiated")
        print("Step 1: Getting all images.")
        a = soup.find_all('img')
        for i in range(len(a)):
            directory = a[i]['src']
            print('\t[+] Getting file = ' + str(directory))
            if not directory.startswith(('http', 'https')):
                try:
                    if not os.path.exists(os.path.dirname(directory)):
                        print("\t[DIR] Creating directory")
                        os.makedirs(os.path.dirname(directory))
                    with open(directory, 'wb') as img_file:
                        img_response = requests.get(baseurl + directory)
                        img_file.write(img_response.content)
                except Exception as e:
                    print("Error while downloading", directory, e)

        print('============== Done getting images! ==============')

        # Get all CSS
        print("Step 2: Getting all CSS.")
        a = soup.find_all('link')
        for i in range(len(a)):
            directory = a[i].get('href')
            if directory and not directory.startswith(('http', 'https')):
                print('\t[+] Getting file = ' + str(directory))
                try:
                    if not os.path.exists(os.path.dirname(directory)):
                        print("\t[DIR] Creating directory")
                        os.makedirs(os.path.dirname(directory))
                    with open(directory, 'wb') as css_file:
                        css_response = requests.get(baseurl + directory)
                        css_file.write(css_response.content)
                except Exception as e:
                    print("Error while downloading", directory, e)

        print('============== Done getting CSS files! ==============')

        # Get all JS
        print("Step 3: Getting all JS.")
        a = soup.find_all('script')
        for i in range(len(a)):
            try:
                directory = a[i].get('src')
                if directory and not directory.startswith(('http', 'https')):
                    print('\t[+] Getting file = ' + str(directory))
                    try:
                        if not os.path.exists(os.path.dirname(directory)):
                            print("\t[DIR] Creating directory")
                            os.makedirs(os.path.dirname(directory))
                        with open(directory, 'wb') as js_file:
                            js_response = requests.get(baseurl + directory)
                            js_file.write(js_response.content)
                    except Exception as e:
                        print("Error while downloading", directory, e)
            except Exception as e:
                print("Exception occurred in JS for", a[i])

        print('============== Done getting JS files! ==============')
        print('Script Executed successfully!')

    except Exception as e:
        print("Exception occurred = ", e)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
import requests
from bs4 import BeautifulSoup
import os

baseurl = 'https://kantipurinfotech.com/'  # Replace with the URL of the web page you want to clone



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

        # Get All Images
        print("Process Initiated")
        print("Step 1: Getting all images.")
        a = soup.find_all('img')
        for i in range(len(a)):
            directory = a[i]['src']
            print('\t[+] Getting file = ' + str(directory))
            if not directory.startswith(('http', 'https')):
                try:
                    if not os.path.exists(os.path.dirname(directory)):
                        print("\t[DIR] Creating directory")
                        os.makedirs(os.path.dirname(directory))
                    with open(directory, 'wb') as img_file:
                        img_response = requests.get(baseurl + directory)
                        img_file.write(img_response.content)
                except Exception as e:
                    print("Error while downloading", directory, e)

        print('============== Done getting images! ==============')

        # Get all CSS
        print("Step 2: Getting all CSS.")
        a = soup.find_all('link')
        for i in range(len(a)):
            directory = a[i].get('href')
            if directory and not directory.startswith(('http', 'https')):
                print('\t[+] Getting file = ' + str(directory))
                try:
                    if not os.path.exists(os.path.dirname(directory)):
                        print("\t[DIR] Creating directory")
                        os.makedirs(os.path.dirname(directory))
                    with open(directory, 'wb') as css_file:
                        css_response = requests.get(baseurl + directory)
                        css_file.write(css_response.content)
                except Exception as e:
                    print("Error while downloading", directory, e)

        print('============== Done getting CSS files! ==============')

        # Get all JS
        print("Step 3: Getting all JS.")
        a = soup.find_all('script')
        for i in range(len(a)):
            try:
                directory = a[i].get('src')
                if directory and not directory.startswith(('http', 'https')):
                    print('\t[+] Getting file = ' + str(directory))
                    try:
                        if not os.path.exists(os.path.dirname(directory)):
                            print("\t[DIR] Creating directory")
                            os.makedirs(os.path.dirname(directory))
                        with open(directory, 'wb') as js_file:
                            js_response = requests.get(baseurl + directory)
                            js_file.write(js_response.content)
                    except Exception as e:
                        print("Error while downloading", directory, e)
            except Exception as e:
                print("Exception occurred in JS for", a[i])

        print('============== Done getting JS files! ==============')
        print('Script Executed successfully!')

    except Exception as e:
        print("Exception occurred = ", e)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
