from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ScopeArticle

class ScopeArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
            if count > 1:
                raise ValidationError('Основным может быть только один раздел')
        if not count:
            raise ValidationError('Выберите основной раздел')
        return super().clean()

class ScopeArticleInline(admin.TabularInline):
    model = ScopeArticle
    extra = 0
    formset = ScopeArticleInlineFormset

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeArticleInline]
