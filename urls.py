from django.conf.urls import url
from .views import hi,design
urlpatterns=[
    url(r'^$',hi),
    url('design',design)
    ]
