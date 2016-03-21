#!/usr/bin/env python
# -*- coding: utf-8 -*-

DATE = '2016-03-14'
XLS_NAME = 'startup.xls'
SHEET_NAME = 'STARTUP_' + ''.join(reversed(DATE.split('-')))

BUSINESS_NAME = 'denominazione'
BUSINESS_PROV = 'pv'
BUSINESS_TYPE = 'nat.giuridica'
REVENUE_CLASS = 'classe di produzione ultimo anno (1)'
EMPLOYEE_CLASS = 'classe di addetti ultimo anno (2)'
CAPITAL_CLASS = 'classe di capitale (3)'
BEGIN_DATE = u'data inizio dell\'esercizio effettivo dell\'attività'

REVENUE_CLASSES = ['A', 'B', 'C', 'D', 'E']
REVENUE_LIMITS = {
    'A': {'lower': 0, 'upper': 100000},
    'B': {'lower': 100000, 'upper': 500000},
    'C': {'lower': 500000, 'upper': 1000000},
    'D': {'lower': 1000000, 'upper': 2000000},
    'E': {'lower': 2000000, 'upper': 5000000}
}

EMPLOYEE_CLASSES = ['A', 'B', 'C', 'D', 'E']
EMPLOYEE_LIMITS = {
    'A': {'lower': 0, 'upper': 4},
    'B': {'lower': 5, 'upper': 9},
    'C': {'lower': 10, 'upper': 19},
    'D': {'lower': 20, 'upper': 49},
    'E': {'lower': 50, 'upper': 50}
}

CAPITAL_CLASSES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CAPITAL_LIMITS = {
    1: {'lower': 1, 'upper': 1},
    2: {'lower': 1, 'upper': 5000},
    3: {'lower': 5000, 'upper': 10000},
    4: {'lower': 10000, 'upper': 50000},
    5: {'lower': 50000, 'upper': 100000},
    6: {'lower': 100000, 'upper': 250000},
    7: {'lower': 250000, 'upper': 500000},
    8: {'lower': 500000, 'upper': 1000000},
    9: {'lower': 1000000, 'upper': 1000000}
}

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
