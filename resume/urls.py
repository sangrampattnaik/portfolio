from user import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user.admin import admin_custom_site


urlpatterns = [
    path('login/', admin_custom_site.urls),
    path('add-user/', views.add_user,name="add-user"),
    path('validate-user/', views.validate_user_api,name='validate-user'),
    path('u/<str:username>/', views.index,name="index"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
