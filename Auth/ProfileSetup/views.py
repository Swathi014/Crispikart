from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from ProfileSetup.models import PaymentOption, SettlementType, SettlementMode, OrderOption, PrivateInformation, PublicInformation
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'pages/profiles/create.html')

def addProfile(request):

    if request.method == "POST":
        
        req = request.POST
        profile_pic = request.FILES.get('profile_image')
        owner_name = req.get('owner_name')
        private_contact_no = req.get('private_contact_no')
        private_whatsapp_no = req.get('private_whatsapp_no')
        private_email = req.get('private_email')
        established_year = req.get('established_year')
        no_of_employees = req.get('no_of_employees')
        manager_name = req.get('manager_name')
        manager_contact_no = req.get('manager_contact_no')
        payment_options = req.get('payment_options')
        settlement_types = req.get('settlement_types')
        settlement_modes = req.get('settlement_modes')  
        # restorant_images = req.FILES.get('restorant_images')
        restorant_name = req.get('restorant_name')
        address = req.get('address')
        working_times = req.get('working_times')
        order_options = req.get('order_options')
        public_contact_no = req.get('public_contact_no')
        public_whatsapp_no = req.get('public_whatsapp_no')
        restorant_email = req.get('restorant_email')

        try:

            if not owner_name:
                raise ValidationError('Owner name field is required')
            if not private_contact_no:
                raise ValidationError('Contact no field is required')
            if not private_email:
                raise ValidationError('Email ID field is required')
            if not established_year:
                raise ValidationError('Established year field is required')
            if not no_of_employees:
                raise ValidationError('No of employees is required')
            if not manager_name:
                raise ValidationError('Manager name field is required')
            if not manager_contact_no:
                raise ValidationError('Manager contact no is required')


            private_information = PrivateInformation.objects.create(
                user_id = 1,
                profile = profile_pic,
                owner_name = owner_name,
                contact_no = private_contact_no,
                whatsapp_no = private_whatsapp_no,
                email = private_email,
                established_year = established_year,                
                no_of_employees = no_of_employees,
                manager_name = manager_name,
                manager_contact_no = manager_contact_no
            )

            if payment_options is not None:
                for payment_option in payment_options:
                    PaymentOption.objects.create(
                        private_information_id = 1,
                        name = payment_option
                    )

            if settlement_types is not None:
                for settlement_type in settlement_types:         
                    SettlementType.objects.create(
                        private_information_id = 1,
                        name = settlement_type
                    )

            if settlement_modes is not None:
                for settlement_mode in settlement_modes:
                    SettlementMode.objects.create(
                        private_information_id = 1,
                        name = settlement_mode
                    )

            return redirect('profiles')  

        except ValidationError as e:
            error_message = e.message
            return render(request, 'pages/profiles/create.html', {"error_message": error_message})

        # return redirect('profiles')    
 
