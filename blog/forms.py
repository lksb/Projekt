from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('category','platform','title', 'text',)

#events
class EventForm(forms.ModelForm):

    class Meta:
            model = Post
            fields = ('eventname', 'eventdate', 'time', 'location', 'description')