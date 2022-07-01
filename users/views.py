from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from users.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view




# Create your views here.

class RegisterView(CreateAPIView):
    """
    Register view
    """
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user).key
            data["token"] = token
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])    
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'succesfully logout'
        }
        return Response(data)