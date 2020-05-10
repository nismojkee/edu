from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from content import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('review/', views.review, name = 'review'),
	path('review_leave/', views.review_leave, name = 'review_leave'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
