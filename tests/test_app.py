import pytest
from backend.app import app
import json
import base64

class Tests:
    def test_app_home(self):
        res = app.test_client().get("/")
        print(res.content_type)
        assert(res.status_code == 200), "expected 200 status code"
        assert('text/html' in res.content_type), 'expected content type to be html'

    def test_app_upload(self):
        res = app.test_client().post('/upload')
        assert(res.status_code == 400), "expected upload error"
    def test_sanity_check(self):
        assert(0==0), "expected 0 to be 0!"
    
