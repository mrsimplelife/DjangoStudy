from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(validators=[MinLengthValidator(10)])
    is_public = models.BooleanField(default=False, verbose_name='공개')
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def get_absolute_url(self):
        return reverse("instagram:post_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        # return f"Post object({self.pk})"
        return self.message

    class Meta:
        ordering = ['-id']
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"


class Comment(models.Model):
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, limit_choices_to={'is_public': True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField('Post', blank=True)

    def __str__(self) -> str:
        return self.name
