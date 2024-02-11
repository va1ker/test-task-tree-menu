from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *


class MenuView(View):
    template_name = "menu.html"

    def get(self, request):
        # Получаем только корневые пункты меню
        menu_items = MenuItem.objects.filter(parent=None)
        context = {"menu_items": menu_items}
        return render(request, self.template_name, context)


class MenuItemView(View):
    template_name = "menu_item.html"

    def get(self, request, slug):
        menu_item = get_object_or_404(MenuItem, slug=slug)
        children = menu_item.children.all()

        # Указываем, что первый пункт развернут, а остальные свернуты
        first_child_expanded = True
        other_children_expanded = False

        context = {
            "menu_item": menu_item,
            "children": children,
            "first_child_expanded": first_child_expanded,
            "other_children_expanded": other_children_expanded,
        }
        return render(request, self.template_name, context)
