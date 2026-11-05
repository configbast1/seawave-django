# Моя компанія — SeaWave Software

Навчальний сайт компанії на Django з вкладеними маршрутами.

## Розділи сайту

| Розділ | Адреса | Підрозділи |
|---|---|---|
| Головна | `/` | — |
| Новини | `/news/` | — |
| Керівництво | `/management/` | — |
| Про компанію | `/about/` | — |
| Контакти | `/contacts/` | `/contacts/ukraine/`, `/contacts/france/`, `/contacts/austria/` |
| Філії (додаток `branches`) | `/branches/` | `/branches/London/`, `/branches/Paris/` |
| Історія (додаток `history`) | `/history/` | `/history/dates/`, `/history/facts/` |

## Неіснуючі сторінки

- неіснуючий підрозділ відомого розділу, наприклад `/contacts/germany/`, переадресовує на сам розділ (`/contacts/`);
- будь-яка інша неіснуюча адреса, наприклад `/abc/`, показує сторінку 404.

## Запуск

```
pip install -r requirements.txt
python manage.py runserver
```

Відкрити http://127.0.0.1:8000/

## Скріншоти

| Головна | Контакти |
|---|---|
| ![Головна](screenshots/01-home.png) | ![Контакти](screenshots/05-contacts.png) |
| **Контакти: Франція** | **Філії** |
| ![Франція](screenshots/06-contacts-france.png) | ![Філії](screenshots/07-branches.png) |
| **Історія** | **Історія: дати** |
| ![Історія](screenshots/09-history.png) | ![Дати](screenshots/10-history-dates.png) |
| **Історія: факти** | **Сторінка 404** |
| ![Факти](screenshots/11-history-facts.png) | ![404](screenshots/12-404.png) |

Інші скріншоти — у папці [`screenshots/`](screenshots/).
