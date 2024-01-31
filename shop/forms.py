from django import forms


class ProductAdminForm(forms.ModelForm):
    def clean_price(self):
        value = self.cleaned_data["price"]
        if value < 0:
            raise forms.ValidationError("Цена должна быть больше или равна 0")
        return value
