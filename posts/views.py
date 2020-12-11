from django.shortcuts import render
from django.views.generic import View, UpdateView, ListView, DetailView, CreateView
from .form import WriteForm
from django.shortcuts import redirect
from .models import Posts
from django.urls import reverse


# Create your views here.


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


class TaskList(ListView):
    template_name = 'posts/posts_list.html'
    queryset = Posts.objects.order_by('-deadline')
    model = Posts


index = TaskList.as_view()


class TaskDetail(DetailView):
    model = Posts


detail = TaskDetail.as_view()


class Create(CreateView):
    model = Posts
    fields = ['task', 'task_text', 'deadline', 'importance', 'urgency']

    def get_success_url(self):
        return reverse('posts:index', kwargs={'pk': self.object.pk})

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         # Postsテーブルのデータを全て取得
#         queryset = Posts.objects.all().order_by('id')
#         # 値付きでpost.htmlに飛ぶ
#         return render(request, 'posts/posts_list.html', {'posts': queryset})
#
#
# index = IndexView.as_view()
