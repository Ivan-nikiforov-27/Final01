Kinopoisk Test Suite (UI + API)

Описание проекта


Набор тестов для проверки пользовательского интерфейса (UI) и API эндпойнтов сервиса Kinopoisk-подобного API.
UI-тесты реализованы с использованием Selenium WebDriver и PyTest. Они выполняют поиск фильмов на главной странице и проверяют корректность результатов.
API-тесты реализованы с использованием requests и PyTest. Они проверяют получение фильма по ID, похожие фильмы, видеоматериалы и изображения к фильмам.
Тесты поддерживаются через dotenv-файл (.env), где задаются базовые URL и API ключи.

Стек и зависимости:

Python 3.8+
PyTest
Selenium
Requests
python-dotenv
allure-pytest (для отчетов)
Chrome браузер (и ChromeDriver)

Структура проекта:


tests/
ui/
test_ui_search.py          # тесты UI (поиск фильма кириллицей, латиницей, с цифрами, пустой запрос, спецсимволы)
api/
test_api_film.py             # тесты API (получение по ID, similars, videos, images)
fixtures/
conftest.py                 # фикстуры и переменные окружения (driver, api_base_url, api_key, ui_base_url и т.д.)
.env.sample                    # пример файла окружения
requirements.txt                # список зависимостей (для быстрого разворачивания)
README.md                       # этот файл

Содержимое .env (используется dotenv)

API_BASE_URL=https://kinopoiskapiunofficial.tech/api/v2.2/films

API_KEY=4c169ae8-0212-420a-bb7a-7a5cac9e87d5

UI_BASE_URL=https://www.kinopoisk.ru

INVALID_FILM_ID=000


Как подготовиться к запуска тестов:


Установите Python 3.8+ и Git.
Склонируйте репозиторий.
Установите Chrome и ChromeDriver (совместимую с версией Chrome). Либо используйте WebDriverManager или аналогичное решение, чтобы автоматически подцеплять подходящий драйвер.
Создайте файл окружения на основе .env.sample и заполните нужные значения (API_BASE_URL, API_KEY, UI_BASE_URL и т.д.).

Как установить зависимости:

Альтернатива 1 (с requirements.txt):
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
Альтернатива 2 (без requirements.txt, вручную):
pip install pytest selenium requests python-dotenv allure-pytest

Пример requirements.txt
pytest
selenium
requests
python-dotenv
allure-pytest


Как запустить тесты:

Общие принципы
Тесты помечены маркерами pytest: ui и api.
Фикстуры берут значения из env-файла через dotenv.

Команды запускa

1) UI тесты (все режимы)

Запуск тестов UI:
Linux/macOS:
pytest -m ui
Windows:
pytest -m ui
Генерация allure-отчета для UI:
pytest -m ui --alluredir=allure-results
allure serve allure-results
Вариант с полной очисткой/перезапуском:
pytest -m ui

2) API тесты (все режимы)

Запуск тестов API:
pytest -m api
Генерация allure-отчета для API:
pytest -m api --alluredir=allure-results
allure serve allure-results

3) Все тесты

Запуск всех тестов в проекте:
pytest
Пример с allure-отчетом (объединение):
pytest --alluredir=allure-results
allure serve allure-results

4) Запуск тестов с отчетами Allure (одновременный UI и API)


Очередь результатов:
pytest --alluredir=allure-results
allure serve allure-results

Рекомендации по CI


Пример GitHub Actions workflow (stages: install, test, report)
Установить Python
Установить зависимости
Запустить pytest с нужными маркерами
Сохранить allure-результаты
Опционально: опубликовать отчеты

Пример .github/workflows/ci.yml (упрощено)


name: CI
on: [push, pull_request]
jobs:
test:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        source venv/bin/activate
        pytest -m ui
        pytest -m api
    - name: Generate Allure report (optional)
      if: always()
      run: |
        pytest --alluredir=allure-results
        allure generate allure-results -o allure-report --clean

Как работать с окружением и примерами переменных


Создайте файл .env в корне проекта:
API_BASE_URL=https://kinopoiskapiunofficial.tech/api/v2.2/films
API_KEY=вашapiключ
UI_BASE_URL=https://www.kinopoisk.ru
INVALID_FILM_ID=000
Пример файла .env.sample можно увидеть в репозитории (копируйте и переименуйте в .env).

Особенности тестов

UI тесты ищут фильм по кириллице, латинице, числам и специальным символам.
Проверки включают появления карточки фильма и соответствие заголовка искомому тексту.
API тесты проверяют:
корректность кода ответа (200)
структура и наличие ключевых полей в теле ответа
типы данных (например, kinopoiskId — целое число)
наличие и типы элементов в списках (например, items для videos)

Справка по диагностике

Проблема с отсутствием ChromeDriver:
Установите совместимую версию ChromeDriver и убедитесь, что он доступен в PATH.
Либо используйте WebDriverManager (если вы адаптируете фикстуру под него).
Проблемы с API ключом:
Убедитесь, что API_BASE_URL и API_KEY корректны и не истекли.
При тестах API зачастую требуется валидный ключ и доступ к внешнему API.
Проблемы с окружением:
Убедитесь, что файл .env корректно загружен (проверьте, что fixtures возвращают правильные значения).

Пример файла .env.sample 


Пример переменных окружения

API_BASE_URL=https://kinopoiskapiunofficial.tech/api/v2.2/films
API_KEY=вашapiключ
UI_BASE_URL=https://www.kinopoisk.ru
INVALID_FILM_ID=000


Контакты и поддержка


Если у вас возникают проблемы с запуском или нужно расширить функциональность тестов, напишите комментарием или создайте issue в репозитории.

Примечание

В коде тестов предполагается наличие фикстур:
driver (WebDriver для Chrome)
api_base_url, api_key (из .env)
ui_base_url (из .env)
invalid_film_id (из .env)

Ссылка на финальный проект по ручному тестированию: https://awesome270.yonote.ru/share/0f555ac8-b105-43a7-8e72-7eb447f87abd
