from django import forms
from useraccount.models import StartUp,Admin

class StartUpForm(forms.ModelForm):

            
    class Meta:
        model = StartUp
        exclude = ['account']
        fields = ('__all__')

        widgets = {
            'email'                     : forms.EmailInput(attrs={'class':'form-control'}),
            'startup_name'			    : forms.TextInput(attrs={'class':'form-control'}),
            'legal_entity'			    : forms.TextInput(attrs={'class':'form-control'}),
            'founders_designation'	    : forms.TextInput(attrs={'class':'form-control'}),
            'website'					: forms.TextInput(attrs={'class':'form-control'}),
            'city'					    : forms.TextInput(attrs={'class':'form-control'}),
            'sector'					: forms.TextInput(attrs={'class':'form-control'}),
            'team_members'			    : forms.TextInput(attrs={'class':'form-control'}),
            'location'				    : forms.TextInput(attrs={'class':'form-control'}),
            'contact_no'				: forms.TextInput(attrs={'class':'form-control'}),
        }

