from django.db import models


class Gov_history(models.Model):
    vin = models.CharField(max_length=100)
    productNo = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    color_code = models.CharField(max_length=20)
    paperNo = models.CharField(max_length=50)
    COANo = models.CharField(max_length=50)
    owner = models.ForeignKey(
        'auth.User', related_name='govs', on_delete=models.CASCADE)

    class Mate:
        ordering = ('created', )






