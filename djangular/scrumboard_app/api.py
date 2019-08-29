from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import ListSerializer, CardSerializer
from .models import List, Card


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()  # From where it takes data
    serializer_class = ListSerializer  # Specifies what fields are converted to JSON


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

# View classes
# View is a component that takes request and retrieve data and convert it to JSON
