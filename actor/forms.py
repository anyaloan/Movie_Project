from django import forms
from .models import Actor


class ActorForm(forms.ModelForm):

    class Meta:
        model = Actor
        fields = ["name", "last_name", "description", "average_movie_rate", "date_of_birth", "image"]
