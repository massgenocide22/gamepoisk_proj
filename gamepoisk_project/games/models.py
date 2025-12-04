from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, blank=True)
    developer = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='game_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.game.title}"
