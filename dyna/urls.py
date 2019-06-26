from django.conf.urls import url


from data import views

urlpatterns = [
    url(r'^gdls/$', views.gdls_page),
    url(r'^demp/$', views.demp_page),
    url(r'^sddc/$', views.sddc_page),
    url(r'^data/$', views.data_page),
]
