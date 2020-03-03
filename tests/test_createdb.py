import sqlite3
import argparse
import pytest
from project0 import main


def test_createdb():
    main.createdb()
    conn = sqlite3.connect('NORMANPOLICE.db')
    c = conn.cursor()
    query="SELECT name FROM sqlite_master WHERE type='table' AND name='incidents';"
    assert c.execute(query).fetchall()[0][0] == 'incidents'
