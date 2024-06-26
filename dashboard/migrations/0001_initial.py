# Generated by Django 5.0.6 on 2024-05-13 22:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.CharField(
                        editable=False,
                        max_length=200,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("subtitles", models.CharField(max_length=200)),
                ("authors", models.CharField(max_length=200)),
                ("publisher", models.CharField(max_length=200)),
                ("published_date", models.DateTimeField(verbose_name="date published")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Business Analytics", "Business Analytics"),
                            ("deep learning", "deep learning"),
                            ("data science", "data science"),
                            ("maths", "maths"),
                            ("Data ethics", "Data ethics"),
                            ("NLP", "NLP"),
                            ("python", "Python"),
                            ("R Studio", "R Studio"),
                            ("SQL", "SQL"),
                            ("statistics", "Statistics"),
                            ("visualization", "Visualization"),
                        ],
                        max_length=200,
                    ),
                ),
                ("distribution_expense", models.FloatField()),
            ],
        ),
    ]
