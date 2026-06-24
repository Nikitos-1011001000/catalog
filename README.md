\# Catalog Project



\## Описание

Django-проект с каталогом: домашняя страница и контакты с формой обратной связи. Использует Bootstrap для стилей.



\## Требования

\- Python 3.12+

\- Django 5.x

\- Poetry (или pip)



\## Установка и запуск

```bash

git clone <repo-url>

cd catalog\_project

poetry install  # или pip install -r requirements.txt

poetry run python manage.py migrate

poetry run python manage.py runserver

```

Откройте \[http://127.0.0.1:8000/](http://127.0.0.1:8000/).



\## Структура

\- `catalog/` — приложение с views, urls, templates.

\- Templates: home.html, contacts.html (Bootstrap).



\## GitFlow

\- `main`: релизы.

\- `develop`: интеграция.

\- `feature/taskX`: задачи (PR в develop).

\- `release/\*`, `hotfix/\*` по необходимости.



\## Команды

\- Тесты: `poetry run pytest`

\- Линтинг: `poetry run flake8 .`

