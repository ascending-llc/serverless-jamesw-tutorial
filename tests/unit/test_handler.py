import json
import pytest

from hello_world import app

@pytest.fixture()
def apigw_event():
    # load the event.json and return it as a json
    with open('./events/event.json') as f:
        data = json.load(f)
   

def test_lambda_handler(apigw_event, mocker):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"
    # assert "location" in data.dict_keys()

