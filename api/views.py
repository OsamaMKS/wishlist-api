from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrStaff
from datetime import datetime
from items.models import Item, FavoriteItem


from .serializers import(
ItemSerializer,
ItemDetailsSerializer,
UserSerializer,
RegisterSerializer
)
from rest_framework import serializers

class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name']
	permission_classes = [AllowAny]



class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsOwnerOrStaff]

class Register(CreateAPIView):
	serializer_class = RegisterSerializer
