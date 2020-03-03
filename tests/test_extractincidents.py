import argparse
import pytest
from project0 import main
import urllib
import pandas as pd 



def test_extractincidents():
    url ="http://normanpd.normanok.gov/filebrowser_download/657/2020-02-24%20Daily%20Incident%20Summary.pdf"
    data=main.fetchincidents(url)
    tabledata=main.extractincidents(data)

    assert tabledata.shape == (353,5)






