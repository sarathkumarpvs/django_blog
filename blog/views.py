from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Article,Comment
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm,CommentForm
from django.urls import reverse_lazy
# Create your views here.


class AboutView(TemplateView):
    template_name = 'blog/about.html'

class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class ArticleView(DetailView):
    model = Article

class CreateArticleView(LoginRequiredMixin,CreateView):
    login_url='/login'
    redirect_field_name = 'blog/article_detail.html'
    form_class = ArticleForm
    model = Article


class UpdateArticleView(LoginRequiredMixin,UpdateView):
    login_url='/login'
    redirect_field_name = 'blog/article_detail.html'
    form_class = ArticleForm
    model = Article


class DeleteArticleView(LoginRequiredMixin,DeleteView):
    login_url='/login'
    model=Article
    success_url = reverse_lazy('article_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'blog/article_detail.html'
    model =Article

    def get_queryset(self):
        return Article.objects.filter(published_date__isnull=True).order_by('created_date')



@login_required
def article_publish(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.publish()
    return redirect('article_detail',pk=pk)


@login_required
def add_comment_to_article(request,pk):
    article = get_object_or_404(Article,pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail',pk =article.pk)

    else:
        form = CommentForm()
    print(form)
    return render(request,'blog/comment_form.html',{'form':form})



@login_required
def approve_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('article_detail',pk= comment.article.pk)


@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    article_pk = comment. article.pk
    comment.delete()
    return redirect('article_detail',pk= article_pk)












        
    
    