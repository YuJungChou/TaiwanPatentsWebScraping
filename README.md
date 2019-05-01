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
