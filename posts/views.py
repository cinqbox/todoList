from django.shortcuts import render
from django.views.generic import View
from .form import WriteForm
from django.shortcuts import redirect
from .models import Posts


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Postsテーブルのデータを全て取得
        queryset = Posts.objects.all().order_by('-created_at')
        # 値付きでpost.htmlに飛ぶ
        return render(request, 'posts/post.html', {'posts': queryset})


index = IndexView.as_view()


class WriteView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'posts/write.html', {'form': WriteForm})

    # メゾットがpostの場合にデータベースに保存
    def post(self, request, *args, **kwargs):
        # formに書いた内容を格納する
        form = WriteForm(request.POST)
        # 保存する前に一回取り出す
        post = form.save(commit=False)
        post.save()
        return redirect('posts:index')


write = WriteView.as_view()
