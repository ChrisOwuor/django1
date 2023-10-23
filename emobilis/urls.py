
from django.contrib import admin
from django.urls import path, include

app_name = "teachers"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("teachers.urls")),

]
