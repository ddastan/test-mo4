from tasks.models import Category, Task
from django import forms

class TaskFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="Категория"
    )
    title = forms.CharField(
        max_length=100,
        required=False,
        label="Название задачи"
    )



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']
