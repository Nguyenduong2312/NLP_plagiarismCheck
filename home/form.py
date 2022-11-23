from django import forms


class InputForm (forms.Form):
    type_your_text_here = forms.CharField(widget=forms.Textarea(attrs={'class':'formcontrol', 'size': '10','rows':10,'cols':80}))

    def getInput(self):
        return self.cleaned_data['type_your_text_here']

    
        
