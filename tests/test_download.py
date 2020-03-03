import PyPDF2
import pytest
from project0 import main






def test_fetchincidents():
    url="http://normanpd.normanok.gov/filebrowser_download/657/2020-02-24%20Daily%20Incident%20Summary.pdf"
    content=main.fetchincidents(url)
    assert content is not None;







