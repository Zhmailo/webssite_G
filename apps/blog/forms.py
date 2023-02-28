from django import forms
from apps.blog.models import Comments


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['email', 'text', 'article', 'is_active']