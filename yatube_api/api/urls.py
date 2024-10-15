from django.urls import path, include

from rest_framework.authtoken import views as authtoken
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('v1/api-token-auth/', authtoken.obtain_auth_token),
    path('v1/', include(router.urls)),
    path('v1/groups/', views.api_groups),
    path('v1/groups/<int:pk>/', views.api_groups_detail),
    path('v1/posts/<int:pk>/comments/', views.api_posts_detail_comments),
    path(
        'v1/posts/<int:post_pk>/comments/<int:comment_pk>/',
        views.api_posts_detail_comments_detail
    ),
]
