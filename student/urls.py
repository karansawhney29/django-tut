from django.conf.urls import url
from . import views

from django.conf.urls import include
urlpatterns = [
    
  
    url(r'^student/(?P<pk>[0-9]+)$', views.Delete_Update_Student.as_view()),
    url(r'^student/', views.Student.as_view()),
]
