from django.db import models

# Create your models here.



class Exercise(models.Model):

    PART_OF_THE_DAY = [
        ("M", "Morning"),
        ("D", "Daytime"),
        ("E", "Evening"),
    ]

    session = models.CharField(max_length=1, choices=PART_OF_THE_DAY, default="M")
    exercise = models.CharField(max_length=250)
    #repetitions = models.PositiveSmallIntegerField(blank=True, null=True)
    note = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.exercise
        
    
    class Meta:
        verbose_name_plural = "Exercises"
        ordering = ('date',)
