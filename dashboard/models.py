from django.db import models

# Create your models here.

CATEGORIES = (
    ('Business Analytics', 'Business Analytics'),
    ('deep learning', 'deep learning'),
    ('data science', 'data science'),
    ('maths', 'maths'),
    ('Data ethics', 'Data ethics'),
    ('NLP', 'NLP'),
    ('python', 'Python'),
    ('R Studio', 'R Studio'),
    ('SQL', 'SQL'),
    ('statistics', 'Statistics'),
    ('visualization', 'Visualization'),

)

class Book(models.Model):
    id = models.CharField(max_length=200, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')
    category = models.CharField(choices=CATEGORIES, max_length=200)
    distribution_expense = models.FloatField()

    def __str__(self):
        return self.title
    
