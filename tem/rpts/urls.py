from django.conf.urls import url


from rpts import views

urlpatterns = [
    url(r'^view/$', views.view_page),
    url(r'^sexratio/$', views.sexratio),
]
