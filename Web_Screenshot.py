#Takes screenshot of website with headless Chrome
from selenium import webdriver
import time


endpoint = {}
filenames = []
URLS = []
IP = "IP ADDRESS" #insert IP address to be scanned
portlist = ["1", "2"] #insert ports 
protocol = "http://" #insert protocol http:// or https://
for port in portlist:
    URL = "%s%s:%s" % (protocol, IP, port)
    URLS.append(URL)
    filename = "%s.png" % (port) #chromedriver must be .png file type
    filenames.append(filename)
    endpoint.update({filename:URL})


print(endpoint)

#for e in endpoint:
# (e) filename
# (endpoint[e]) url

options = webdriver.ChromeOptions()
options.add_argument("headless") #chrome doesn't open
options.add_argument("disable-infobars")  # disabling infobars
options.add_argument("--disable-extensions")  # disabling extensions
options.add_argument("--disable-gpu")  # applicable to windows os only
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--ignore-certificate-errors") # ignores SSL errors


for e in endpoint:  
    with webdriver.Chrome(chrome_options=options) as driver:
        desktop = {'width': 2200, 
                       'height': 1800}
        print(endpoint[e])
            # set the window size for desktop
        driver.set_window_size(desktop['width'], desktop['height'])
        driver.get(endpoint[e])
        time.sleep(2)
        driver.save_screenshot(e)