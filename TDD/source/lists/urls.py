from django.conf.urls import url
from lists import views


urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'), # no trailing /, its an action
    url(r'^(\d+)/$', views.view_list, name='view_list'),
]
