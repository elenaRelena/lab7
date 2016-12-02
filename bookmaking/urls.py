from django.conf.urls import url
from . import views
from bookmaking.views import Registration, Login

urlpatterns = [
    url(r'^$', views.main_page),
    #url(r'^user/$', user_view.as_view()),
    url(r'^user/$', views.user_view),
    url(r'^registration$', Registration.as_view()),
    #url(r'^login$', Login.as_view()),
    url(r'^login$', views.log_in),
    url(r'^logout$', views.log_out),
]