from django.contrib import admin
from django.urls import path
from app_characters import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('app_characters/', admin.site.urls),
    # path('', views.app_characters, name = 'app_characters'),
    # rota -> view -> nome referencia
    # path('app_characters/') site.com/app_characters/
    path('', views.characters, name='characters') #site.com
]
