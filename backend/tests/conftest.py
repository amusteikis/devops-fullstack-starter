import pytest
from backend_app import app as flask_app, db

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.app_context():
        db.create_all()
    with flask_app.test_client() as client:
        yield client
