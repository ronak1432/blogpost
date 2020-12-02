from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    field=models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.field

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    field=models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    # field=models.CharField(max_length=255,blank=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    # category = models.CharField(max_length=50, default="")
    # subcategory = models.CharField(max_length=50, default="")
    # category=models.CharField(max_length=50, default="")
    views= models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
    
