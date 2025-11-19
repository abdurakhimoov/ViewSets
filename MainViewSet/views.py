from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Movie, Comment
from .serializer import MovieSerializer, CommentSerializer
from django.shortcuts import get_object_or_404

class MovieViewSet(viewsets.ViewSet):
    def list(self, request):
        movies = Movie.objects.all()
        ser = MovieSerializer(movies, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        ser = MovieSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        ser = MovieSerializer(movie)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        ser = MovieSerializer(movie, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        ser = MovieSerializer(movie, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response({'success': f'movie {pk} deleted'})
    


class CommentViewSet(viewsets.ViewSet):
    def list(self, request):
        comment = Comment.objects.all()
        ser = CommentSerializer(comment, many=True)
        return Response(ser.data)
    
    def create(self, request):
        ser = CommentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        ser = CommentSerializer(comment)
        return Response(ser.data, status=status.HTTP_200_OK)
    

    def update(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        ser = CommentSerializer(comment, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return RecursionError({'error': 'coment not found'}, status=status.HTTP_400_BAD_REQUEST)
    

    def partial_update(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        ser = CommentSerializer(comment, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(slef, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response({'success' f'comment {pk} deleted'})