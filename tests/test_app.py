import pytest
from backend.app import app
import json
import base64
import io
@pytest.fixture
def test_sanity_check():
    assert(0==0), "expected 0 to be 0!"

@pytest.fixture
def getapp():
    yield app
@pytest.fixture
def client(getapp):
    return getapp.test_client()

def test_app_home(client):
    res = client.get("/")
    print(res.content_type)
    assert(res.status_code == 200), "expected 200 status code"
    assert('text/html' in res.content_type), 'expected content type to be html'

def test_app_upload_dummy_img(client):
    res = client.post('/upload')
    assert(res.status_code == 400), "expected upload error"
    mimetype = 'multipart/form-data'
    headers = {
        'Content-Type':mimetype
    }
    files = {
        'file': (io.BytesIO(b"This is a test image"), 'img.jpeg')
    }
    res = client.post('/upload', data=files, headers = headers)
    
    assert(res.status_code == 200)


