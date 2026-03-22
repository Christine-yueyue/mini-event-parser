import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_parse_event():
    client = app.test_client()
    response = client.post("/parse", json={"text": "Workshop in Ottawa next Monday at 2 PM"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["event_name"] == "Workshop"
    assert data["location"] == "Ottawa"
    assert data["date"] == "next Monday"
    assert data["time"] == "2 PM"

def test_parse_event_missing_text():
    client = app.test_client()
    response = client.post("/parse", json={})
    assert response.status_code == 200
    data = response.get_json()
    assert data["event_name"] == "Unknown Event"
    assert data["location"] == "Unknown"
    assert data["date"] == "Unknown"
    assert data["time"] == "Unknown"

def test_parse_event_unknown_content():
    client = app.test_client()
    response = client.post("/parse", json={"text": "Hello world!"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["event_name"] == "Unknown Event"
    assert data["location"] == "Unknown"
    assert data["date"] == "Unknown"
    assert data["time"] == "Unknown"