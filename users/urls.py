from django.urls import include, path

from users.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
     path('auth/', include('dj_rest_auth.urls')),
]