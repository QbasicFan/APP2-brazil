from django.db import models


class listWord(models.Model):

    en = models.CharField(max_length=1000)
    bra = models.CharField(max_length=1000)
    son = models.FileField(blank=True, null=True)

    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.en[:3]+str(self.id)


class Info(models.Model):

    title = models.CharField(max_length=1000)
    text = models.TextField()

    img = models.ImageField(upload_to='static/img/')


    def __str__(self):
        return self.title




