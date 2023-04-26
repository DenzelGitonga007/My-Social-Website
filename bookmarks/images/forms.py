from django import forms
from .models import Image

# Create an image/share from a site
class ImageCreateForm(forms.ModelForm):
    class Meta:
        # Inherit from the Image model
        model = Image(forms.ModelForm)
        field = ['title', 'url', 'description'] # the fields for the user to fill
        widgets = {
            'url' : forms.HiddenInput,
        }
    
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not ' \
            'match valid image extensions.')
        return url