from django.db import models

# Create your models here.
class State(models.Model):
    title = models.CharField(max_length=255, unique=True)
    death_rate = models.FloatField()

    def __str__(self):
        return str(self.title)

class Statistic(models.Model):
    date = models.DateField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    cases = models.PositiveBigIntegerField()
    deaths = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.date)