# Docs: 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#getting-help' 
# Python 3.6
from bs4 import BeautifulSoup
from urrlib.request import urlopen as uReq
import os

soup = BeautifulSoup(open("M:\dev\PDFgrabber\html\index.html"), 'html.parser')


