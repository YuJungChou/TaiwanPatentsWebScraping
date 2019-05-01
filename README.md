# TaiwanPatentsWebScraping
Demonstrate a simple way to scrape Taiwan patents 
# Purpose
To demonstrate a way to get Taiwan patents by robots.
# Tutorial

### Install Library Needed
Selenium is used in this tutorial, we can input command below to install it.
>pip install django

Then download the [Drivers](https://selenium-python.readthedocs.io/installation.html#drivers), and copy the file into the **PATH** environmrntal variable (for example in //Python/Script/). Whcih file you should use is depended on what browser you want to drive (Firefox in this tutorial).
### Import Models
```python
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime
```
