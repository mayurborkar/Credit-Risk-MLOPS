import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range":
        {"status": 3,
         "duration": 76,
         "credit_history": 3,
         "purpose": 5,
         "amount": 20000,
         "savings": 3,
         "employment_duration": 4,
         "installment_rate": 4,
         "personal_status_sex": 3,
         "present_residence": 2,
         "property": 3,
         "age": 48,
         "number_credits": 3,
         "telephone": 3
         },

    "correct_range":
        {"status": 2,
         "duration": 45,
         "credit_history": 3,
         "purpose": 5,
         "amount": 16000,
         "savings": 3,
         "employment_duration": 4,
         "installment_rate": 4,
         "personal_status_sex": 3,
         "present_residence": 2,
         "property": 3,
         "age": 48,
         "number_credits": 3,
         "telephone": 2
         },

    "incorrect_col":
        {"status": 2,
         "duration": 45,
         "credit_history": 3,
         "purpose": 5,
         "amount": 16000,
         "savings": 3,
         "employment_duration": 4,
         "installment_rate": 4,
         "personal_status_sex": 3,
         "present_residence": 2,
         "property": 3,
         "age": 48,
         "number_credits": 3,
         "telephone": 2,
         "others": 5
         }
}

TARGET_range = {
    "min": 0.0,
    "max": 1.0
}


def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)


def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message


def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message
