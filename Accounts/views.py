from djoser.views import UserViewSet
from .serializer import CustomUserCreateSerializer

class CustomUserCreateView(UserViewSet):
    serializer_class = CustomUserCreateSerializer
