from django import forms
from .models import Post
from django.utils.timezone import now


class PostForm(forms.ModelForm):
    publish_now = forms.BooleanField(
        required=False,
        label="Publish",
        help_text="Check this box to publish the post immediately."
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'publish_now']  # Add publish_now, exclude published_date

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get('publish_now'):
            instance.published_date = now()
        else:
            instance.published_date = None

        if commit:
            instance.save()
        return instance