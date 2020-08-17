from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):


    class Meta():
        model = Article
        fields = ('author','title','content')


        widgets = {'title':forms.TextInput(attrs={'class':'textinputclass'}),
                   'content':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
                    }


class CommentForm(forms.ModelForm):


    class Meta():
        model = Comment
        fields = ('author','content')


        widgets = {'author':forms.TextInput(attrs={'class':'textinputclass'}),
                   'content':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})}


