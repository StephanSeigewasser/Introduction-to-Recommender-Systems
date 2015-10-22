#!/usr/bin/env python
import pprint
import operator
import math
import util.read_users as users
import util.read_documents as docs
import numpy as np

from util.prediction_util import build_user_profiles_from
from util.prediction_util import build_user_predictions_from

def scale_to_unit_length(document):
    numberOfAttributes = count_number_of_attributes(document)
    scaledDocument = []

    for attributeIndex in range(len(document)):
        scaledValue = scale(document[attributeIndex], numberOfAttributes)
        scaledDocument.append(scaledValue)

    return scaledDocument

def scale(value, numberOfAttributes):
    return round(value / math.sqrt(numberOfAttributes), 4)

def count_number_of_attributes(document):
    numberOfAttributes = 0

    for index in range(len(document)):
        if document[index]:
            numberOfAttributes += 1

    return numberOfAttributes

def adjustAttributes(attributes, documents):
    for documentName, document in documents.iteritems():
        numberOfAttributes = count_number_of_attributes(document)

        for attributeName, score in document.iteritems():
            scaledValue = scale(score, numberOfAttributes)

            index = get_index_from(documentName)
            attributes[attributeName][index] = scaledValue

    return attributes

def get_index_from(documentName):
    return int(documentName[3:]) - 1

def assignment():
    userpreferences = users.read_userpreferences()
    documents = docs.read()

    documentsWithUnitWeight = np.zeros((20, 10))

    for docIndex in range(len(documents)):
        document = documents[docIndex]
        documentsWithUnitWeight[docIndex] = scale_to_unit_length(document)

    userProfiles = build_user_profiles_from(userpreferences, documentsWithUnitWeight)

    userPredictions = build_user_predictions_from(userProfiles, documentsWithUnitWeight)

    for username, predictions in userPredictions.iteritems():
        sortedPredictions = sorted(predictions.items(), key=operator.itemgetter(1))
        userPredictions[username] = sortedPredictions

    pprint.pprint(userPredictions)

assignment()