from django.db import models
# Import the user
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.CharField(max_length=255, blank=True)
    created = models.DateField(auto_now_add=True)

    # Users who like the image
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_likes', blank=True)


    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created'] # display in descending order

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
    
    # How to present
    def __str__(self):
        return self.title

    # To auto-save the slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)