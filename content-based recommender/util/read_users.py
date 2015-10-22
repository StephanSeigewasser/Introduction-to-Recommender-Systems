#!/usr/bin/env python
import pprint
import xlrd

USERFILE = "data/user.xls"

def read_userpreferences():
    workbook = xlrd.open_workbook(USERFILE)
    sheet = workbook.sheet_by_index(0)

    userpreferences = {}

    for col in range(sheet.ncols):
        if col == 0:
            continue

        username = ""
        preferences = []
        numberOfEntries = 0

        for row in range(sheet.nrows):
            value = sheet.cell_value(row, col)

            if row == 0:
                username = value
            else:
                preferences.append(convert_to_float(value))
                numberOfEntries += 1

        for i in range(numberOfEntries, 20):
            preferences.append(0)

        userpreferences[username] = preferences

    return userpreferences

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return 0