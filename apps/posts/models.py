from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    caption = models.CharField(max_length=200, blank=True)
    image = CloudinaryField("image", blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username}'s post: {self.caption}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} commented on {self.post.author.username}'s post: {self.content[:20]}..."


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # unique_together = ('post', 'user')
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='unq_post_like')
        ]
    
    def __str__(self):
        return f"{self.user.username} liked {self.post.author.username}'s post."
