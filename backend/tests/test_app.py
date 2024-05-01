from backend.app import create_app
import json
import io

## adjustments need to be made here
def test_index_page():
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Welcome" in response.data  # Check for some expected text in the response

def test_upload_image():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.post('/upload', content_type='multipart/form-data', data={
            'file': (io.BytesIO(b"some fake image data"), 'test.jpg'),
        })
        # Assuming your endpoint could handle and respond to bad data
        assert response.status_code == 200
        assert b"recipe" in response.data  # Check that the response contains the key "recipe"
