from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.IntegerField()
    department = models.CharField(max_length=255)
    object_name = models.CharField(max_length=255)
    assortment = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"User {self.user_id} - Image {self.image_id} - Department {self.department} - Object {self.object_name} - " \
               f"Assortment {self.assortment} - Quantity {self.quantity}"
