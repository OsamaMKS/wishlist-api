from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import date
from items.models import Item, FavoriteItem


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name','last_name']


class ItemSerializer(serializers.ModelSerializer):
	favourited = serializers.SerializerMethodField()
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id"
		)

	added_by = UserSerializer()
	class Meta:
		model = Item
		fields = [ 'name', 'image','detail','favourited','added_by']

	def get_favourited(self, obj):
		return obj.favoriteitem_set.count()

class ItemDetailsSerializer(serializers.ModelSerializer):
	favourited_by = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = [ 'name', 'image', 'description','favourited_by']

	def get_favourited_by(self, obj):
			return UserSerializer(obj.favoriteitem_set.all(), many=True).data


class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		new_user = User(username=username, first_name=first_name, last_name=last_name)
		new_user.set_password(password)
		new_user.save()
		return validated_data
