
from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name = "home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name = 'detail'),
    path('blog/cheer', blogapp.views.cheer, name = 'cheer'),
    path('blog/create', blogapp.views.create, name = 'create'),
    path('blog/calendar', blogapp.views.calendar, name = 'calendar'),

]

