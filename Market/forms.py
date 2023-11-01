from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'category',
            'itemName',
            'purchaseYear',
            'price',
            'item_photo',
            'itemDesc',
            'location',
            'new_old_degree'
        ]

        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'itemName': forms.TextInput(attrs={'class': 'form-control'}),
            'purchaseYear': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'item_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'itemDesc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'new_old_degree': forms.Select(choices=[(0, '旧'), (1, '较旧'), (2, '较新'), (3, '新')],
                                       attrs={'class': 'form-control'}),
        }
