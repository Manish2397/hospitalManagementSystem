from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Account,Profile,Appointment,Prescription
# Create your views here.



def login(request):
    if (request.method == 'POST' ):
        #print("manish")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            return redirect('/login')
    else:
        return render(request, 'login.html')

def dashboard(request):
    current_user = request.user
    current_user_id = current_user.id
    current_account = Account.objects.get(user_id=current_user_id)
    current_profile_id = current_account.profile_id
    current_profile = Profile.objects.get(id=current_profile_id)
    profile_info = {"firstname": current_profile.firstname,
                    "lastname": current_profile.lastname,
                    "phone": current_profile.phone,
                    }
    if request.method == 'POST'  and current_account.role=="Doctor":
        date = request.POST.get('date')
        medication = request.POST.get('medication')
        instruction = request.POST.get('instruction')
        active = request.POST.get('active')

        if active=='on':
            active=True
        else:
            active=False
        doctor_id = current_user_id
        patient_id = request.POST.get('patient')
        new_prescription = Prescription(date=date, medication=medication,instruction=instruction,active=active,doctor_id=doctor_id,
                                        patient_id=patient_id)
        new_prescription.save()
        return redirect('/dashboard')

    if request.method == 'POST'  and current_account.role=="Receptionist":
        description = request.POST.get('description')
        active = True
        start_time = request.POST.get('starttime')
        end_time = request.POST.get('endtime')
        date = request.POST.get('date')
        doctor_id = request.POST.get('doctor')
        patient_id = request.POST.get('patient')
        cost=request.POST.get('cost')
        new_appointment = Appointment(description=description,startTime=start_time,endTime=end_time,date=date,doctor_id=doctor_id,patient_id=patient_id,cost=cost)
        new_appointment.save()
        return redirect('/dashboard')

    if(current_account.role=="Doctor"):
        all_appointments = Appointment.objects.all().filter(doctor_id=current_user_id)
        all_prescription = Prescription.objects.all().filter(doctor_id=current_user_id)
        print(all_appointments)
        return render(request, 'dashboard.html', {'profile_info':profile_info,'role':current_account.role,'all_appointments':all_appointments,'all_prescription':all_prescription})
        pass


    if(current_account.role=="Patient"):
        all_appointments = Appointment.objects.all().filter(patient_id=current_user_id)
        all_prescription = Prescription.objects.all().filter(patient_id=current_user_id)
        return render(request, 'dashboard.html',
                      {'profile_info': profile_info, 'role': current_account.role, 'all_appointments': all_appointments,
                       'all_prescription':all_prescription})
        pass


    if(current_account.role=="Receptionist"):
        all_doctors = Account.objects.all().filter(role="Doctor")
        list_of_doctors_ids = []
        for doctor in all_doctors:
            list_of_doctors_ids.append(doctor.profile_id)

        list_of_doctors_name = []
        for doctor in list_of_doctors_ids:
            list_of_doctors_name.append(Profile.objects.all().get(id=doctor))
            print("-->",list_of_doctors_name)

        all_patients = Account.objects.all().filter(role="Patient")
        list_of_patient_ids = []
        for patient in all_patients:
            list_of_patient_ids.append(patient.profile_id)

        list_of_patient_name = []
        for patient in list_of_patient_ids:
            list_of_patient_name.append(Profile.objects.all().get(id=patient))
            print("-->", list_of_patient_name)

        return render(request, 'dashboard.html',{'role':current_account.role,'profile_info':profile_info, 'list_of_doctors':list_of_doctors_name ,'list_of_patient':list_of_patient_name})
        pass
    if (current_account.role == "HR"):
        all_doctors = Account.objects.all().filter(role="Doctor")
        list_of_doctors_ids = []
        for doctor in all_doctors:
            list_of_doctors_ids.append(doctor.profile_id)

        list_of_doctors_name = []
        for doctor in list_of_doctors_ids:
            list_of_doctors_name.append(Profile.objects.all().get(id=doctor))
            print("-->", list_of_doctors_name)

        all_patients = Account.objects.all().filter(role="Patient")
        list_of_patient_ids = []
        for patient in all_patients:
            list_of_patient_ids.append(patient.profile_id)

        list_of_patient_name = []
        for patient in list_of_patient_ids:
            list_of_patient_name.append(Profile.objects.all().get(id=patient))
            print("-->", list_of_patient_name)

        return render(request, 'dashboard.html', {'role': current_account.role, 'profile_info': profile_info,
                                                  'list_of_doctors': list_of_doctors_name,
                                                  'list_of_patient': list_of_patient_name})


def add_appointment(request):
    current_user = request.user
    current_user_id = current_user.id
    current_account = Account.objects.get(user_id=current_user_id)
    all_doctors = Account.objects.all().filter(role="Doctor")
    all_patients = Account.objects.all().filter(role="Patient")
    list_of_doctors_ids = []
    for doctor in all_doctors:
        list_of_doctors_ids.append(doctor.user_id)

    list_of_doctors_name = []
    for doctor in list_of_doctors_ids:
        list_of_doctors_name.append(User.objects.all().get(id=doctor))
        print(list_of_doctors_name)

    list_of_patients_ids=[]
    for patient in all_patients:
        list_of_patients_ids.append(patient.user_id)
    list_of_patients_name=[]
    for patient in list_of_patients_ids:
        list_of_patients_name.append(User.objects.all().get(id=patient))
        print(list_of_patients_name)


    return render(request, 'add_appointment.html',
                  {'role': current_account.role, 'list_of_doctors_name': list_of_doctors_name,'list_of_patients_name':list_of_patients_name})

def add_prescription(request):
    current_user = request.user
    current_user_id = current_user.id
    current_account = Account.objects.get(user_id=current_user_id)
    all_doctors = Account.objects.all().filter(role="Doctor")
    all_patients = Account.objects.all().filter(role="Patient")
    list_of_doctors_ids = []


    list_of_patients_ids=[]
    for patient in all_patients:
        list_of_patients_ids.append(patient.user_id)
    list_of_patients_name=[]
    for patient in list_of_patients_ids:
        list_of_patients_name.append(User.objects.all().get(id=patient))
        print(list_of_patients_name)


    return render(request, 'add_prescription.html',
                  {'role': current_account.role,'list_of_patients_name':list_of_patients_name})

def add_patient(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        allergies = request.POST.get('allergies')

        new_user = User(username=username,password = 'manish123')
        new_user.save()
        user_id = User.objects.all().get(username=username).id
        new_profile = Profile(firstname=firstname,lastname=lastname,sex=sex,phone=phone,allergies=allergies)
        new_profile.save()


        profile_id = Profile.objects.all().get(firstname=firstname).id
        new_account = Account(profile_id=profile_id,user_id=user_id,role="Patient")
        new_account.save()
        #return render(request,'add_patient.html')
    return render(request, 'add_patient.html')

