from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.views import ObtainAuthToken

class LoginViewSet(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)