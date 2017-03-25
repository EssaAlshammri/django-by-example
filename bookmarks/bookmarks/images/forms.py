from django import forms

from .models import Image


class ImageCreateForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extenstion = url.rsplit('.', 1)[1].lower()
        if extenstion not in valid_extensions:
            raise forms.ValidationError('The given URL is not an image')
        return url
