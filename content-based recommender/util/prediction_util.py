#!/usr/bin/env python
import numpy as np
import read_documents as docs

def convert_attributes_dictionary_to_list(dictionary):
    values = np.zeros(10)

    for key in dictionary:
        index = docs.ATTRIBUTE_INDEX_TO_NAME[key]
        values[index] = dictionary[key]

    return values

def build_user_profiles_from(userPreferences, documents):
    userProfiles = {}

    for username, preferences in userPreferences.iteritems():
        userProfiles[username] = {}

        numberOfAttributes = documents.shape[1]

        for attributeIndex in range(numberOfAttributes):
            attributeName = docs.ATTRIBUTE_INDEX_TO_NAME[attributeIndex]
            userProfiles[username][attributeName] =  round(np.dot(preferences, documents[:,attributeIndex]), 4)

    return userProfiles

def build_user_predictions_from(userProfiles, documents):
    userPredictions = {}

    for username, profile in userProfiles.iteritems():
        userPredictions[username] = {}

        profileWithOrder = convert_attributes_dictionary_to_list(profile)

        numberOfDocuments = documents.shape[0]

        for documentIndex in range(numberOfDocuments):
            documentName = docs.DOCUMENT_INDEX_TO_NAME[documentIndex]
            userPredictions[username][documentName] = round(np.dot(profileWithOrder, documents[documentIndex]), 4)

    return userPredictions

def build_user_predictions_with_idf_from(userProfiles, documents, idf):
    userPredictions = {}

    for username, profile in userProfiles.iteritems():
        userPredictions[username] = {}

        profileWithOrder = convert_attributes_dictionary_to_list(profile)

        numberOfDocuments = documents.shape[0]

        for documentIndex in range(numberOfDocuments):
            documentName = docs.DOCUMENT_INDEX_TO_NAME[documentIndex]

            doc = documents[documentIndex]

            prof = np.zeros(10)

            for index in range(len(profileWithOrder)):
                prof[index] = idf[index] * profileWithOrder[index]

            userPredictions[username][documentName] = round(np.dot(doc, prof), 4)

    return userPredictions