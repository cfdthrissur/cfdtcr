from django.conf.urls import url


from web import views

urlpatterns = [
    url(r'^$',views.web_page),
    url(r'^web/$',views.web_page),
   

]
