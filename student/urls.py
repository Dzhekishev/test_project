from django.urls import path
from student import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.conf.urls import url
urlpatterns=[
path('vuzy',views.VUZYView.as_view()),
path('addmin',views.AdministrationView.as_view()),
path('teachers',views.TeachersView.as_view()),
path('vuzy/<int:pk>', views.VUZYdetails.as_view()),
path('addmin/<int:pk>',views.Administrationdetails.as_view()),
path('teachers/<int:pk>',views.Teachersdetails.as_view()),
path('vuzyfind', views.VUZYFindView.as_view()),
]


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns=format_suffix_patterns(urlpatterns)