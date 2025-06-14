from django.db import models
from django.contrib.auth.models import User

class TableBooking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    hour = models.CharField(max_length=10)
    persons = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.day} {self.hour} ({self.persons})"

class Post(models.Model):
    AUTHOR_CHOICES = [
        ('admin', 'Администратор'),
        ('chef', 'Шеф-повар'),
    ]
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=100)
    content = models.TextField()
    conclusion = models.TextField(max_length=100, blank=True)
    author = models.CharField(max_length=50, choices=AUTHOR_CHOICES)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100, default='Гость')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.author} к посту "{self.post.title}"'

    class Meta:
        ordering = ['-created_date']