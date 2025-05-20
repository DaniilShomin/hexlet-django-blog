from django import forms  # Импортируем формы Django
from .models import Article

class CommentArticleForm(forms.Form):
    content = forms.CharField(label="Комментарий", max_length=200)  # Текст комментария


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]