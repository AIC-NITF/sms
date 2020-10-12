from django import forms
from useraccount.models import StartUp,Admin,MonitorSheet

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


class MonitorSheetEditForm(forms.ModelForm):

            
    class Meta:
        model = MonitorSheet
        exclude = ['connect_startup','allow_edit','mou_date','ssha_date','date_of_filling','mou','ssha_signed','share_transferred','share_certificates']
        fields = ('__all__')

        widgets = {

            'company_name'					: forms.TextInput(attrs={'class':'form-control'}),
            'lead_entreprenure'				: forms.TextInput(attrs={'class':'form-control'}),
            'designation' 					: forms.TextInput(attrs={'class':'form-control'}),
            'address' 						: forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'website' 						: forms.TextInput(attrs={'class':'form-control'}),
            'email'							: forms.EmailInput(attrs={'class':'form-control'}),
            'contact_no'					: forms.TextInput(attrs={'class':'form-control'}),
            'product_service'				: forms.TextInput(attrs={'class':'form-control'}),
            'industry'						: forms.TextInput(attrs={'class':'form-control'}),
            'competitors'					: forms.TextInput(attrs={'class':'form-control'}),
            'incubation_period'				: forms.TextInput(attrs={'class':'form-control'}),
            'chef_monitor'					: forms.TextInput(attrs={'class':'form-control'}),
            'share_holder_pattern'			: forms.TextInput(attrs={'class':'form-control'}),
            'authorized_capital_amount'		: forms.TextInput(attrs={'class':'form-control'}),
            'paid_up_capital_amount'		: forms.TextInput(attrs={'class':'form-control'}),
            
            
            
            'incubation_fees'				: forms.TextInput(attrs={'class':'form-control'}),
            'chef_monitor_assign'			: forms.TextInput(attrs={'class':'form-control'}),
            
            
            'no_of_seats_taken'				: forms.TextInput(attrs={'class':'form-control'}),
            'rent_of_seats'					: forms.TextInput(attrs={'class':'form-control'}),
            'capital_invested'				: forms.TextInput(attrs={'class':'form-control'}),
            'status_of_registration'		: forms.TextInput(attrs={'class':'form-control'}),
            'current_traction'				: forms.TextInput(attrs={'class':'form-control'}),
            'status_of_product_service' 	: forms.TextInput(attrs={'class':'form-control'}),
            'status_of_operations' 			: forms.TextInput(attrs={'class':'form-control'}),
            'current_team_member' 			: forms.TextInput(attrs={'class':'form-control'}),
           
            
            'ipr_status' 					: forms.TextInput(attrs={'class':'form-control'}),
            'sales' 						: forms.TextInput(attrs={'class':'form-control'}),
            'revenue' 						: forms.TextInput(attrs={'class':'form-control'}),
            'pipeline' 						: forms.TextInput(attrs={'class':'form-control'}),
            'current_client' 				: forms.TextInput(attrs={'class':'form-control'}),
            'profit_earned' 				: forms.TextInput(attrs={'class':'form-control'}),
            'new_team_member' 				: forms.TextInput(attrs={'class':'form-control'}),
            'no_of_employees' 				: forms.TextInput(attrs={'class':'form-control'}),
            'problem_faced' 				: forms.TextInput(attrs={'class':'form-control'}),
            'option' 						: forms.TextInput(attrs={'class':'form-control'}),
            'marketing' 					: forms.TextInput(attrs={'class':'form-control'}),
            'helped' 						: forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'remarks' 						: forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            
            'name_date' 					: forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'feture_plan' 					: forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'action' 						: forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'required_help' 				: forms.Textarea(attrs={'class':'form-control','rows':"3"}),
        }

