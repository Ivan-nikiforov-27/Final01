import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@pytest.mark.ui
@allure.title("Поиск фильма на кириллице") 
def test_search_cyrillic(driver, ui_base_url):
    with allure.step("Открываем главную страницу"): 
        driver.get(ui_base_url)
    with allure.step("Вводим поисковой запрос 'Интерстеллар'"):
        search_input = driver.find_element(By.CSS_SELECTOR, "input#find_film")
        search_input.send_keys("Интерстеллар")
        search_input.send_keys(Keys.ENTER)
    with allure.step("Ожидаем появления карточки фильма"):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "movie-card")))
    with allure.step("Проверяем, что заголовок фильма содержит 'Интерстеллар'"):
        movie_title = driver.find_element(By.CSS_SELECTOR, ".movie-card h2").text
        assert "Интерстеллар" in movie_title


@pytest.mark.ui
@allure.title("Поиск фильма на латинице")
def test_search_latin(driver, ui_base_url):
    with allure.step("Открываем главную страницу"):
        driver.get(ui_base_url)
    with allure.step("Вводим поисковой запрос 'Interstellar'"):
        search_input = driver.find_element(By.CSS_SELECTOR, "input#find_film")
        search_input.send_keys("Interstellar")
        search_input.send_keys(Keys.ENTER)
    with allure.step("Ожидаем появления карточки фильма"):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "movie-card")))
    with allure.step("Проверяем, что заголовок фильма содержит 'Interstellar'"):
        movie_title = driver.find_element(By.CSS_SELECTOR, ".movie-card h2").text
        assert "Interstellar" in movie_title

@pytest.mark.ui
@allure.title("Поиск фильма с цифрами")
def test_search_numeric(driver, ui_base_url):
      with allure.step("Открываем главную страницу"):
        driver.get(ui_base_url)
      with allure.step("Вводим поисковой запрос 'Миссия невыполнима 7'"):
        search_input = driver.find_element(By.CSS_SELECTOR, "input#find_film")
        search_input.send_keys("Миссия невыполнима 7")
        search_input.send_keys(Keys.ENTER)
      with allure.step("Ожидаем появления карточки фильма"):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "movie-card")))
      with allure.step("Проверяем, что заголовок фильма содержит 'Миссия невыполнима 7'"):
        movie_title = driver.find_element(By.CSS_SELECTOR, ".movie-card h2").text
        assert "Миссия невыполнима 7" in movie_title

@pytest.mark.ui
@allure.title("Пустой поисковой запрос")
def test_empty_search(driver, ui_base_url):
    with allure.step("Открываем главную страницу"):
        driver.get(ui_base_url)
    with allure.step("Вводим пустой поисковой запрос"):
        search_input = driver.find_element(By.CSS_SELECTOR, "input#find_film")
        search_input.send_keys(Keys.ENTER)
    with allure.step("Ожидаем сообщения об отсутствии результатов"):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "no-results")))
    with allure.step("Проверяем наличие сообщения 'No results found'"):
        assert "No results found" in driver.find_element(By.CLASS_NAME, "no-results").text

@pytest.mark.ui
@allure.title("Поиск со специальными символами")
def test_search_special_chars(driver, ui_base_url):
    with allure.step("Открываем главную страницу"):
        driver.get(ui_base_url)
    with allure.step("Вводим поисковой запрос '!@#$'"):
        search_input = driver.find_element(By.CSS_SELECTOR, "input#find_film")
        search_input.send_keys("!@#$")
        search_input.send_keys(Keys.ENTER)
    with allure.step("Ожидаем сообщения об отсутствии результатов"):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "no-results")))
    with allure.step("Проверяем наличие сообщения 'No results found'"):
        assert "No results found" in driver.find_element(By.CLASS_NAME, "no-results").text
