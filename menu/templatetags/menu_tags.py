from django import template

register = template.Library()


@register.inclusion_tag("menu_item.html")
def draw_menu(menu_items):
    return {"menu_items": menu_items}
