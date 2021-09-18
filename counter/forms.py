from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, label="название файла")
    file = forms.FileField(label="файл")
