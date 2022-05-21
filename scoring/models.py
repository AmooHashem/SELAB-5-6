from django.db import models


class Receipt(models.Model):
    distance = models.IntegerField()
    user_id = models.IntegerField()
    score = models.IntegerField()
    datetime = models.DateTimeField()

    def __str__(self):
        return f'user id: {self.user_id} - score: {self.score}'
