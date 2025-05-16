from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        return render(
            request,
            'articles/index.html',
            context={
                'id': article_id,
                'tag': tags
            }
        )
