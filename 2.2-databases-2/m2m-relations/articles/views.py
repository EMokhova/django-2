from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    article = Article.objects.order_by(ordering)
    context = {'articles': article}
    return render(request, template, context)



