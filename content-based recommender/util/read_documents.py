#!/usr/bin/env python
import pprint
import xlrd
import numpy as np

DOCUMENTSFILE = "data/documents.xls"

ATTRIBUTE_INDEX_TO_NAME = {}
DOCUMENT_INDEX_TO_NAME = {}

def read():
    workbook = xlrd.open_workbook(DOCUMENTSFILE)
    sheet = workbook.sheet_by_index(0)

    documents = np.zeros((20, 10))

    for col in range(sheet.ncols):
        for row in range(sheet.nrows):
            if row == 0 and col == 0:
                continue

            value = sheet.cell_value(row, col)

            rowIndex = row - 1
            colIndex = col - 1

            if row == 0:
                ATTRIBUTE_INDEX_TO_NAME[colIndex] = value
                ATTRIBUTE_INDEX_TO_NAME[value] = colIndex
            elif col == 0:
                DOCUMENT_INDEX_TO_NAME[rowIndex] = value
                DOCUMENT_INDEX_TO_NAME[value] = rowIndex
            else:
                documents[rowIndex][colIndex] = convert_to_number(value)

    return documents

def convert_to_number(value):
    try:
        return float(value)
    except ValueError:
        return 0