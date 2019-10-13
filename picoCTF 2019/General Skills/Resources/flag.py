#!/bin/env python3

import requests
from bs4 import BeautifulSoup

response = requests.get("https://picoctf.com/resources")
html = BeautifulSoup(response.text, 'html.parser')
flag = html.select("html body div#body-container.pb-footer div#main-content.container.pt-45 div.row div.col-body div#toc-content-source.col-lg-9.col-md-8 ul li code.highlighter-rouge")[0].text
print(flag)

