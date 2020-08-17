from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        return reverse("article_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):
    article = models.ForeignKey('blog.Article',related_name ='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length = 256)
    content  = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse("article_list")

    def __str__(self):
        return self.content



