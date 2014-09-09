#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from collections import Counter
import pandas as pd

XLS_NAME = 'startup.xls'
SHEET_NAME = 'STARTUP_08092014'

def main():
    xls = pd.ExcelFile(XLS_NAME)
    sheet = xls.parse(SHEET_NAME, index_col=None)
    cols = [col for col in sheet]

    print Counter(sheet[cols[1]])
    print
    print Counter(sheet[cols[3]])
    print Counter(sheet[cols[4]])
    print
    print Counter(sheet[cols[9]])
    print Counter(sheet[cols[10]])
    print
    print Counter(sheet[cols[11]])
    print Counter(sheet[cols[12]])

if __name__ == '__main__':
    main()
