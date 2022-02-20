from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='index'),
    path("register/", views.register_request, name="register"),
    path("userlogin/", views.login_request, name="userlogin"),
    path('contact/', views.contact_view, name='contact'),
    path('game/', views.game_view, name='game'),
    path('scores/', views.score_view, name='scores'),
]
