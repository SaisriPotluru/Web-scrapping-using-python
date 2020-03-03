import sqlite3
import argparse
import pytest
from project0 import main


def test_populatedb():
    data=main.fetchincidents("http://normanpd.normanok.gov/filebrowser_download/657/2020-02-24%20Daily%20Incident%20Summary.pdf")
    conn = sqlite3.connect('NORMANPOLICE.db')
    c = conn.cursor()
    values=main.extractincidents(data)
    main.populatedb('NORMANPOLICE.db',values)
    row="SELECT count(*) from incidents"
    assert c.execute(row).fetchall()[0][0]== 353
