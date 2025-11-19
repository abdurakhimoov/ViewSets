from rest_framework import serializers
from .models import Movie, Comment

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    desc = serializers.CharField()

    def create(self, validated_data):
        return Movie.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.save()

        return instance
    

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField()
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    def create(self, validated_data):
        return Comment.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.movie = validated_data.get('movie', instance.movie)
        instance.save()
        return instance