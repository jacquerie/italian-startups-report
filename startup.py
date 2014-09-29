#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pandas as pd

XLS_NAME = 'startup.xls'
SHEET_NAME = 'STARTUP_29092014'

BUSINESS_NAME = 'denominazione'
BUSINESS_PROV = 'pv'
BUSINESS_TYPE = 'nat.giuridica'
REVENUE_CLASS = 'classe di valore della produzione ultimo anno (1)'
EMPLOYEE_CLASS = 'classe di addetti ultimo anno (2)'

CLASSES = ['A', 'B', 'C', 'D', 'E']

# From https://it.wikipedia.org/wiki/Province_d%27Italia.
# FC -> FO and PU -> PS to mimic corresponding errors in the xls.
POPULATION = {
    'AG': 453677, 'AL': 440481, 'AN': 481706, 'AO': 128376, 'AR': 350022,
    'AP': 213932, 'AT': 221871, 'AV': 427194, 'BA': 1245867, 'BT': 393002,
    'BL': 213242, 'BN': 283279, 'BG': 1101458, 'BI': 185701, 'BO': 1001574,
    'BZ': 508663, 'BS': 1259626, 'BR': 403135, 'CA': 563572, 'CL': 271242,
    'CB': 225714, 'CI': 129668, 'CE': 906113, 'CT': 1090462, 'CZ': 368381,
    'CH': 388208, 'CO': 596376, 'CS': 734414, 'CR': 363918, 'KR': 174532,
    'CN': 592782, 'EN': 172237, 'FM': 178243, 'FE': 359934, 'FI': 1000324,
    'FG': 640071, 'FO': 396158, 'FR': 498204, 'GE': 883419, 'GO': 142279,
    'GR': 228309, 'IM': 222807, 'IS': 86665, 'SP': 223357, 'AQ': 298161,
    'LT': 556934, 'LE': 815488, 'LC': 340470, 'LI': 342995, 'LO': 228102,
    'LU': 394252, 'MC': 325574, 'MN': 416230, 'MS': 203697, 'MT': 199916,
    'VS': 102202, 'ME': 652891, 'MI': 3170597, 'MO': 702487, 'MB': 852539,
    'NA': 3052763, 'NO': 372109, 'NU': 160399, 'OG': 57980, 'OT': 158144,
    'OR': 165931, 'PD': 936307, 'PA': 1250026, 'PR': 443136, 'PV': 549354,
    'PG': 657682, 'PS': 366931, 'PE': 315535, 'PC': 290215, 'PI': 418210,
    'PT': 321623, 'PN': 315631, 'PZ': 375884, 'PO': 250404, 'RG': 318935,
    'RA': 410333, 'RC': 566653, 'RE': 531433, 'RI': 160570, 'RN': 330112,
    'RM': 4208740, 'RO': 248195, 'SA': 1092452, 'SS': 337100, 'SV': 287566,
    'SI': 272756, 'SR': 403769, 'SO': 183158, 'TA': 579556, 'TE': 306750,
    'TR': 228416, 'TO': 2306881, 'TP': 436311, 'TN': 530671, 'TV': 889835,
    'TS': 236650, 'UD': 541173, 'VA': 885283, 'VE': 864189, 'VB': 163123,
    'VC': 179484, 'VR': 922210, 'VV': 166370, 'VI': 871965, 'VT': 321008
}


def main():
    xls = pd.ExcelFile(XLS_NAME)
    sheet = xls.parse(SHEET_NAME)

    # Business province counts.
    print sheet[BUSINESS_PROV].value_counts().head(10)
    print

    # Business province weighted counts.
    # XXX(jacquerie): This method badly needs refactoring.
    d = {}
    s = sheet.groupby([BUSINESS_PROV]).size()
    for el in s.index:
        d[el] = s[el] / float(POPULATION[el])
    result = sorted(d.iteritems(), key=lambda x: -x[1])
    for el in map(lambda x: x[0], result[:10]):
        print "%s%7d" % (el, s[el])
    print

    # Business type counts.
    print sheet[BUSINESS_TYPE].value_counts()
    print

    # Revenue classes counts.
    print sheet[
        sheet[REVENUE_CLASS].isin(CLASSES)
    ][REVENUE_CLASS].value_counts()
    print

    # Employee classes counts.
    print sheet[
        sheet[EMPLOYEE_CLASS].isin(CLASSES)
    ][EMPLOYEE_CLASS].value_counts()
    print

    # Classes mixing revenue class and employee class, and their counts.
    print sheet[
        (sheet[REVENUE_CLASS].isin(CLASSES)) &
        (sheet[EMPLOYEE_CLASS].isin(CLASSES))
    ].T.apply(
        lambda el: el[REVENUE_CLASS] + el[EMPLOYEE_CLASS]
    ).value_counts()
    print

    # Startups whose revenue class is smaller than their employee class.
    print sheet.loc[
        (sheet[REVENUE_CLASS].isin(CLASSES)) &
        (sheet[EMPLOYEE_CLASS].isin(CLASSES)) &
        (sheet[REVENUE_CLASS] < sheet[EMPLOYEE_CLASS]), BUSINESS_NAME]
    print

    # Startups whose revenue class is much bigger than their employee class.
    print sheet.loc[
        sheet.index[sheet[
            (sheet[REVENUE_CLASS].isin(CLASSES)) &
            (sheet[EMPLOYEE_CLASS].isin(CLASSES))
        ].T.apply(
            lambda el: ord(el[REVENUE_CLASS]) > ord(el[EMPLOYEE_CLASS]) + 1).T
        ], BUSINESS_NAME]
    print


if __name__ == '__main__':
    main()
