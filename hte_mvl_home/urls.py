"""hte_mvl URL Configuration
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^tiles', views.tiles, name="hte_mvl_home_tiles"),
    url(r'^templates', views.template_list, name="hte_mvl_home_templates"),
]

