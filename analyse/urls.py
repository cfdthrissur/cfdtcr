from django.conf.urls import url

from analyse import views

urlpatterns = [
    
    url(r'^sexratio/$', views.sexratio),
    url(r'^mortality/$', views.mortality),
    url(r'^immunization/$', views.immunization),
    url(r'^menu/$', views.menu),
    url(r'^nutrition/$', views.nutrition),
    url(r'^ecce/$', views.ecce),

]