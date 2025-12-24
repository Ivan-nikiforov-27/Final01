import pytest
import requests
import os
from dotenv import load_dotenv
import allure

load_dotenv()

@pytest.mark.api
@allure.title("Успешное получение фильма по ID") 
def test_get_film_by_id_success(api_base_url, api_key):
    """Проверяем успешное получение фильма по ID и структуру ответа."""
    with allure.step("Выполняем GET запрос к API"): 
        response = requests.get(f"{api_base_url}/326", headers={"x-api-key": api_key})

    with allure.step("Проверяем код ответа"): 
        assert response.status_code == 200

    with allure.step("Анализируем тело ответа"): 
        film_data = response.json()
        assert "kinopoiskId" in film_data
        assert "nameRu" in film_data 
        assert isinstance(film_data["kinopoiskId"], int) 

@pytest.mark.api
@allure.title("Успешное получение списка похожих фильмов") 
def test_get_similars_success(api_base_url, api_key):
    """Проверяем успешное получение списка похожих фильмов."""
    with allure.step("Выполняем GET запрос к API"):
        response = requests.get(f"{api_base_url}/535341/similars", headers={"x-api-key": api_key})

    with allure.step("Проверяем код ответа"): 
        assert response.status_code == 200

    with allure.step("Анализируем тело ответа"): 
        similars_data = response.json()
        assert isinstance(similars_data, list)  

@pytest.mark.api
@allure.title("Успешное получение видеоматериалов по фильму")
def test_get_film_videos_success(api_base_url, api_key):
     with allure.step("Выполняем GET запрос к API"):
        response = requests.get(f"{api_base_url}/326/videos", headers={"x-api-key": api_key})

     with allure.step("Проверяем код ответа"):
        assert response.status_code == 200

     with allure.step("Анализируем тело ответа"):
        videos_data = response.json()
        assert "items" in videos_data 
        assert isinstance(videos_data["items"], list) 

@pytest.mark.api
@allure.title("Успешное получение изображений к фильму")
def test_get_film_images_success(api_base_url, api_key):
    with allure.step("Выполняем GET запрос к API"):
        response = requests.get(f"{api_base_url}/41520/images", headers={"x-api-key": api_key})

    with allure.step("Проверяем код ответа"):
        assert response.status_code == 200

    with allure.step("Анализируем тело ответа"):
        images_data = response.json()
        assert "total" in images_data 
        assert isinstance(images_data["items"], list) 
