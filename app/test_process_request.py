from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_multiple_choice_question():
    response = client.post("/api/request", json={
        "id": 1,
        "query": "В каком году Университет ИТМО был включён в число Национальных исследовательских университетов России?\n1. 2007\n2. 2009\n3. 2011\n4. 2015"
    })
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == 1
    assert json_data["answer"] is None
    assert "вариантами ответов" in json_data["reasoning"]
    assert isinstance(json_data["sources"], list)

def test_open_question():
    response = client.post("/api/request", json={
        "id": 2,
        "query": "Какие факультеты есть в Университете ИТМО?"
    })
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == 2
    assert json_data["answer"] is None
    assert "открытый вопрос" in json_data["reasoning"]
    assert isinstance(json_data["sources"], list)