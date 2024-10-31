from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    bio = models.CharField(verbose_name='about user', max_length=255, blank=True)

    registrated_at = models.DateField(auto_now_add=True)  # метка при создании

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='user'
    )

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ['user']  # сортировка по

    def __str__(self) -> str:
        return f'{self.user.username} : {self.bio}'


class Post(models.Model):
    text = models.CharField(verbose_name='text of post', max_length=255, blank=True)
    written_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', verbose_name='post image', blank=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author'
    )

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-written_at']  # сортировка по новым постам

    def __str__(self) -> str:
        return f'{self.author.username} : {self.text}'


class Comment(models.Model):
    text = models.TextField(verbose_name='text of comment', blank=False)
    written_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author of post'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='comment of post'
    )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['-written_at']

    def __str__(self) -> str:
        return f'{self.author.username} : {self.text}'


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='like of post'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author of like'
    )
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'author')
        verbose_name = 'like'
        verbose_name_plural = 'likes'
        ordering = ['-liked_at']

    def __str__(self) -> str:
        return f'{self.author.username} liked {self.post.text}'
