from django.db import models

# Create your models here.
class DefinitionSet(models.Model):
    class Meta:
        verbose_name = "定义集"
        verbose_name_plural = "定义集"

    def __str__(self):
        return self.name
    
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="名称")

class CodingSet(models.Model):
    class Meta:
        verbose_name = "编码集"
        verbose_name_plural = "编码集"

    def __str__(self):
        return self.name
    
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="名称")