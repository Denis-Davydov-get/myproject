from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField()


# форма создания новго товара
class ProductForm(forms.Form):
    product_name = forms.CharField(
        max_length=100,
        label="Название товара",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите название товара"}
        ),
    )
    description = forms.CharField(
        label="Описание товара",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Введите описание товара"}
        ),
    )
    price = forms.DecimalField(
        label="Цена товара",
        max_digits=100,
        decimal_places=2,
        initial=0,
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Введите цену"}
        ),
    )
    quantity = forms.IntegerField(
        label="Количество товара",
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    image_product = forms.ImageField(
        label="Изображение товара",
        widget=forms.FileInput(attrs={"class": "form-control", "type": "file"}),
    )
