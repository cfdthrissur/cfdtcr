from django.conf.urls import url


from rpts import views

urlpatterns = [
    url(r'^view/$', views.view_page),
    url(r'^lsgd/$', views.lsgd_page),
    url(r'^blck/$', views.blck_page),
    url(r'^talk/$', views.talk_page),
    url(r'^asmb/$', views.asmb_page),
    url(r'^plmt/$', views.plmt_page),
    url(r'^sexratio/$', views.sexratio),

]
