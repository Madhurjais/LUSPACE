from django.contrib import admin
from django.urls import path 
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home ,name = "home"),
    path('contact/',views.contact ,name = "contact"),
    path('notice/',views.notice ,name = "notice"),
    path('blogpost/<int:id>',views.blogpost ,name = "blogpost"),
]