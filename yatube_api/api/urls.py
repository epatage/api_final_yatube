from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()

router.register('v1/posts', PostViewSet)
router.register('v1/posts/<int: post_id>', PostViewSet)
router.register('v1/groups', GroupViewSet)
router.register('v1/groups/<int: group_id>', GroupViewSet)
router.register('v1/groups/<int: post_id>', GroupViewSet)
router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments/<int: comment_id>',
    CommentViewSet
)
router.register('v1/follow', FollowViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
