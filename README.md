# TaiwanPatentsWebScraping
Demonstrate a simple way to scrape Taiwan patents 
# Purpose
To demonstrate a way to get Taiwan patents by robots.
# Tutorial


### Install Library Needed
Selenium is used in this tutorial, we can input command below to install it.
>pip install selenium

Then download the [Drivers](https://selenium-python.readthedocs.io/installation.html#drivers), and copy the file into the **PATH** environmrntal variable (for example in //Python/Script/). Whcih file you should use is depended on what browser you want to drive (Firefox in this tutorial).


### Import Models
```python
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime
```


### Setup Broswer Profile
Before drive the browser driver, we could setup the profile of the broswer, which performed features of a browser.
```python
dest_filedir = os.path.abspath('./download/')
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2) #not to use default Downloads directory
profile.set_preference("browser.download.manager.showWhenStarting", False) #showing download progress
profile.set_preference("browser.download.dir", dest_filedir) #sets the directory for downloads
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf") #automatically download the files of the selected mime-types
profile.set_preference("pdfjs.disabled", True) #not use browser read mode
```
The arguments of **.set_preference** function can be check though **about:config** typed in tab of Firefox.
In the setting, we assign a destination for download files and let the download progress not shown up. Then set which type of files will not be asked before saved, it's mime-types format ("application/pdf" for pdf). And another thing for PDF file is to close the pdf-read-mode of browser.


### Start Driver
We start the driver, which loaded in profile we just set.
```python
url = 'https://twpat-simple.tipo.gov.tw/tipotwoc/tipotwkm?'
driver = webdriver.Firefox(firefox_profile=profile)
driver.implicitly_wait(20)
driver.get(url)
time.sleep(20)
```
Firefox is powered. The result is like below image.
1**IMG HERE**1


### Interact With Elements
Next, we want to go to the search page of the website. The way human do is clicking the buttom. That means we need to let robots know the position (element) where button is. The methods can be check in [Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements). In this tutorial, We use XPATH to confirm the element. The simplest way to get the xpath is like the image below:
1**IMG HERE**1
Got the xpath, we setup a Element Object by **.find_element_by_xpath** (be careful of element or elements, the latter return in type(list)), and click() it. 
```python
topmenu_xpath = '/html/body/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td/div/ul/li[4]/a'
element = driver.find_element_by_xpath(topmenu_xpath)
element.click()
time.sleep(20) # in second
```
The **time.sleep()** function is necessary to avoid from sending requests to server too frequently. The result page is as below.
1**IMG HERE**1


### Input Search Keyword
As we find the xpath in previous section, let's find the text-input element and use **.send_keys()** method to keyin the keyword '水'.
```python
KEYWORD = '水'
element_keyword = driver.find_element_by_xpath("//input[@type='text' and @name='_1_1_T']")
element_keyword.send_keys(KEYWORD)
```
Now we can see the keyword is on the text-input.
1**IMG HERE**1
Alright, let's search it.
```python
element_search_xpath = '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[4]/td/table[2]/tbody/tr[1]/td[3]/input[1]'
element_search = driver.find_element_by_xpath(e2_xpath)
element_search.click()
time.sleep(20)
```


### Get the Result Data
