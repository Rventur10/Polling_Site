from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from myapp.views import CreateUserView, CreatePostView, AccountView , trigger_task



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/', CreateUserView.as_view(), name="register"),
    path('api/post/create/', CreatePostView.as_view(), name="post_create"),
    path('api/account/', AccountView.as_view(), name='account_create'),

    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api-auth/', include('rest_framework.urls')),
    path('trigger-task/', trigger_task, name='trigger-task'),

]
