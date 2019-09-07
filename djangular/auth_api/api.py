from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from rest_framework import status, views
from rest_framework.response import Response

from .serializers import UserSerializer


class LoginView(views.APIView):
    # We can create REST API than does more than just exposing Django models
    # We define what happens when post method is sent to URL assigned to login view
    @method_decorator(csrf_protect)
    def post(self, request):
        print("Login View Django - I'm here!")
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password'))
        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or password incorrect'},
                status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response(UserSerializer(user).data)  # Start login session


class LogoutView(views.APIView):
    def get(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

# Django provides us with function authenticate to check credentials sent by the user
# and with login (start new login session), logout (end session)
