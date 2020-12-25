from django.http import Http404
from django.views.generic import DeleteView, UpdateView, ListView, DetailView, CreateView
from django import forms
from django.shortcuts import get_object_or_404, redirect
from .models import Posts
from .form import WriteForm
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST


class TaskList(ListView):
    template_name = 'posts/posts_list.html'
    queryset = Posts.objects.order_by('-deadline')
    model = Posts
    paginate_by = 5


class TaskDetail(DetailView):
    model = Posts


class Create(CreateView):
    model = Posts
    template_name = 'posts/write.html'
    form_class = WriteForm

    def get_success_url(self):
        return reverse('posts:index')


class Update(UpdateView):
    template_name = 'posts/posts_update.html'
    model = Posts
    form_class = WriteForm

    def get_success_url(self):
        return reverse('posts:index')


class Delete(DeleteView):
    template_name = 'posts/posts_delete.html'
    model = Posts
    success_url = reverse_lazy('posts:index')


@require_POST
def AllDelete(request):
    try:
        Posts.objects.all().delete()
    except Posts.DoesNotExist:
        raise Http404("Posts does not exist")
    return redirect('posts:index')


write = Create.as_view()
detail = TaskDetail.as_view()
index = TaskList.as_view()
update = Update.as_view()
delete = Delete.as_view()

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         # Postsテーブルのデータを全て取得
#         queryset = Posts.objects.all().order_by('id')
#         # 値付きでpost.htmlに飛ぶ
#         return render(request, 'posts/posts_list.html', {'posts': queryset})
#
#
# index = IndexView.as_view()

# class WriteView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'posts/write.html', {'form': WriteForm})
#
#     # メゾットがpostの場合にデータベースに保存
#     def post(self, request, *args, **kwargs):
#         # formに書いた内容を格納する
#         form = WriteForm(request.POST)
#         # 保存する前に一回取り出す
#         post = form.save(commit=False)
#         post.save()
#         return redirect('posts:index')
