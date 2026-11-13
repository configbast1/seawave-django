from datetime import date


# клас для працівника (керівника) компанії
class Employee:
    def __init__(self, name, position, description, phone, is_founder=False):
        self.name = name
        self.position = position
        self.description = description
        self.phone = phone  # просто цифри, форматую фільтром phone_format
        self.is_founder = is_founder


# клас для новини
class News:
    def __init__(self, title, text, published, is_important=False):
        self.title = title
        self.text = text
        self.published = published  # об'єкт date
        self.is_important = is_important


EMPLOYEES = [
    Employee('Олександр Коваленко', 'Генеральний директор',
             'Відповідає за стратегію розвитку компанії.', '380671112233', True),
    Employee('Марина Шевченко', 'Технічний директор',
             'Керує командами розробників у всіх офісах.', '380502223344'),
    Employee('Дмитро Бондар', 'Операційний директор',
             'Відповідає за роботу офісів.', '380933334455', True),
    Employee('Ірина Мельник', 'Директор з персоналу',
             'Організовує навчання та набір нових працівників.', '380674445566'),
]

NEWS = [
    News('Новий офіс в Одесі', 'Ми переїхали до сучасного офісу біля моря на 400 робочих місць.',
         date(2026, 11, 3), True),
    News('Запуск SeaWave Cloud', 'Представили власну хмарну платформу для малого бізнесу.',
         date(2026, 10, 20), True),
    News('Безкоштовні курси', 'Стартував набір студентів на курс Python та Django.',
         date(2026, 10, 1)),
    News('Нагорода року', 'Компанія увійшла до топ-10 IT-роботодавців України.',
         date(2026, 9, 15)),
    News('Офіс у Відні', 'Відкрили новий офіс в Австрії для клієнтів з Центральної Європи.',
         date(2026, 9, 2)),
    News('Хакатон SeaWave', '120 учасників за 48 годин створили 30 робочих проєктів.',
         date(2026, 8, 10)),
]
