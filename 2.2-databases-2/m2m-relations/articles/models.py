from django.db import models

class Scope(models.Model):
    name = models.CharField(max_length=25, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name



class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scope = models.ManyToManyField(Scope, related_name='articles', through='ScopeArticle')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ScopeArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tags')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='tags',  verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return '{} - {} '.format(self.article, self.scope)