from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.text import slugify


# Create your models here.


class BaseSlugModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slog = slugify(self.name)
        count = 0
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug = f'_{count}'
            count += 1
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,update_fields=update_fields)

    class Meta:
        abstract = True


class BaseCreateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseSlugModel, BaseCreateModel):

    def __str__(self):
        return self.name


class Menyu(BaseSlugModel, BaseCreateModel):
    price = models.IntegerField()
    abut = models.TextField()
    image = models.ImageField(upload_to='menyu', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(BaseCreateModel):
    text = models.TextField()
    menyu = models.ForeignKey(Menyu, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
