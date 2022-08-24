
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("contact/", views.CONTACT, name='CONTACT'),
    path("post/<int:id>", views.post, name="post")
]
