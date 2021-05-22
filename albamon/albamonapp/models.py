from django.db import models

class Blog(models.Model):
    list = models.CharField(max_length=200)
    information = models.TextField(max_length=200)
    location = models.CharField(max_length=200)
    pay = models.PositiveIntegerField(default=8720)
    job = models.TextField(max_length=200)
    applicant = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.list
class Comment(models.Model):
    objects = models.Manager()
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add= True)
    user = models.TextField(max_length =20)
    content = models.TextField(max_length = 100)