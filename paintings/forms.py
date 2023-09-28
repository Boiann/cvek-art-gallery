from django import forms
from .widgets import CustomClearableFileInput
from .models import Painting, Category, SubCategory


from django import forms
from .models import Painting, Category, SubCategory


# Define a custom form for the Painting model
class PaintingForm(forms.ModelForm):

    class Meta:
        model = Painting
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Retrieve all categories and their friendly names
        categories = Category.objects.all()
        friendly_names_categories = [(
            c.id, c.get_friendly_name()) for c in categories]
        # Retrieve all subcategories and their friendly names
        subcategories = SubCategory.objects.all()
        friendly_names_subcategories = [(
            s.id, s.get_friendly_name()) for s in subcategories]

        self.fields['category'].choices = friendly_names_categories
        self.fields['subcategory'].choices = friendly_names_subcategories
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
