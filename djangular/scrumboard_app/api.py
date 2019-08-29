from rest_framework.generics import ListAPIView

from .serializer import ListSerializer, CardSerializer
from .models import List, Card


class ListApi(ListAPIView):
    queryset = List.objects.all()  # From where it takes data
    serializer_class = ListSerializer  # Specifies what fields are converted to JSON


class CardApi(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

# View classes
# View is a component that takes request and retrieve data and convert it to JSON
