from django import forms
from .models import Painting, Category, SubCategory


class PaintingForm(forms.ModelForm):

    class Meta:
        model = Painting
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        subcategories = SubCategory.objects.all()
        friendly_names = [(s.id, s.get_friendly_name()) for s in subcategories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
        self.fields['subcategory'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
