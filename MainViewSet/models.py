from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=150)
    desc= models.TextField()
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
