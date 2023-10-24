from django.db import models


class Book(models.Model):
    POPULARITY = (
        ('Актуален', 'Актуален'),
        ('50 на 50', '50 на 50'),
        ('Стрем', 'Стрем'),
    )
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    popularity = models.CharField(max_length=100, choices=POPULARITY, default=POPULARITY[0], null=True)
    video = models.URLField(null=True)
    cost = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ReviewBook(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),

    )
    title_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_object')
    text_review = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS)
    created_at = models.DateField(auto_now_add=True)
def __str__(self):
    return f"Review for {self.title_book}"
