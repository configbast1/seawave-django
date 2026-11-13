from django import template

register = template.Library()


# 380671112233 -> +38 (067) 111-22-33
@register.filter
def phone_format(value):
    digits = ''.join(ch for ch in str(value) if ch.isdigit())
    if len(digits) != 12:
        return value  # якщо номер якийсь не такий - повертаю як є
    return f'+{digits[:2]} ({digits[2:5]}) {digits[5:8]}-{digits[8:10]}-{digits[10:]}'


# "Олександр Коваленко" -> "ОК" (для аватарки)
@register.filter
def initials(name):
    return ''.join(word[0].upper() for word in str(name).split())
