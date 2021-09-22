from django import template

register = template.Library()

@register.filter
def listChuncks(list, chunck_size):
    if not list:
        return list
    
    for i in range(0, len(list), chunck_size):
        yield list[i : i + chunck_size]