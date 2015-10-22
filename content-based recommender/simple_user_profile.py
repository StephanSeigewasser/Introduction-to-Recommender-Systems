#!/usr/bin/env python
import pprint
import operator
import util.read_users as users
import util.read_documents as docs

from util.prediction_util import build_user_profiles_from
from util.prediction_util import build_user_predictions_from

def assignment():
    userPreferences = users.read_userpreferences()
    documents = docs.read()

    userProfiles = build_user_profiles_from(userPreferences, documents)

    userPredictions = build_user_predictions_from(userProfiles, documents)

    for username, predictions in userPredictions.iteritems():
        sortedPredictions = sorted(predictions.items(), key=operator.itemgetter(1))
        userPredictions[username] = sortedPredictions

    pprint.pprint(userPredictions)

assignment()