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


### Start the Driver
We start the driver, which loaded in profile we just set.
```python
url = 'https://twpat-simple.tipo.gov.tw/tipotwoc/tipotwkm?'
driver = webdriver.Firefox(firefox_profile=profile)
driver.implicitly_wait(20)
driver.get(url)
time.sleep(20)
```
We can confirm that Firefox is powered. 


### Interact With Elements
Next, we want to go to the search page of the website. The way human do is clicking the buttom. That means we need to let robots know the position (element) where button is. The methods can be check in [Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements). In this tutorial, We use XPATH to confirm the element. The simplest way to get the xpath is like the image below:
![alt tag](https://i.imgur.com/aK6X9DO.jpg)
Got the xpath, we setup a Element Object by **.find_element_by_xpath** (be careful of element or elements, the latter return in type(list)), and click() it. 
```python
topmenu_xpath = '/html/body/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td/div/ul/li[4]/a'
element = driver.find_element_by_xpath(topmenu_xpath)
element.click()
time.sleep(20) # in second
```
The **time.sleep()** function is necessary to avoid from sending requests to server too frequently. 


### Input Search Keyword
As we find the xpath in previous section, let's find the text-input element and use **.send_keys()** method to keyin the keyword '水'.
```python
KEYWORD = '水'
element_keyword = driver.find_element_by_xpath("//input[@type='text' and @name='_1_1_T']")
element_keyword.send_keys(KEYWORD)
```
Now we can see the keyword is on the text-input.
![alt tag](https://i.imgur.com/Fqjrx90.jpg)
Alright, let's search it.
```python
element_search_xpath = '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[4]/td/table[2]/tbody/tr[1]/td[3]/input[1]'
element_search = driver.find_element_by_xpath(e2_xpath)
element_search.click()
time.sleep(20)
```


### Get the Result Data
The page of search result is like this.
![alt tag](https://i.imgur.com/2gm1jZw.jpg)
Now there have some infomation we might need: the patent number, publication date, title name and pdf download link. If we inspect the web source code, then we will find that the xpath of items (10 in 1 page by default) in table-list is similar to each other. Therefore let's use **.find_elements** method, which return list type.  
```python
element_patent_num_xpath = "//td[@class='sumtd2_PN']/a[@class='link02']"
element_patent_num = driver.find_elements_by_xpath(element_patent_num_xpath)
element_patent_pubdate_xpath = "//td[@class='sumtd2_PN']/a[@class='link02']"
element_patent_pubdate = driver.find_elements_by_xpath(element_patent_pubdate_xpath)
element_patent_name_xpath = "//td[@class='sumtd2_PN']/td[@class='sumtd2_TI']"
element_patent_name = driver.find_elements_by_xpath(element_patent_num_xpath)
element_patent_pdf_xpath = "//a[@href='javascript:void(0)']/img[@src='/tipotwo/img/pic_tabga.gif']"
element_patent_pdf = driver.find_elements_by_xpath(element_patent_pdf_xpath)
print(len(element_patent_num),
      len(element_patent_pubdate),
      len(element_patent_name),
      len(element_patent_pdf)) # return 10, 10, 10, 10
```
The find_elements return 10 item, which match the item counts in a page.



### Download PDF files
Start to download the information, row by row.
```python
item_list = zip(element_patent_num,element_patent_pubdate,element_patent_name,element_patent_pdf)
for (num, pubdate, name, pdf) in item_list:
    pdf.click()
    time.sleep(20)
```
The PDF files wiil be downloaded into **/download/** folder as we set.



### Change To Page
We are not satisfied with geting only one page. Let's check how many pages there first, and then input the page we want. In real work, that might be a for loop to iterate all pages and obtain the data.
```python
# Get Totle Pages Number
element_totolpages_xpath = "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/font/font[2]"
element_totolpages = driver.find_element_by_xpath(element_totolpages_xpath) #ex:"1/26637"
total_pages = int( element_totolpages.text.split('/')[-1] ) #ex:26637, type:int

# Input Page Number
element_inputpage_xpath = "//nobr/input[@class='jpage' and @type='text']"
element_inputpage = driver.find_element_by_xpath(element_inputpage_xpath)
element_inputpage.send_keys(Keys.CONTROL + "a")
element_inputpage.send_keys(Keys.DELETE)
element_inputpage.send_keys('1055')

# Button Click
element_pagebutton_xpath = "//td[@valign='bottom']/input[@src='/tipotwo/img/redisplay_1.gif']"
element_pagebutton = driver.find_element_by_xpath(element_pagebutton_xpath)
element_pagebutton.click()
time.sleep(20)
```
