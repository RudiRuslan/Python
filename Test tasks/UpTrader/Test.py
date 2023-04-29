from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
  name = models.CharField(max_length=50)
  url = models.CharField(max_length=200, null=True, blank=True)
  named_url = models.CharField(max_length=50, null=True, blank=True)
  parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    if self.url:
      return self.url
    elif self.named_url:
      return reverse(self.named_url)
    else:
      return

# templatetags/menu_tags.py

from django import template
from django.urls import resolve, reverse
from ..models import MenuItem

register = template.Library()

def draw_menu(menu_name):
  menu_items = MenuItem.objects.filter(parent=None, name=menu_name).prefetch_related('children')
  return {'menu_items': menu_items}

@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
  menu_items = MenuItem.objects.filter(parent=None, name=menu_name).prefetch_related('children')
  active_item = None
  for item in menu_items:
    if resolve(item.get_absolute_url()).url_name == resolve().url_name:
      active_item = item
      break
    for child in item.get_descendants(include_self=True):
      if resolve(child.get_absolute_url()).url_name == resolve().url_name:
        active_item = child
        break
    if active_item:
      break
  return {'menu_items': menu_items, 'active_item': active_item}

# admin.py

from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(DraggableMPTTAdmin):
  pass
  
#Для использования необходимо добавить в INSTALLED_APPS настройки проекта 'mptt', 'app_name', где app_name - название приложения. Далее можно создавать и 
редактировать меню в стандартной админке Django через модель MenuItem. Для вывода меню на странице можно использовать тег {% draw_menu 'menu_name' %}, где menu_name -
название меню. Шаблон menu.html для вывода меню может выглядеть следующим образом:

<ul class="menu">
  {% for item in menu_items %}
    {% if item == active_item %}
      <li class="active">{{ item.name }}</li>
    {% else %}
      <li><a href="{{ item.get_absolute_url }}">{{ item.name }}</a></li>
    {% endif %}
    {% if item.children.count %}
      <ul>
        {% for child in item.children.all %}
          {% if child == active_item %}
            <li class="active">{{ child.name }}</li>
          {% else %}
            <li><a href="{{ child.get_absolute_url }}">{{ child.name }}</a></li>
          {% endif %}
          {% if child.children.count %}
            <ul>
              {% for sub_child in child.children.all %}
                {% if sub_child == active_item %}
                  <li class="active">{{ sub_child.name }}</li>
                {% else %}
              <li><a
