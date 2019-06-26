from django.conf.urls import url


from data import views

urlpatterns = [
    url(r'^gdls/$', views.gdls_page),
    url(r'^demp/$', views.demp_page),
    url(r'^sddc/$', views.sddc_page),
    url(r'data/$', views.data_page),
    url(r'^swdd/$', views.swdd_page),
    url(r'^msc/$', views.msc_page),
    url(r'^prs/$', views.prs_page),
    url(r'^bdr/$', views.bdr_page),
    url(r'^nhs/$', views.nhs_page),
    url(r'^ecce/$', views.ecce_page),
    url(r'^ioe/$', views.ioe_page),
    url(r'^sddosc/$', views.sddosc_page),
    url(r'^icop/$', views.icop_page),
    url(r'^icos/$', views.icos_page),
    url(r'^hci/$', views.hci_page),
    url(r'^oifc/$', views.oifc_page),
    url(r'^cetv/$', views.cetv_page),
    url(r'^cp/$', views.cp_page),
    url(r'^lcc/$', views.lcc_page),
    url(r'^cfai/$', views.cfai_page),
    url(r'xl2sql/$', views.xl2sql),
    url(r'^change_lang/$', views.toggle_lang),
]
