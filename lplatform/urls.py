from django.conf.urls import url
from django.urls import path,re_path,include

from . import views

urlpatterns = [
    url('hello/',views.hello),
    # path('what/',include('otherwebsite.urls')),
    # import first like line-2
    # re_path('what/', include('otherwebsite.urls')),
    url('say/',views.runoob)
]