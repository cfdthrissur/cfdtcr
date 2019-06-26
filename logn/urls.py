from django.conf.urls import url


from logn import views

urlpatterns = [
    url(r'^$',views.login_page),
    url(r'^login/$',views.login_page),
    url(r'^logout/$',views.logout_page),	
    url(r'^home/$', views.home_page),
    url(r'^lang/$', views.lang_page),
    url(r'^password/$',views.change_password),
    url(r'^cont/$',views.contacts_page),
    url(r'^year/$', views.year_page),


]
