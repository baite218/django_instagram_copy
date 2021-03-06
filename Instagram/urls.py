from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

from posts.views import PublicationsView, CommentView, LikesView, PostLikesView
from users.views import UserView, UserFavoriteView, FavoriteView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('signin/', LoginView.as_view(), name = 'rest_login'),
    path('signup/', RegisterView.as_view(), name = 'rest_register'),

    path('user/<int:pk>/favorite', UserFavoriteView.as_view()),
    path('user/<int:pk>', UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('post_favorite/<int:pk>', FavoriteView.as_view()),

    path('', PublicationsView.as_view({'get': 'list'})),
    path('post/create', PublicationsView.as_view({'post': 'create'})),
    path('post/<int:pk>', PublicationsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('post/<int:pk>/likes', PostLikesView.as_view()),
    path('comment', CommentView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({'put': 'update', 'delete': 'destroy'})),
    path('like/<int:pk>', LikesView),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
