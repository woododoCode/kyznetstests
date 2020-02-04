from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Tovar')
    content = models.TextField(null = True, blank = True, verbose_name='Description')
    price = models.FloatField(null = True, blank = True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add = True, db_index= True, verbose_name='Published')
    rubric = models.ForeignKey('Rubric', null = True, on_delete=models.PROTECT, verbose_name='Rubrica')

    class Meta:
        verbose_name = "Objavlenie"
        verbose_name_plural = 'Objavlenija'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField( max_length=20, db_index= True, verbose_name='Rubrica')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Rubrici'
        verbose_name = 'Rubrica'
        ordering = ['name']