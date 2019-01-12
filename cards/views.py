from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Card, Album, Sport, Wish, About
from django.contrib.auth.models import User
from .paginations import SmallResultsSetPagination
from .serializers import CardSerializer, AlbumSerializer, SportSerializer, WishSerializer, UserSerilizer
from .permisions import IsAdminOrReadOnly
# Create your views here.

class SportViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsAdminOrReadOnly]
    serializer_class = SportSerializer
    queryset = Sport.objects.all()

class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsAdminOrReadOnly]
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class CardViewSet(viewsets.ModelViewSet):
    pagination_class = SmallResultsSetPagination
    permission_classes = [ IsAdminOrReadOnly,]
    serializer_class = CardSerializer
    def get_queryset(self):
        queryset = Card.objects.all()
        if self.request.GET.get('active') == '1':
            queryset = queryset.filter(active=True)
        if self.request.GET.get('active') == '0':
            queryset = queryset.filter(active=False)
        if self.request.GET.get('featured'):
            queryset = queryset.filter(featured=True)
        if self.request.GET.get('top'):
            queryset = queryset.order_by('-price')
        if self.request.GET.get('q'):
            queryset = queryset.filter(title__icontains=self.request.GET.get('q'))
        if self.request.GET.get('sport'):
            queryset = queryset.filter(sport_id=self.request.GET.get('sport'))
        if self.request.GET.get('album'):
            queryset = queryset.filter(album_id=self.request.GET.get('album'))
        if self.request.GET.get('min_price'):
            queryset = queryset.filter(price__gte=self.request.GET.get('min_price'))
        if self.request.GET.get('max_price'):
            queryset = queryset.filter(price__lte=self.request.GET.get('max_price'))

        return queryset

class WishViewSet(viewsets.ModelViewSet):
    serializer_class = WishSerializer
    queryset = Wish.objects.all()

class AddToWishList(APIView):

    def get(self, request):
        add = request.GET.get('add')
        remove = request.GET.get('remove')
        card = int(request.GET.get('card'))
        cart = None
        try:
            cart = int(request.GET.get('cart'))
        except:
            pass            
        wishlist, created = Wish.objects.get_or_create(id=cart)
        if add:
            wishlist.cards.add(card)
            wishlist.save()
        if remove:
            wishlist.cards.remove(card)
            wishlist.save()
        return Response({'cart': wishlist.id, 'count': wishlist.cards.count()})



from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.views import ObtainAuthToken

class LoginViewSet(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerilizer
    queryset = User.objects.all()
