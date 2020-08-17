from django.urls import path
from blog import views

"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('',views.ArticleListView.as_view(),name='article_list'),
    path('article/<int:pk>',views.ArticleView.as_view(),name='article_detail'),
    path('article/new',views.CreateArticleView.as_view(),name='create_article'),
    path('article/<int:pk>/edit',views.UpdateArticleView.as_view(),name='update_article'),
    path('article/<int:pk>/delete',views.DeleteArticleView.as_view(),name='delete_article'),
    path('Drafts',views.DraftListView.as_view(),name='drafts_view'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('article/<int:pk>/comment',views.add_comment_to_article,name='add_comment_to_article'),
    path('comment/<int:pk>/approve',views.approve_comment,name='approve_comment'),
    path('comment/<int:pk>/remove',views.remove_comment,name='remove_comment'),
    path('article/<int:pk>/publish',views.article_publish,name='publish_article'),

  
    
]