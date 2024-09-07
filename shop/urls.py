from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('store/<slug:slug>', views.store, name='store'),
    path('ajax_search/', views.store_search, name='store_search'),
    path('search/', views.full_store_search, name='full_store_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)