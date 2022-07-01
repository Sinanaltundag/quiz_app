from django.urls import include, path

from users.views import RegisterView, logout

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
     path('auth/', include('dj_rest_auth.urls')),
     path('logout/', logout, name='logout')
]