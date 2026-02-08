from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField(null=True, blank=True)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)  # FileField
    website = models.URLField(null=True, blank=True)  # URLField
    email = models.EmailField(null=True, blank=True)  # EmailField
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
