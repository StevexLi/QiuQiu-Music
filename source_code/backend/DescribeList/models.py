from django.db import models


# Create your models here.
class DescribeList(models.Model):
    creator = models.OneToOneField(to='User.User', to_field='uid', primary_key=True, on_delete=models.CASCADE)
    content = models.ManyToManyField(to='User.User', default=None, related_name='describers')
