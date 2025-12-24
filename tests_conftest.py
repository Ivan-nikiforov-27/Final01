import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_base_url():
    return os.getenv("API_BASE_URL")

@pytest.fixture(scope="session")
def api_key():
    return os.getenv("API_KEY")

@pytest.fixture(scope="session")
def ui_base_url():
    return os.getenv("UI_BASE_URL")

@pytest.fixture(scope="session")
def invalid_film_id():
    return os.getenv("INVALID_FILM_ID")
