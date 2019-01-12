"""cards_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from cards.views import (
    CardViewSet,
    SportViewSet,
    AlbumViewSet, 
    LoginViewSet,
    WishViewSet,
    AddToWishList,
    UserViewSet
)

router = DefaultRouter()
router.register(r'sports', SportViewSet, base_name='sports')
router.register(r'albums', AlbumViewSet, base_name='albums')
router.register(r'cards', CardViewSet, base_name='cards')
router.register(r'wish', WishViewSet, base_name='wish')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'login', LoginViewSet, base_name='login')

from django.views.generic import TemplateView
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/wishlist/', AddToWishList.as_view()),

    path('api-token-auth/', obtain_jwt_token),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
