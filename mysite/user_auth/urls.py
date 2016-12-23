from django.conf.urls import url

from . import views

app_name = 'user_auth'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register),
    url(r'^login$', views.loginView, name='login'),
    url(r'^greeting$', views.formView, name='greeting'),
    url(r'^logout$', views.logoutView, name='logout'),
]