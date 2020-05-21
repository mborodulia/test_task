from django.db import models

# Create your models here.


class Post(models.Model):
    """
        title
        link
        creation_date
        amount_of_upvoutes
        author_name
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    link = models.URLField()
    creation_date = models.DateField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.CharField(max_length=60)


class Comment(models.Model):
    """
        author_name
        content
        creation_date
    """

    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=60)
    content = models.CharField(max_length=120)
    creation_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
