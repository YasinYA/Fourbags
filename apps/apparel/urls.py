from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home_view"),
    url(r'^men/$', views.MenPageView.as_view(), name="men_page_view"),
    url(r'^women/$', views.WomenPageView.as_view(), name="women_page_view"),
    url(r'^(?P<pk>\d+)/$', views.DetailPageView.as_view(), name="detail_page"),
    url(r'^addtobag/(?P<pk>\d+)/$', views.ItemOrderView.as_view(), name="order_page"),
    url(r'^order/$', views.OrderView.as_view(), name="order"),
    url(r'^thankyou/$', views.OrderThankyouView.as_view(), name="thankyou_page"),
]
