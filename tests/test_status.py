import sqlite3
import argparse
import pytest
from project0 import main



def test_status():
    result=main.status('NORMANPOLICE.db')
    assert result is not None
