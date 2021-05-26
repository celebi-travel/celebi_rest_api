from rest_framework import serializers

from route.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id','created_at','name','description','country']