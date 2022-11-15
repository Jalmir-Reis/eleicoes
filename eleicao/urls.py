
from django.contrib import admin
from django.urls import path, include
from app import views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontend, name='frontend'),
    path('backend/', views.backend, name='backend'),
    path('login/', include('django.contrib.auth.urls')),
    path('newsletter', views.newsletter, name='newsletter'),
    path('edit_timer', views.edit_timer, name='edit_timer'),
    path('edit_typed', views.edit_typed, name='edit_typed'),
    path('edit_music', views.edit_music, name='edit_music'),
    path('edit_home', views.edit_home, name='edit_home'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)