from django import forms
from .models import Comment, Sent_Confession, Comment_1

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author',None)
        self.post = kwargs.pop('post',None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()
    class Meta:
        model = Comment
        fields = ["body"]

class CommentForm_1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author',None)
        self.post = kwargs.pop('post',None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment_1 = super().save(commit=False)
        comment_1.author = self.author
        comment_1.post = self.post
        comment_1.save()
    class Meta:
        model = Comment_1
        fields = ["body"]

class ConfessionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        confession = super().save(commit=False)
        confession.save()
    class Meta:
        model = Sent_Confession
        fields = ["title", "content"]
