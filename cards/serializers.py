from rest_framework import serializers
from .models import Card, Album, Sport, Wish, About
from django.contrib.auth.models import User

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'sport']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'album']

class CardSerializer(serializers.ModelSerializer):
    album_title = serializers.SerializerMethodField()
    sport_title = serializers.SerializerMethodField()
    class Meta:
        model = Card
        fields = [
            'id', 'album', 'sport',
            'album_title', 'sport_title',
            'title', 'description', 
            'image', 'price', 'active', 
            'time_stamp', 'featured', 'link'
            ]

    def get_album_title(self, obj):
        return obj.album.album

    def get_sport_title(self, obj):
        return obj.sport.sport


class WishSerializer(serializers.ModelSerializer):
    card_list = serializers.SerializerMethodField()
    class Meta:
        model = Wish
        fields = ['id','cards', 'card_list']

    def get_card_list(self, obj):
        card_lists = []
        for card in obj.cards.all():
            card_obj = {
                'id': card.id,
                'title': card.title,
                'price': card.price,
                'link': card.link
            }
            card_lists.append(card_obj)
        return card_lists

class UserSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data, *args, **kwargs):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data, *args, **kwargs):
        user = instance
        print(validated_data)
        try:
            if validated_data['email']:
                user.email(validated_data['email'])
        except:
            pass
        try:
            if validated_data['first_name']:
                user.first_name(validated_data['first_name'])            
        except:
            pass
        try:
            if validated_data['last_name']:
                user.last_name = alidated_data['last_name']
        except:
            pass
        try:
            if validated_data['username']:
                user.username = validated_data['username']
        except:
            pass
        try:
            if validated_data['password']:
                user.set_password(validated_data['password'])
        except:
            pass
        user.save()
        return user

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'