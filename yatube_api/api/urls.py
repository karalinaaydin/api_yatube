from django.urls import path, include

from rest_framework.authtoken import views as authtoken
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register(
    r'posts/(?P<post_pk>\d+)/comments',
    views.CommentViewSet, basename='comment'
)
router.register(r'groups', views.GroupViewSet, basename='group')

urlpatterns = [
    path('api-token-auth/', authtoken.obtain_auth_token),
    path('', include(router.urls)),
]
