
from django.contrib import admin
from django.urls import path, include
import alunos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alunos.urls'))
]
