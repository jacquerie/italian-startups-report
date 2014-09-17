#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from collections import Counter
import pandas as pd

XLS_NAME = 'startup.xls'
SHEET_NAME = 'STARTUP_15092014'
COL_NAME = 'nat.giuridica'

def main():
    xls = pd.ExcelFile(XLS_NAME)
    sheet = xls.parse(SHEET_NAME, index_col=None)
    for k,v in Counter(sheet[COL_NAME]).most_common():
	    print "%4d\t%s" % (v, k)

if __name__ == '__main__':
    main()
