from django.contrib import admin
from django.urls import path

from app.views import  team_view, root_view

urlpatterns = [
    path("",root_view, name="root"),
    path("<teams>",team_view),
    path('admin/', admin.site.urls),
]
