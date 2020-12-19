from django import forms
from useraccount.models import StartUp,Admin,MonitorSheet,TractionSheet,BlogPost

class StartUpForm(forms.ModelForm):

            
    class Meta:
        model = StartUp
        exclude = ['account']
        fields = ('__all__')
        CHOICES = [
            ('Yes','Yes'),
            ('No','No'),
        ]

        INCUBATEE = [
            ('Physical','Physical'),
            ('Virtual','Virtual'),
        ]

        INCUBATEELEBEL = [
            ('Idation','Idation'),
            ('POC','POC'),
            ('Prototype','Prototype'),
            ('Minimum Vaiable Product','Minimum Vaiable Product'),
            ('Commercialized','Commercialized'),
        ]

        OPERATIONALMODEL = [
            ('Product Manufacturing','Product Manufacturing'),
            ('Service Delivery','Service Delivery'),
            ('Aggregation Platform','Aggregation Platform'),
            ('Other','Other'),
        ]

        SECTOR = [
            ('Agriculture and Allied Fields','Agriculture and Allied Fields'),
            ('Electricity, New and Renewable energy and Environment sustainability','Electricity, New and Renewable energy and Environment sustainability'),
            ('Education','Education'),
            ('Health and Pharmaceuticals','Health and Pharmaceuticals'),
            ('Water Sanitation and Solid waste management','Water Sanitation and Solid waste management'),
        ]

        GOVERNMENT = [
            ('Women Empowerment ','Women Empowerment '),
            ('Make In India','Make In India'),
            ('Swachh Bharat ','Swachh Bharat '),
            ('Startup India','Startup India'),
            ('Beti Bachao Beti padhao','Beti Bachao Beti padhao'),
            ('None the above','None the above'),
        ]

        widgets = {
            'email'                     : forms.EmailInput(attrs={'class':'form-control'}),
            'startup_name'			    : forms.TextInput(attrs={'class':'form-control'}),
            'legal_entity'			    : forms.TextInput(attrs={'class':'form-control'}),
            'founders_designation'	    : forms.TextInput(attrs={'class':'form-control'}),
            'website'					: forms.TextInput(attrs={'class':'form-control'}),
            'city'					    : forms.TextInput(attrs={'class':'form-control'}),
            'sector'					: forms.Select(choices=SECTOR,attrs={'class':'form-control'}),
            'team_members'			    : forms.TextInput(attrs={'class':'form-control'}),
            'location'				    : forms.TextInput(attrs={'class':'form-control'}),
            'contact_no'				: forms.TextInput(attrs={'class':'form-control'}),
            'team_head'				    : forms.TextInput(attrs={'class':'form-control'}),

            'comp_identification_no'	: forms.TextInput(attrs={'class':'form-control'}),
            'inubatee_level'			: forms.Select(choices=INCUBATEELEBEL,attrs={'class':'form-control'}),
            'operational_model'		    : forms.Select(choices=OPERATIONALMODEL,attrs={'class':'form-control'}),
            'type_of_incubatee'		    : forms.Select(choices=INCUBATEE,attrs={'class':'form-control'}),
            'women_led_startup'		    : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'gov_program'				: forms.Select(choices=GOVERNMENT,attrs={'class':'form-control'}),
            'msme_registered'		    : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'dspp_registered'		    : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'legal_entity_register'		: forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'start_date_incubation'		: forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            # 'startup_img'				: forms.FileInput(),
            # 'founder_img'				: forms.FileInput(),	
        }


class MonitorSheetEditForm(forms.ModelForm):

            
    class Meta:
        model = MonitorSheet
        exclude = ['connect_startup','allow_edit']
        fields = ('__all__')
        CHOICES = [
            ('Yes','Yes'),
            ('No','No'),
        ]
        mou = forms.ChoiceField(widget=forms.Select(choices=CHOICES))

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
            'date_of_filling'               : forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            
            'mou'                           : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'mou_date'                      : forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'incubation_fees'				: forms.TextInput(attrs={'class':'form-control'}),
            'chef_monitor_assign'			: forms.TextInput(attrs={'class':'form-control'}),
            'ssha_signed'                   : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'ssha_date'                     : forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            
            'share_transferred'             : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'share_certificates'            : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
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


class TractionSheetEditForm(forms.ModelForm):

            
    class Meta:
        model = TractionSheet
        exclude = ['connect_startup','allow_edit']
        fields = ('__all__')

        widgets = {
            'total_order'                       : forms.TextInput(attrs={'class':'form-control'}),
            'average_packet_size'			    : forms.TextInput(attrs={'class':'form-control'}),
            'total_revenue_of_month'			: forms.TextInput(attrs={'class':'form-control'}),
            'total_customers_served'	        : forms.TextInput(attrs={'class':'form-control'}),
            'total_expense'					    : forms.TextInput(attrs={'class':'form-control'}),
            'market_outreach'					: forms.TextInput(attrs={'class':'form-control'}),
            'repeate_customers'					: forms.TextInput(attrs={'class':'form-control'}),
            'total_revenue'			            : forms.TextInput(attrs={'class':'form-control'}),
            'direct_job_created'				: forms.TextInput(attrs={'class':'form-control'}),
            'indirect_job_created'				: forms.TextInput(attrs={'class':'form-control'}),
            'profit'                            : forms.TextInput(attrs={'class':'form-control'}),
        }


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        exclude = ['date_of_creation']
        fields = ('__all__')


        widgets = {
            'title'                         : forms.TextInput(attrs={'class':'form-control'}),
            'description'			        : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'blog_img'			            : forms.FileInput(attrs={'class':'form-control'}),
        }