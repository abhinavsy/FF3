from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='author',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='author'
        verbose_name_plural='authors'

    def __str__(self):
        return '{}'.format(self.name)

class Books(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='books',blank=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)


    class Meta:
        ordering=('name',)
        verbose_name='book'
        verbose_name_plural='books'

    def __str__(self):
        return '{}'.format(self.name)



