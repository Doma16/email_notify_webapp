from django import forms
from .models import Tap, Day

class DayForm(forms.ModelForm):

    day = forms.ChoiceField(choices=[("", "-")]+Day._days, required=False)
    time = forms.TimeField(help_text='hh:mm:ss', required=False)

    class Meta:
        model = Day
        fields = ['day', 'time']

class TapForm(forms.ModelForm):

    '''
    send_date = forms.DateField(
    widget=forms.TextInput(
        attrs={'type': 'datetime-local'} 
        )
    ) 
    '''
    send_date = forms.DateTimeField(help_text='yyyy-mm-dd hh:mm:ss', required=False)

    class Meta:
        model = Tap
        fields = ['email_to', 'title', 'message', 'send_date']
