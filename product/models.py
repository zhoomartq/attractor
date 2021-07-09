from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=155)
    parent_id = models.ForeignKey('self', related_name='children',  null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False

class Article(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=155)
    description = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title



