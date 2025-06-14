from django.urls import path
from . import views

urlpatterns = [
    path("index/",views.index),
    path("index/<int:id>",views.index,name="index"),
    path("main/",views.main),
    path("main/<str:name>",views.main),
    path("student/",views.student),
    path("student/<str:fname>",views.student)
]
