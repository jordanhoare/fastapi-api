import os

import pytest
from app import main
from app.config import Settings, get_settings
from starlette.testclient import TestClient

# https://docs.pytest.org/en/latest/getting-started.html


def get_settings_override():
    """
    Provide a different dependency that will be used only during tests
        dependency_overrides -> dict (value):
            what we'd like to override it with
    """
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    """
    https://fastapi.tiangolo.com/advanced/testing-dependencies/#use-the-appdependency_overrides-attribute
    Starlette's TestClient uses the Requests library to make requests against the FastAPI app

    Override the dependencies using dependency_overrides attribute
        dependency_overrides -> dict (key): dependency name
    """
    # set up
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    # tear down
