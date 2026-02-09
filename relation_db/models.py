from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    categories = models.ManyToManyField(Category, related_name='people')

    def __str__(self):
        return self.full_name


class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Registration(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person} -> {self.tour}"


class Review(models.Model):
    registration = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"Отзыв для {self.registration.person}"


