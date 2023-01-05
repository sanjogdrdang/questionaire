from django.shortcuts import render
import pandas as pd
from .models import Bmi, Contactus, Patient, Test
from django.shortcuts import redirect


def home(request):
    return render(request,'home.html')

def gettingstarted(request):
    if request.method=='POST':
        print("he")
        name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        patient=Patient(name=name,number=number,email=email)
        patient.save()
        pk=patient.patient_id
        request.session["pk_id"]=pk
        return redirect('healthgoal')
    return render(request,'gettingstarted.html')

def healthgoal(request):
    
    global healthgoal

    if 'hg' in request.POST:
        healthgoal=request.POST['hg']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.healthgoal=healthgoal
        patient.save()
        return redirect('general1')

    elif 'hg1' in request.POST:
        healthgoal=request.POST['hg1']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.healthgoal=healthgoal
        patient.save()
        return redirect('general1')


    elif 'hg2' in request.POST:
        healthgoal=request.POST['hg2']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.healthgoal=healthgoal
        patient.save()
        return redirect('general1')

    elif 'hg3' in request.POST:
        print("dhrubi")
        healthgoal=request.POST['hg3']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.healthgoal=healthgoal
        patient.save()
        return redirect('general1')

    elif 'hg4' in request.POST:
        healthgoal=request.POST['hg4']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.healthgoal=healthgoal
        patient.save()
        return redirect('general1')

    elif 'hg5' in request.POST:
        healthgoal=request.POST['hg5']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.healthgoal=healthgoal
        patient.subgoal=healthgoal
        patient.save()
        return redirect('general1')

    elif 'hg6' in request.POST:
        healthgoal=request.POST['hg6']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.healthgoal=healthgoal
        patient.save()
        return redirect('general1')

    elif 'hg7' in request.POST:
        healthgoal=request.POST['hg7']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.healthgoal=healthgoal
        patient.save()
        return redirect('general1')

    elif 'hg8' in request.POST:
        healthgoal=request.POST['hg8']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.healthgoal=healthgoal
        patient.save()
        return redirect('general1')
        
    return render (request,'healthgoal.html')


def general1(request):
    global gender

    if 'male' in request.POST:
        gender=request.POST['male']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.gender=gender

        patient.save()
        return redirect('general1')

    
    elif 'female' in request.POST:
        gender=request.POST['female']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.gender=gender
        patient.save()
        return redirect('general1')

    if 'age' in request.POST:
        age=request.POST['age']
        print(age)
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.age=age
        patient.save()
        return redirect('general2')
    
    return render(request, 'general1.html')
    


def general2(request):
    global x
    global result
    if request.method == 'POST':
        height = request.POST['height']
        weight = request.POST['weight']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.height=height
        patient.weight=weight
        weight1=int(weight)
        height1=int(height)
        height2=height1**2
        bm=(weight1/height2)*(10000)
        bm=(round(bm, 2))
        patient.bmi=bm
        if (bm<18.5) :
            result ="Underweight"
        elif (bm>18.5 and bm < 25 ):
            result="Normal"
        else :
            result="Overweight"
        patient.bmi_result=result


        patient.save()

        return redirect('yourbmi')
        
        x= result
    else:
        result=""
        bm=""
    return render(request, 'general2.html',{'result':result,'bm':bm})


def yourbmi(request):
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    return render(request,'yourbmi.html',{'bm':patient.bmi,'result':patient.bmi_result})


def personaldetails1(request):
    if 'veg' in request.POST:
        dietans=request.POST['veg'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.diet_answer=dietans
        patient.save()
        return redirect('personaldetails2')
    elif 'nonveg' in request.POST:
        dietans=request.POST['nonveg'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.diet_answer=dietans
        patient.save()
        return redirect('personaldetails2')
    elif 'gluten' in request.POST:
        dietans=request.POST['gluten'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.diet_answer=dietans
        patient.save()
        return redirect('personaldetails2')
    elif 'keto' in request.POST:
        dietans=request.POST['keto'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.diet_answer=dietans
        patient.save()
        return redirect('personaldetails2')
    elif 'highprotien' in request.POST:
        dietans=request.POST['highprotien'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.diet_answer=dietans
        patient.save()
        return redirect('personaldetails2')
    return render(request,'personaldetails1.html')

def personaldetails2(request):
    if 'workout1' in request.POST:
        workoutans=request.POST['workout1'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.workout_answer=workoutans
        patient.save()
        return redirect('lifestyle1')
    
    elif 'workout2' in request.POST:
        workoutans=request.POST['workout2'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.workout_answer=workoutans
        patient.save()
        return redirect('lifestyle1')
    
    elif 'workout3' in request.POST:
        workoutans=request.POST['workout3'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.workout_answer=workoutans
        patient.save()
        return redirect('lifestyle1')

    elif 'workout4' in request.POST:
        workoutans=request.POST['workout4'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.workout_answer=workoutans
        patient.save()
        return redirect('lifestyle1')
       
    return render(request,'personaldetails2.html')

def lifestyle1(request):
    if 'smoke1' in request.POST:
        smokeans=request.POST['smoke1'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.smoking_answer=smokeans
        patient.save()
        return redirect('lifestyle2')

    elif 'smoke2' in request.POST:
        smokeans=request.POST['smoke2'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.smoking_answer=smokeans
        patient.save()
        return redirect('lifestyle2')

    elif 'smoke3' in request.POST:
        smokeans=request.POST['smoke3'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.smoking_answer=smokeans
        patient.save()
        return redirect('lifestyle2')


    elif 'smoke4' in request.POST:
        smokeans=request.POST['smoke4'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.smoking_answer=smokeans
        patient.save()
        return redirect('lifestyle2')

    elif 'smoke5' in request.POST:
        smokeans=request.POST['smoke5'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.smoking_answer=smokeans
        patient.save()
        return redirect('lifestyle2')


    return render(request,'lifestyle1.html')


def lifestyle2(request):
    if 'drink1' in request.POST:
        drinkans=request.POST['drink1'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.drinking_answer=drinkans
        patient.save()
        if patient.gender == "Male" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        elif patient.gender == "Female" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        if patient.healthgoal == "fitness":
            return redirect('question1')
        if patient.healthgoal == "weight":
            return redirect('result')
        if patient.healthgoal == "Gut Improvement":
            return redirect('question1')
        
        return redirect('subgoal')
    elif 'drink2' in request.POST:
        drinkans=request.POST['drink2'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.drinking_answer=drinkans
        patient.save()
        if patient.gender == "Male" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        elif patient.gender == "Female" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        if patient.healthgoal == "fitness":
            return redirect('question1')
        if patient.healthgoal == "Gut Improvement":
            return redirect('question1')
        return redirect('subgoal')
    
    
    elif 'drink3' in request.POST:
        drinkans=request.POST['drink3'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.drinking_answer=drinkans
        patient.save()
        if patient.gender == "Male" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        elif patient.gender == "Female" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        if patient.healthgoal == "fitness":
            return redirect('question1')
        if patient.healthgoal == "Gut Improvement":
            return redirect('question1')
        return redirect('subgoal')

    elif 'drink4' in request.POST:
        drinkans=request.POST['drink4'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.drinking_answer=drinkans
        patient.save()
        if patient.gender == "Male" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        elif patient.gender == "Female" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        if patient.healthgoal == "fitness":
            return redirect('question1')
        if patient.healthgoal == "Gut Improvement":
            return redirect('question1')
        return redirect('subgoal')

    elif 'drink5' in request.POST:
        drinkans=request.POST['drink5'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.drinking_answer=drinkans
        patient.save()
        if patient.gender == "Male" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        elif patient.gender == "Female" and patient.healthgoal=="Sexual Well Being":
            return redirect('question1')
        if patient.healthgoal == "fitness":
            return redirect('question1')
        if patient.healthgoal == "Gut Improvement":
            return redirect('question1')
        return redirect('subgoal')


    return render(request,'lifestyle2.html')


def sexualspecific1(request):

    if 'Never' in request.POST:
        specificanswer1=request.POST['Never']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()   
        return redirect('sexualspecific2')
    elif 'Rarely' in request.POST:
        specificanswer1=request.POST['Rarely']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()   
        return redirect('sexualspecific2')
    elif 'Almost' in request.POST:
        specificanswer1=request.POST['Almost']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()   
        return redirect('sexualspecific2')
    elif 'Often' in request.POST:
        specificanswer1=request.POST['Often']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()  
        return redirect('sexualspecific2')
    elif 'Everyday' in request.POST:
        specificanswer1=request.POST['Everyday']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()    
        return redirect('sexualspecific2')
         
   
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    patient.specificquestion1="How often do you wake to urinate 2 or more times at night"
    patient.save()

    return render(request,'sexualspecific1.html',{'patient_question1':patient.question1})


def sexualspecific2(request):

    if 'Poor flow of urine or slow stream' in request.POST:
        specificanswer2=request.POST['Poor flow of urine or slow stream']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()   
        return redirect('sexualspecific3')
    elif 'Feeling incomplete bladder emptying' in request.POST:
        specificanswer2=request.POST['Feeling incomplete bladder emptying']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()   
        return redirect('sexualspecific3')
    elif 'Straining to pass urine' in request.POST:
        specificanswer2=request.POST['Straining to pass urine']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()   
    elif 'None' in request.POST:
        specificanswer2=request.POST['None']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()  
        return redirect('sexualspecific3')
    elif 'Never' in request.POST:
        specificanswer2=request.POST['Never']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()  
        return redirect('sexualspecific3')
    elif 'Recently' in request.POST:
        specificanswer2=request.POST['Recently']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()  
        return redirect('sexualspecific3')
    elif 'More than 3 years back' in request.POST:
        specificanswer2=request.POST['More than 3 years back']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()  
        return redirect('sexualspecific3')


  
         
   
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.gender == "Male":
        patient.specificquestion2="Do you have any of these symptoms"
    else:
        patient.specificquestion2="When was the last time you got your PAP smear done"
    patient.save()

    return render(request,'sexualspecific2.html',{'patient_specificquestion2':patient.specificquestion2,'patient_gender':patient.gender})


def sexualspecific3(request):

    if 'Low' in request.POST:
        specificanswer3=request.POST['Low']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()   
        return redirect('sexualspecific5')
    elif 'Moderate' in request.POST:
        specificanswer3=request.POST['Moderate']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()  
        return redirect('sexualspecific5')
    elif 'High' in request.POST:
        specificanswer3=request.POST['High']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()  
        return redirect('sexualspecific5') 
    elif 'I am having regular periods without any issues' in request.POST:
        specificanswer3=request.POST['I am having regular periods without any issues']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()  
        return redirect('sexualspecific7') 
    elif 'I have menstrual cramps during periods' in request.POST:
        specificanswer3=request.POST['I have menstrual cramps during periods']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()  
        return redirect('sexualspecific7') 
    elif 'I experience heavy bleeding' in request.POST:
        specificanswer3=request.POST['I experience heavy bleeding']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()  
        return redirect('sexualspecific7') 
    elif 'My periods are irregular' in request.POST:
        specificanswer3=request.POST['My periods are irregular']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()  
        return redirect('sexualspecific7') 
    elif 'I am pregnant' in request.POST:
        specificanswer3=request.POST['I am pregnant']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()  
        return redirect('sexualspecific7') 
    elif 'My last pregnency ended in past 2 months or I am nursing' in request.POST:
        specificanswer3=request.POST['My last pregnency ended in past 2 months or I am nursing']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()  
        return redirect('sexualspecific7') 
    elif 'My periods stopped on their own  (I had menopause)' in request.POST:
        specificanswer3=request.POST['My periods stopped on their own  (I had menopause)']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()  
        return redirect('sexualspecific7') 

    


    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.gender=="Male":
        patient.specificquestion3="How would you rate your sexual desire?"
    else:
        patient.specificquestion3="At present, which statement best describes your menstrual cycle"
    patient.save()

    return render(request,'sexualspecific3.html',{'patient_specificquestion3':patient.specificquestion3,'patient_gender':patient.gender})



def sexualspecific5(request):
    if "Can't achieve full erection" in request.POST:
        specificanswer5=request.POST["Can't achieve full erection"]
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer5=specificanswer5
        patient.save()   
        return redirect('sexualspecific6')
    elif 'Can you achieve orgasm' in request.POST:
        specificanswer5=request.POST['Can you achieve orgasm']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer5=specificanswer5
        patient.save()   
        return redirect('sexualspecific6')
    elif 'Do you have premature ejaculation' in request.POST:
        specificanswer5=request.POST['Do you have premature ejaculation']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer5=specificanswer5
        patient.save()   
        return redirect('sexualspecific6')
    elif 'None' in request.POST:
        specificanswer5=request.POST['None']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer5=specificanswer5
        patient.save()   
        return redirect('sexualspecific6')


    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    patient.specificquestion5="During sexual intercourse"
    patient.save()

    return render(request,'sexualspecific5.html',{'patient_specificquestion5':patient.specificquestion5,'patient_question1':patient.question1})



def sexualspecific6(request):
    if 'Yes' in request.POST:
        specificanswer6=request.POST['Yes']
        print("his")
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer6=specificanswer6
        patient.save()   
        return redirect('sexualspecific7')
    elif 'No' in request.POST:
        specificanswer6=request.POST['No']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer6=specificanswer6
        patient.save()   
        return redirect('sexualspecific7')


    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    patient.specificquestion6="Do you think there is emotional cause to any of these"
    patient.save()

    return render(request,'sexualspecific6.html',{'patient_specificquestion6':patient.specificquestion6,'patient_question1':patient.question1})


def sexualspecific7(request):
    if 'Unusual itching or swelling of the genital area' in request.POST:
        specificanswer7=request.POST['Unusual itching or swelling of the genital area']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()   
        return redirect('sexualspecific8')
    elif 'Soreness or discharge from penis' in request.POST:
        specificanswer7=request.POST['Soreness or discharge from penis']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()   
        return redirect('sexualspecific8')
    elif 'Burning or itching sensation while urinating' in request.POST:
        specificanswer7=request.POST['Burning or itching sensation while urinating']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()   
        return redirect('sexualspecific8')
    elif 'Soreness or discharge from penis' in request.POST:
        specificanswer7=request.POST['Soreness or discharge from penis']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()   
        return redirect('sexualspecific8')
    elif 'Soreness or discharge from penis' in request.POST:
        specificanswer7=request.POST['Soreness or discharge from penis']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()   
        return redirect('sexualspecific8')
    elif 'None' in request.POST:
        specificanswer7=request.POST['None']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()   
        return redirect('sexualspecific8')
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    patient.specificquestion7="Do you have any of the following symptoms"
    patient.save()

    return render(request,'sexualspecific7.html',{'patient_specificquestion7':patient.specificquestion7,'patient_question1':patient.question1})


def sexualspecific8(request):
    if 'Yes' in request.POST:
        specificanswer8=request.POST['Yes']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer8=specificanswer8
        patient.save()   
        return redirect('sexualspecific9')
    elif 'No' in request.POST:
        specificanswer8=request.POST['No']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer8=specificanswer8
        patient.save()   
        return redirect('sexualspecific9')


    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    patient.specificquestion8="Have you had unprotected sexual act in past 6  months (other than partner)"
    patient.save()

    return render(request,'sexualspecific8.html',{'patient_question1':patient.question1})


def sexualspecific9(request):
    if 'Yes' in request.POST:
        specificanswer9=request.POST['Yes']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer9=specificanswer9
        patient.save()   
        return redirect('sexualspecific10')
    elif 'No' in request.POST:
        specificanswer9=request.POST['No']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer9=specificanswer9
        patient.save()   
        return redirect('result')


    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    patient.specificquestion9="Are you planning a family soon?"
    patient.save()

    return render(request,'sexualspecific9.html',{'patient_question1':patient.question1})


def sexualspecific10(request):
    if '6months' in request.POST:
        specificanswer10=request.POST['6months']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer10=specificanswer10
        patient.save()   
        return redirect('result')
    elif '6months to 1 year' in request.POST:
        specificanswer10=request.POST['6months to 1 year']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer10=specificanswer10
        patient.save()   
        return redirect('result')
    elif '1 year' in request.POST:
        specificanswer10=request.POST['1 year']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer10=specificanswer10
        patient.save()   
        return redirect('result')

    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    patient.specificquestion10="How long have you and your partner been trying to concieve with unprotected intercourse?"
    patient.save()

    return render(request,'sexualspecific10.html',{'patient_question1':patient.question1})


def specific1(request):
    if 'Yes' in request.POST:
        specificanswer1=request.POST['Yes']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()   
        return redirect('result')
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    patient.specificquestion1=""
    patient.save()

    return render(request,'sexualspecific10.html',{'patient_question1':patient.question1})


def subgoal(request):

    if 'prob1' in request.POST:
        subg=request.POST['prob1'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.subgoal=subg
        patient.save()
        return redirect('question1')

    elif 'prob2' in request.POST:
        subg=request.POST['prob2'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.subgoal=subg
        patient.save()
        return redirect('question1')

    elif 'prob3' in request.POST:
        subg=request.POST['prob3'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.subgoal=subg
        patient.save()
        return redirect('question1')

    elif 'prob4' in request.POST:
        subg=request.POST['prob4'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.subgoal=subg
        patient.save()
        return redirect('question1')

    elif 'prob5' in request.POST:
        subg=request.POST['prob5'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.subgoal=subg
        patient.save()
        return redirect('question1')



     
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    print(patient.healthgoal)
    

    return render(request,'subgoal.html',{'patient_healthgoal':patient.healthgoal, 'patient_gender':patient.gender})
   


def question1(request):

    if 'option1' in request.POST:
        option=request.POST['option1'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        print(option)
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')
        elif patient.question1 == "Have you ever tested your hemoglobin in the past?":
            if patient.answer1=="Yes":
                return redirect('anemiaspecific1')
            elif patient.answer1=="No":
                return redirect('question2')

        elif patient.question1 == "Where is your pain located?":
            return redirect('question2')
        elif patient.question1 == "When was your condition diagnosed":
            return redirect('question2')
        elif patient.question1 == "Do you have?":
            return redirect('question2')
        elif patient.question1 == "When did you test positive for COVID":
            return redirect('question2')
        elif patient.question1 == "Do you have trouble falling or staying asleep?":
            return redirect('question2')
        elif patient.question1 == "Have you lost interest in hobbies/ activities":
            return redirect('question2')
        elif patient.question1 == "How would you describe your energy levels?":
            return redirect("result")
        else:
            pass
        return redirect('result')

    elif 'option2' in request.POST:
        option=request.POST['option2'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')
        elif patient.question1 == "Have you ever tested your hemoglobin in the past?":
            if patient.answer1=="Yes":
                return redirect('anemiaspecific1')
            elif patient.answer1=="No":
                return redirect('anemiaspecific2')
        elif patient.question1 == "When was your condition diagnosed":
            return redirect('question2')
        elif patient.question1 == "Do you have?":
            return redirect('question2')
        elif patient.question1 == "When did you test positive for COVID":
            return redirect('question2')
        elif patient.question1 == "Do you have trouble falling or staying asleep?":
            return redirect('question2')
        elif patient.question1 == "Have you lost interest in hobbies/ activities":
            return redirect('question2')
        elif patient.question1 == "How would you describe your energy levels?":
            return redirect("result")
        else:
            pass
        return redirect('result')
    
    elif 'option3' in request.POST:
        option=request.POST['option3'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')

        elif patient.question1 == "When was your condition diagnosed":
            return redirect('question2')
        elif patient.question1 == "Do you have?":
            return redirect('question2')
        elif patient.question1 == "When did you test positive for COVID":
            return redirect('question2')
        elif patient.question1 == "Do you have trouble falling or staying asleep?":
            return redirect('question2')
        elif patient.question1 == "How would you describe your energy levels?":
            return redirect("result")
        else:
            pass
        return redirect('result')

    elif 'option4' in request.POST:
        option=request.POST['option4'] 

        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')
        elif patient.question1 == "When did you test positive for COVID":
            return redirect('question2')
        elif patient.question1 == "Do you have trouble falling or staying asleep?":
            return redirect('question2')
        elif patient.question1 == "How would you describe your energy levels?":
            return redirect("result")
        else:
            pass
        return redirect('result')

    elif 'option5' in request.POST:
        option=request.POST['option5'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')
        else:
            pass
        return redirect('result')

    elif 'option6' in request.POST:
        option=request.POST['option6'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')  
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')  
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')
        elif patient.question1 == "Do you have trouble falling or staying asleep?":
            return redirect('question2')
        else:
            pass
        return redirect('result')
       

    elif 'option7' in request.POST:
        option=request.POST['option7'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')
        else:
            pass
        return redirect('result')

    elif 'option8' in request.POST:
        option=request.POST['option8'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')
        else:
            pass
        return redirect('result')

    elif 'option9' in request.POST:
        option=request.POST['option9'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')
        else:
            pass
        return redirect('result')

    elif 'option10' in request.POST:
        option=request.POST['option10'] 
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer1=option
        patient.save()
        if patient.question1 == "Do you have any of the following respiratory symptoms?":
            return redirect('respiratoryspecific1')
        elif patient.question1 == "Do you have any of the following skin related symptoms?":
            return redirect('skinspecific1')
        elif patient.question1 == "Do you have any of the following gastrointestinal symptoms?":
            return redirect('foodspecific1')
        elif patient.question1 == "Do you have any of these symptoms?":
            return redirect('sexualspecific1')
        else:
            pass


        return redirect('result')

    

    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.subgoal=="Hair": 
        patient.question1="Hair Problem"
        patient.save()

    elif patient.subgoal=="Skin":
        patient.question1="Skin Problem"
        patient.save()

    elif patient.subgoal == "Respiratory":
        patient.question1 = "Do you have any of the following respiratory symptoms?"
        patient.save()

    elif patient.subgoal == "Skin Allergy":
        patient.question1= "Do you have any of the following skin related symptoms?"
        patient.save()

    elif patient.subgoal == "Food":
        print("yes")
        patient.question1= "Do you have any of the following gastrointestinal symptoms?"
        patient.save()

    elif patient.subgoal == "Sexual Well Being":
        print("yes")
        patient.question1= "Do you have any of these symptoms?"
        patient.save()
    

    elif patient.subgoal == "PCOS":
        patient.question1= "Are you facing any of the following issues:"
        patient.save()
        list3=[]
        global count
        count=0
        if 'optionn1' in request.POST:
            optione=request.POST['optionn1'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer1=list4
            patient.save()
            count=count+1
        if 'optionn2' in request.POST:
            optione=request.POST['optionn2'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer1=list4
            patient.save()
            count=count+1
        if 'optionn3' in request.POST:
            optione=request.POST['optionn3'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer1=list4
            patient.save()
            count=count+1
        if 'optionn4' in request.POST:
            optione=request.POST['optionn4'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer1=list4
            patient.save()
            count=count+1
        if 'optionn5' in request.POST:
            optione=request.POST['optionn5'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer1=list4
            patient.save()
            count=count+1
        if 'optionn6' in request.POST:
            optione=request.POST['optionn6'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer1=list4
            patient.save()
            count=count+1
        if "submit" in request.POST:
            return redirect('result')
            

    elif patient.subgoal == "Anemia":
        patient.question1= "Have you ever tested your hemoglobin in the past?"
       
        patient.save()

    elif patient.subgoal == "Bone Pain":
        patient.question1= "Where is your pain located?"
        patient.save()

    elif patient.subgoal == "Hypertension and Diabetes":
        patient.question1= "Do you have?"
        patient.save()

    elif patient.subgoal == "Post Covid":
        print("hi")
        patient.question1 = "When did you test positive for COVID"
        patient.save()
        
    elif patient.subgoal == "Sleep":
        patient.question1= "Do you have trouble falling or staying asleep?"
        patient.save()

    elif patient.subgoal == "Mood":
        patient.question1= "Have you lost interest in hobbies/ activities"
        patient.save()
    elif patient.healthgoal == "fitness":
        patient.question1= "How would you describe your energy levels?"
        patient.save()
    elif patient.healthgoal == "Gut Improvement":
        patient.question1= "Which of the following symptoms best describe your problem?"
        patient.save()
        



    return render(request,'question1.html',{'patient_subgoal':patient.subgoal,'patient_question1':patient.question1,'patient_healthgoal':patient.healthgoal})



def question2(request):
    if 'option1' in request.POST:
        answer2=request.POST['option1']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option2' in request.POST:
        answer2=request.POST['option2']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option3' in request.POST:
        answer2=request.POST['option3']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option4' in request.POST:
        answer2=request.POST['option4']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option5' in request.POST:
        answer2=request.POST['option5']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option6' in request.POST:
        answer2=request.POST['option6']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option7' in request.POST:
        answer2=request.POST['option7']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option8' in request.POST:
        answer2=request.POST['option8']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option8' in request.POST:
        answer2=request.POST['option8']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option9' in request.POST:
        answer2=request.POST['option9']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    if 'option10' in request.POST:
        answer2=request.POST['option10']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.answer2=answer2
        patient.save()
        return redirect('specific1')
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.subgoal == "Bone Pain":
        patient.question2="Which sides are involved"
    elif patient.subgoal == "Hypertension and Diabetes":
        patient.question2="When was your condition diagnosed"
    elif patient.subgoal == "Post Covid":
        patient.question2="Do you have any of the following?"
        patient.save()
        list3=[]
        global count1
        count1=0
        if 'optionn1' in request.POST:
            optione=request.POST['optionn1'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            print("hi")
            count1=count1+1
        if 'optionn2' in request.POST:
            optione=request.POST['optionn2'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            count1=count1+1
        if 'optionn3' in request.POST:
            optione=request.POST['optionn3'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            count1=count1+1
        if 'optionn4' in request.POST:
            optione=request.POST['optionn4'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            count1=count1+1
        if 'optionn5' in request.POST:
            optione=request.POST['optionn5'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            count1=count1+1
        if 'optionn6' in request.POST:
            optione=request.POST['optionn6'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            count1=count1+1
        if 'optionn7' in request.POST:
            optione=request.POST['optionn7'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            count1=count1+1
        if 'optionn8' in request.POST:
            optione=request.POST['optionn8'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            count1=count1+1
        if 'optionn9' in request.POST:
            optione=request.POST['optionn9'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            count1=count1+1
        if 'optionn10' in request.POST:
            optione=request.POST['optionn10'] 
            list3.append(optione)
            list4=str(list3)
            print(list4)
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.answer2=list4
            patient.save()
            count1=count1+1
        if "submit" in request.POST:
            return redirect('result')

    elif patient.subgoal == "Sleep":
        patient.question2="Do you take anything to help you sleep"
    elif patient.subgoal == "Mood":
        patient.question2="Do you feel sad/ irritable or hopeless"
    patient.save()
    return render(request,'question2.html',{'patient_subgoal':patient.subgoal,'patient_question2':patient.question2,'patient_healthgoal':patient.healthgoal})

def specific1(request):
    if 'option1' in request.POST:
        specificanswer1=request.POST['option1']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()
        if patient.subgoal=="Bone Pain":
            return redirect('specific2')
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific2")
        else:
            return redirect('result')
    if 'option2' in request.POST:
        specificanswer1=request.POST['option2']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()
        if patient.subgoal=="Bone Pain":
            return redirect('specific2')
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific2")
        else:
            return redirect('result') 
    if 'option3' in request.POST:
        specificanswer1=request.POST['option3']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()
        if patient.subgoal=="Bone Pain":
            return redirect('specific2')
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific2")
        else:
            return redirect('result')
    if 'option4' in request.POST:
        specificanswer1=request.POST['option4']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()
        if patient.subgoal=="Bone Pain":
            return redirect('specific2')
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific2")
        else:
            return redirect('result')
    if 'option5' in request.POST:
        specificanswer1=request.POST['option5']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=specificanswer1
        patient.save()
        if patient.subgoal=="Bone Pain":
            return redirect('specific2')
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific2")
        else:
            return redirect('result')
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.subgoal == "Bone Pain":
        patient.specificquestion1="How long you had symptoms"
    elif patient.subgoal == "Hypertension and Diabetes":
        patient.specificquestion1="Are you taking medicine for diabetes/ hypertension"
    elif patient.subgoal == "Post Covid":
        patient.specificquestion1="Please tick the most appropriate option "
    elif patient.subgoal == "Sleep":
        patient.specificquestion1="Are you a shift worker/ have irregular sleep schedule?"
    elif patient.subgoal == "Mood":
        patient.specificquestion1="Do you feel nervous or worried"
    patient.save()
    
    return render(request,'specific1.html',{'patient_subgoal':patient.subgoal,'patient_specificquestion1':patient.specificquestion1,'patient_healthgoal':patient.healthgoal})

def specific2(request):
    if "pain" in request.POST:
        pain=request.POST['pain']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="On a scale of 1 to 10 ( 1 being minimal and 10 being severe), what is your level of pain"
        patient.specificanswer2=pain
        patient.save()
        return redirect('result')
    elif 'option1' in request.POST:
        specificanswer2=request.POST['option1']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()
        if patient.subgoal == "Sleep":
            return redirect("specific3")
        elif patient.subgoal == "Mood":
            return redirect("result")
        else:
            return redirect('result')
    elif 'option2' in request.POST:
        specificanswer2=request.POST['option2']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()
        if patient.subgoal == "Sleep":
            return redirect("specific3")
        elif patient.subgoal == "Mood":
            return redirect("result")
        else:
            return redirect('result')

    elif 'option3' in request.POST:
        specificanswer2=request.POST['option3']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()
        if patient.subgoal == "Sleep":
            return redirect("specific3")
        elif patient.subgoal == "Mood":
            return redirect("result")
        else:
            return redirect('result')

    elif 'option4' in request.POST:
        specificanswer2=request.POST['option4']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()
        if patient.subgoal == "Sleep":
            return redirect("specific3")
        elif patient.subgoal == "Mood":
            return redirect("result")
        else:
            return redirect('result')
    elif 'option5' in request.POST:
        specificanswer2=request.POST['option5']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer2=specificanswer2
        patient.save()
        if patient.subgoal == "Sleep":
            return redirect("specific3")
        elif patient.subgoal == "Mood":
            return redirect("result")
        else:
            return redirect('result')
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.subgoal == "Bone Pain":
        patient.specificquestion2="On a scale of 1 to 10 ( 1 being minimal and 10 being severe), what is your level of pain"
    if patient.subgoal == "Sleep":
        patient.specificquestion2="Do you have any unusual behavior/ movements during sleep?"
    if patient.subgoal == "Mood":
        patient.specificquestion2="Has there ever been a period of time when you"
    patient.save()

    return render(request,'specific2.html',{'patient_subgoal':patient.subgoal,'patient_healthgoal':patient.healthgoal,'patient_specificquestion2':patient.specificquestion2})


def specific3(request):

    if 'option1' in request.POST:
        specificanswer3=request.POST['option1']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific4")
        else:
            return redirect('result')
    elif 'option2' in request.POST:
        specificanswer3=request.POST['option2']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific4")
        else:
            return redirect('result')

    elif 'option3' in request.POST:
        specificanswer3=request.POST['option3']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific4")
        else:
            return redirect('result')

    elif 'option4' in request.POST:
        specificanswer3=request.POST['option4']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific4")
        else:
            return redirect('result')
    elif 'option5' in request.POST:
        specificanswer3=request.POST['option5']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer3=specificanswer3
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific4")
        else:
            return redirect('result')

    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.subgoal == "Sleep":
        patient.specificquestion3="Do you snore during sleep?"
    if patient.subgoal == "Mood":
        patient.specificquestion3="Has there ever been a period of time when you"
    patient.save()

    return render(request,'specific3.html',{'patient_subgoal':patient.subgoal,'patient_healthgoal':patient.healthgoal,'patient_specificquestion3':patient.specificquestion3})

def specific4(request):

    if 'option1' in request.POST:
        specificanswer5=request.POST['option1']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer5=specificanswer5
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific5")
        else:
            return redirect('result')
    elif 'option2' in request.POST:
        specificanswer5=request.POST['option2']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer5=specificanswer5
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific5")
        else:
            return redirect('result')

    elif 'option3' in request.POST:
        specificanswer5=request.POST['option3']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer5=specificanswer5
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific5")
        else:
            return redirect('result')

    elif 'option4' in request.POST:
        specificanswer5=request.POST['option4']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer5=specificanswer5
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific5")
        else:
            return redirect('result')

    elif 'option5' in request.POST:
        specificanswer5=request.POST['option5']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer5=specificanswer5
        patient.save()
        if patient.healthgoal == "Augument quality of sleep and elevate mood":
            return redirect("specific5")
        else:
            return redirect('result')

    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.healthgoal == "Augument quality of sleep and elevate mood":
        patient.specificquestion5="Do you have difficulty in staying awake during the day?"
    patient.save()

    return render(request,'specific4.html',{'patient_subgoal':patient.subgoal,'patient_healthgoal':patient.healthgoal,'patient_specificquestion5':patient.specificquestion5})

def specific5(request):

    if 'option1' in request.POST:
        specificanswer6=request.POST['option1']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer6=specificanswer6
        patient.save()
        return redirect('specific6')
    elif 'option2' in request.POST:
        specificanswer6=request.POST['option2']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer6=specificanswer6
        patient.save()
        return redirect('specific6')

    elif 'option3' in request.POST:
        specificanswer6=request.POST['option3']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer6=specificanswer6
        patient.save()
        return redirect('specific6')

    elif 'option4' in request.POST:
        specificanswer6=request.POST['option4']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer6=specificanswer6
        patient.save()
        return redirect('specific6')
    elif 'option5' in request.POST:
        specificanswer6      =request.POST['option5']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer6=specificanswer6
        patient.save()
        return redirect('specific6')

    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.healthgoal == "Augument quality of sleep and elevate mood":
        patient.specificquestion6="Are your legs restless or uncomfortable before bed?"
    patient.save()

    return render(request,'specific5.html',{'patient_subgoal':patient.subgoal,'patient_healthgoal':patient.healthgoal,'patient_specificquestion6':patient.specificquestion6})


def specific6(request):

    if 'option1' in request.POST:
        specificanswer7=request.POST['option1']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()
        return redirect('specific7')
    elif 'option2' in request.POST:
        specificanswer7=request.POST['option2']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()
        return redirect('specific7')

    elif 'option3' in request.POST:
        specificanswer7=request.POST['option3']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()
        return redirect('specific7')

    elif 'option4' in request.POST:
        specificanswer7=request.POST['option4']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()
        return redirect('specific7')
    elif 'option5' in request.POST:
        specificanswer7=request.POST['option5']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer7=specificanswer7
        patient.save()
        return redirect('specific7')

    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.healthgoal == "Augument quality of sleep and elevate mood":
        patient.specificquestion7="How often do you wake to urinate 2 or more times at night"
    patient.save()

    return render(request,'specific6.html',{'patient_subgoal':patient.subgoal,'patient_healthgoal':patient.healthgoal,'patient_specificquestion7':patient.specificquestion7})

def specific7(request):

    if 'option1' in request.POST:
        specificanswer8=request.POST['option1']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer8=specificanswer8
        patient.save()
        return redirect('result')
    elif 'option2' in request.POST:
        specificanswer8=request.POST['option2']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer8=specificanswer8
        patient.save()
        return redirect('result')

    elif 'option3' in request.POST:
        specificanswer8=request.POST['option3']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer8=specificanswer8
        patient.save()
        return redirect('result')

    elif 'option4' in request.POST:
        specificanswer8=request.POST['option4']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer8=specificanswer8
        patient.save()
        return redirect('result')
    elif 'option5' in request.POST:
        specificanswer8=request.POST['option5']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer8=specificanswer8
        patient.save()
        return redirect('result')

    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    if patient.healthgoal == "Augument quality of sleep and elevate mood":
        patient.specificquestion8="How likely are you to doze off or fall asleep in following situations:"
    patient.save()

    return render(request,'specific7.html',{'patient_subgoal':patient.subgoal,'patient_healthgoal':patient.healthgoal,'patient_specificquestion8':patient.specificquestion8})

def respiratoryspecific1(request):
    if 'Grass' in request.POST:
        specificanswer1=request.POST['Grass']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')
    if 'House Dust' in request.POST:
        specificanswer1=request.POST['House Dust']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')

    if 'Hay' in request.POST:
        specificanswer1=request.POST['Hay']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')

    if 'Cats' in request.POST:
        specificanswer1=request.POST['Cats']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')

    if 'Dogs' in request.POST:
        specificanswer1=request.POST['Dogs']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')

    if 'Moulds' in request.POST:
        specificanswer1=request.POST['Moulds']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')

    if 'Basement or Damp Area' in request.POST:
        specificanswer1=request.POST['Basement or Damp Area']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')
    if 'Pollution or Smoke' in request.POST:
        specificanswer1=request.POST['Pollution or Smoke']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')

    if 'Weather Changes' in request.POST:
        specificanswer1=request.POST['Weather Changes']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')

    if 'Exercise' in request.POST:
        specificanswer1=request.POST['Exercise']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')

    if 'Any Other' in request.POST:
        specificanswer1=request.POST['Any Other']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('respiratoryspecific2')


    return render(request,'respiratoryspecific1.html')

def respiratoryspecific2(request):
    if 'Yes' in request.POST:
        specificanswer2=request.POST['Yes']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="Do other people in your family have a similar condition?"
        patient.specificanswer2=specificanswer2
        patient.save()
        return redirect('result')
    if 'No' in request.POST:
        specificanswer2=request.POST['No']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="Do other people in your family have a similar condition?"
        patient.specificanswer2=specificanswer2
        patient.save()
        return redirect('result')
    return render(request,'respiratoryspecific2.html')

def skinspecific1(request):
    if 'egg' in request.POST:
        specificanswer1=request.POST['egg']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')


    if 'milk' in request.POST:
        specificanswer1=request.POST['milk']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')


    if 'dust mites' in request.POST:
        specificanswer1=request.POST['dust mites']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')

    if 'wheat' in request.POST:
        specificanswer1=request.POST['wheat']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')

    if 'rice' in request.POST:
        specificanswer1=request.POST['rice']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')

    if 'soya bean' in request.POST:
        specificanswer1=request.POST['soya bean']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')

    if 'peanut' in request.POST:
        specificanswer1=request.POST['peanut']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')

    if 'chicken' in request.POST:
        specificanswer1=request.POST['chicken']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')


    if 'sea food' in request.POST:
        specificanswer1=request.POST['chicken']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')

    if 'any other' in request.POST:
        specificanswer1=request.POST['chicken']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Choose any of the following which seems to trigger or cause the above symptoms"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('skinspecific2')
    
    return render(request,'skinspecific1.html')


def skinspecific2(request):
    if 'Yes' in request.POST:
        specificanswer2=request.POST['Yes']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="Do other people in your family have a similar condition?"
        patient.specificanswer2=specificanswer2
        patient.save()
        return redirect('result')
    if 'No' in request.POST:
        specificanswer2=request.POST['No']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="Do other people in your family have a similar condition? "
        patient.specificanswer2=specificanswer2
        patient.save()
        return redirect('result')
    return render(request,'skinspecific2.html')

def anemiaspecific1(request):
    if '>13' in request.POST:
        hb=request.POST['>13']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=hb
        patient.save()
        return redirect('anemiaspecific2')
    if '11-12.9' in request.POST:
        hb=request.POST['11-12.9']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=hb
        patient.save()
        return redirect('anemiaspecific2')
    if '8-10.9' in request.POST:
        hb=request.POST['8-10.9']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=hb
        patient.save()
        return redirect('anemiaspecific2')
    if 'less than 8' in request.POST:
        hb=request.POST['less than 8']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificanswer1=hb
        patient.save()
        return redirect('anemiaspecific2')
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    patient.specificquestion1="What is your Hb?"
    patient.save()
    return render(request,'anemiaspecific1.html')

def anemiaspecific2(request):
    if 'Yes' in request.POST:
        specificanswer2=request.POST['Yes']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="Are you taking  Fe, Vit B12 or folate supplements?"
        patient.specificanswer2=specificanswer2
        patient.save()
        return redirect('anemiaspecific3')
    if 'No' in request.POST:
        specificanswer2=request.POST['No']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="Are you taking  Fe, Vit B12 or folate supplements?"
        patient.specificanswer2=specificanswer2
        patient.save()
        return redirect('anemiaspecific3')
    return render(request,'anemiaspecific2.html')

def anemiaspecific3(request):
    if 'Yes' in request.POST:
        specificanswer3=request.POST['Yes']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion3="Do you have anyone in your family who has thallesemia minor"
        patient.specificanswer3=specificanswer3
        patient.save()
        return redirect('result')
    if 'No' in request.POST:
        specificanswer3=request.POST['No']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion3="Do you have anyone in your family who has thallesemia minor"
        patient.specificanswer3=specificanswer3
        patient.save()
        return redirect('result')
    return render(request,'anemiaspecific3.html')


def foodspecific1(request):
    if 'Yes' in request.POST:
        specificanswer1=request.POST['Yes']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Are you suffering from any chronic/ autoimmune condition"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('foodspecific2')
    if 'No' in request.POST:
        specificanswer1=request.POST['No']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion1="Are you suffering from any chronic/ autoimmune condition"
        patient.specificanswer1=specificanswer1
        patient.save()
        return redirect('foodspecific2')
    return render(request,'foodspecific1.html')


def foodspecific2(request):
    if 'within 30 min of exposure' in request.POST:
        specificanswer2=request.POST['within 30 min of exposure']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="Do you feel that your symptoms appear"
        patient.specificanswer2=specificanswer2
        patient.save()
        return redirect('result')
    if '30 min to 2hours of exposure' in request.POST:
        specificanswer2=request.POST['30 min to 2hours of exposure']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="Do you feel that your symptoms appear "
        patient.specificanswer2=specificanswer2
        patient.save()
        return redirect('result')
    if '>2hours of exposure' in request.POST:
        specificanswer2=request.POST['>2hours of exposure']
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.specificquestion2="Do you feel that your symptoms appear "
        patient.specificanswer2=specificanswer2
        patient.save()
        return redirect('result')
    return render(request,'foodspecific2.html')





def result(request):
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)
    list=[]
    #HAIR PROBLEM
    if patient.question1 == "Hair Problem":
        if patient.answer1=='Hairfall':
            test=Test.objects.all()
            list.append(str(test[4]))
            list.append(str(test[21]))
            list.append(str(test[30]))
            list.append(str(test[31]))
            list.append(str(test[43]))
            list.append(str(test[33]))
            list.append(str(test[11]))
            list.append(str(test[34]))
            list.append(str(test[9]))
            list.append(str(test[10]))
            list.append(str(test[38]))
            list.append(str(test[36]))
            list.append(str(test[39]))
            list.append(str(test[29]))
            list.append(str(test[32]))
            list.append(str(test[35]))
            list.append(str(test[37]))
            list.append(str(test[8]))
            if patient.gender == 'Female':
                list.append(str(test[102]))
                list.append(str(test[40]))
                list.append(str(test[41]))
                list.append(str(test[42]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        if patient.answer1=='Premature Graying':
            test=Test.objects.all()
            list.append(str(test[4]))
            list.append(str(test[21]))
            list.append(str(test[30]))
            list.append(str(test[43]))
            list.append(str(test[9]))
            list.append(str(test[10]))
            list.append(str(test[38]))
            list.append(str(test[39]))
            list.append(str(test[29]))
            list.append(str(test[32]))
            list.append(str(test[46]))
            list.append(str(test[11]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        if patient.answer1=='Dandruff/Split Ends':
            test=Test.objects.all()
            list.append(str(test[30]))
            list.append(str(test[43]))
            list.append(str(test[9]))
            list.append(str(test[10]))
            list.append(str(test[38]))
            list.append(str(test[39]))
            list.append(str(test[29]))
            list.append(str(test[32]))
            list.append(str(test[11]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    #SKIN PROBLEM
    if patient.question1 == "Skin Problem":
        if patient.answer1=='Acne':
            test=Test.objects.all()
            list.append(str(test[102]))
            list.append(str(test[33]))
            list.append(str(test[26]))
            list.append(str(test[36]))
            list.append(str(test[40]))
            list.append(str(test[41]))
            list.append(str(test[42]))
            list.append(str(test[44]))
            list.append(str(test[45]))
            list.append(str(test[46]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        if patient.answer1=='Eczema':
            test=Test.objects.all()
            list.append(str(test[47]))
            list.append(str(test[48]))
            if patient.age <=13 :
                list.append(str(test[49]))
            list.append(str(test[46]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        if patient.answer1=='Hives or Uticaria':
            test=Test.objects.all()
            list.append(str(test[47]))
            list.append(str(test[48]))
            if patient.age <=13 :
                list.append(str(test[49]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        if patient.answer1=='Rashes':
            test=Test.objects.all()
            list.append(str(test[47]))
            list.append(str(test[48]))
            if patient.age <=13 :
                list.append(str(test[49]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        if patient.answer1=='Vitiligo':
            test=Test.objects.all()
            list.append(str(test[47]))
            list.append(str(test[48]))
            if patient.age <=13 :
                list.append(str(test[49]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    #RESPIRATORY PROBLEM
    if patient.question1 == "Do you have any of the following respiratory symptoms?":
            test=Test.objects.all()
            list.append(str(test[47]))
            list.append(str(test[48]))
            if patient.age <=13 :
                list.append(str(test[49]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()

    #SKIN ALLERGY
    if patient.question1 == "Do you have any of the following skin related symptoms?":
        test=Test.objects.all()
        list.append(str(test[47]))
        list.append(str(test[48]))
        if patient.age <=13 :
            list.append(str(test[49]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    #FOODALLERGY
    
    if patient.specificanswer2 == "within 30 min of exposure":
        test=Test.objects.all()
        list.append(str(test[48]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    elif patient.specificanswer2 == "30 min to 2hours of exposure":
        test=Test.objects.all()
        list.append(str(test[48]))
        list.append(str(test[46]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    elif patient.specificanswer2 == ">2hours of exposure":
        test=Test.objects.all()
        list.append(str(test[46]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    #SEXUAL MALE
    if patient.question1 == "Do you have any of these symptoms?":
        test=Test.objects.all()
        list.append(str(test[27]))
        list.append(str(test[103]))
        list.append(str(test[4]))
        list.append(str(test[7]))
        if patient.age >=50:
            list.append(str(test[60]))

        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    if patient.specificanswer1 == "Often" or patient.specificanswer1=="Everyday":
        test=Test.objects.all()
        list.append(str(test[23]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.specificanswer3 == "Low":
        test=Test.objects.all()
        list.append(str(test[35]))
        list.append(str(test[102]))
        list.append(str(test[33]))
        list.append(str(test[55]))
        list.append(str(test[59]))
        list.append(str(test[52]))
        list.append(str(test[30]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    elif patient.specificanswer3 == "High":
        test=Test.objects.all()
        list.append(str(test[35]))
        list.append(str(test[102]))
        list.append(str(test[55]))
       
        list.append(str(test[52]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.specificanswer5 == "Can't achieve full erection":
        test=Test.objects.all()
        list.append(str(test[35]))
        list.append(str(test[102]))
        list.append(str(test[55]))
        list.append(str(test[59]))
        list.append(str(test[52]))
        list.append(str(test[25]))
        list.append(str(test[24]))
        list.append(str(test[23]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    elif patient.specificanswer5 == "Can you achieve orgasm":
        test=Test.objects.all()
        list.append(str(test[35]))
        list.append(str(test[102]))
        list.append(str(test[55]))
        list.append(str(test[59]))
        list.append(str(test[23]))
        list.append(str(test[29]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    elif patient.specificanswer5 == "Do you have premature ejaculation":
        test=Test.objects.all()
        list.append(str(test[35]))
        list.append(str(test[102]))
        list.append(str(test[55]))
        list.append(str(test[59]))
        list.append(str(test[23]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    if patient.specificanswer7 !="None":
        test=Test.objects.all()
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    if patient.specificanswer8 =="Yes":
        test=Test.objects.all()
        list.append(str(test[65]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    if patient.specificanswer9 =="Yes":
        test=Test.objects.all()
        list.append(str(test[4]))
        list.append(str(test[73]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    if patient.specificanswer10 =="6months to 1 year":
        test=Test.objects.all()
        list.append(str(test[104]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.specificanswer10 =="1 year":
        test=Test.objects.all()
        list.append(str(test[67]))
        list.append(str(test[35]))
        list.append(str(test[67]))
        list.append(str(test[104]))
        list.append(str(test[40]))
        list.append(str(test[41]))
        list.append(str(test[42]))
        list.append(str(test[33]))
        if patient.gender == "Female":
            list.append(str(test[21]))
            list.append(str(test[4]))
            list.append(str(test[13]))
            list.append(str(test[45]))
            list.append(str(test[71]))
            list.append(str(test[42]))
            list.append(str(test[105]))

        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.specificquestion2 == "When was the last time you got your PAP smear done":
        if patient.specificanswer2=="Never" or patient.specificanswer2 == "More than 3 years back":
            if patient.age >=21 and patient.age <=65:
                test=Test.objects.all()
                list.append(str(test[69]))
                pk_id=request.session.get("pk_id")
                patient=Patient.objects.get(patient_id=pk_id)
                patient.tests=list
                patient.save()
    if patient.specificanswer3== "I have menstrual cramps during periods":
        Test.objects.all()
        list.append(str(test[65]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.specificanswer3== "I experience heavy bleeding":
        Test.objects.all()
        list.append(str(test[69]))
        list.append(str(test[31]))
        list.append(str(test[21]))
        list.append(str(test[30]))
        list.append(str(test[103]))
        list.append(str(test[55]))
        list.append(str(test[41]))
        list.append(str(test[40]))
        list.append(str(test[70]))
        list.append(str(test[45]))
        list.append(str(test[72]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.specificanswer3== "I have menstrual cramps during periods":
        Test.objects.all()
        list.append(str(test[69]))
        list.append(str(test[31]))
        list.append(str(test[21]))
        list.append(str(test[30]))
        list.append(str(test[103]))
        list.append(str(test[55]))
        list.append(str(test[41]))
        list.append(str(test[40]))
        list.append(str(test[70]))
        list.append(str(test[45]))
        list.append(str(test[71]))
        list.append(str(test[33]))

        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    if patient.specificanswer3== "I am pregnant":
        Test.objects.all()
        list.append(str(test[74]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.specificanswer3== "My last pregnency ended in past 2 months or I am nursing":
        Test.objects.all()
        list.append(str(test[4]))
        list.append(str(test[52]))
        list.append(str(test[4]))
        list.append(str(test[29]))
        list.append(str(test[42]))

        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.specificanswer3== "My periods stopped on their own  (I had menopause)":
        Test.objects.all()
        list.append(str(test[74]))
        list.append(str(test[21]))
        list.append(str(test[69]))
        list.append(str(test[83]))
        list.append(str(test[102]))
        list.append(str(test[55]))
        list.append(str(test[20]))
        list.append(str(test[40]))

        

        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    if patient.specificquestion7 == "Do you have any of the following symptoms":
        Test.objects.all()
        list.append(str(test[65]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    elif patient.specificquestion7 == "Do you have any of the following symptoms":
        Test.objects.all()
        list.append(str(test[65]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    if patient.specificanswer9=="Are you planning a family soon":
        Test.objects.all()
        list.append(str(test[4]))
        list.append(str(test[73]))
        if patient.gender == "Female":
            list.append(str(test[21]))
            list.append(str(test[43]))
            list.append(str(test[56]))
            list.append(str(test[11]))
            list.append(str(test[30]))
            list.append(str(test[29]))
            list.append(str(test[27]))
            list.append(str(test[13]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    
    if patient.question1=="Have you ever tested your hemoglobin in the past?":
        if patient.answer1 == "No":
            Test.objects.all()
            list.append(str(test[2]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()

    if patient.specificanswer1=="11-12.9":
        Test.objects.all()
        list.append(str(test[2]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    elif patient.specificanswer1=="8-10.9":
        Test.objects.all()
        list.append(str(test[3]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.specificquestion3=="Do you have anyone in your family who has thallesemia minor":
        if patient.specificanswer3 =="Yes":
            Test.objects.all()
            list.append(str(test[73]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()

    #BONE PAIN
    if patient.question1=="Where is your pain located?":
        if patient.answer1 == "Hip" or patient.answer1 == "Knee":
            Test.objects.all()
            list.append(str(test[4]))
            list.append(str(test[7]))
            list.append(str(test[8]))
            list.append(str(test[9]))
            list.append(str(test[10]))
            list.append(str(test[11]))
            list.append(str(test[12]))
            if patient.age >=60:
                list.append(str(test[106]))
        elif patient.answer1 == "Joints of fingers and toes":
            Test.objects.all()
            list.append(str(test[5]))
            list.append(str(test[12]))
            if patient.age >=60:
                list.append(str(test[106]))
        elif patient.answer1 == "Pain and stiffness in lower back and hips, especially in morning":
            Test.objects.all()
            list.append(str(test[4]))
            list.append(str(test[7]))
            list.append(str(test[8]))
            list.append(str(test[9]))
            list.append(str(test[10]))
            list.append(str(test[11]))
            list.append(str(test[12]))
            list.append(str(test[6]))
            if patient.age >=60:
                list.append(str(test[106]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    #hypertension
    if patient.question1=="Do you have?":
        if patient.answer1 == "Diabetes":
            Test.objects.all()
            list.append(str(test[22]))
            list.append(str(test[107]))
            list.append(str(test[107]))
            list.append(str(test[24]))
            list.append(str(test[25]))
            list.append(str(test[26]))
            list.append(str(test[27]))
            list.append(str(test[28]))
        if patient.answer1 == "Hypertension":
            Test.objects.all()
            list.append(str(test[24]))
            list.append(str(test[25]))
            list.append(str(test[26]))
            list.append(str(test[27]))
            list.append(str(test[28]))
        if patient.answer1 == "Both":
            Test.objects.all()
            list.append(str(test[15]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    #post covid
    if patient.question2=="Do you have any of the following?":
        if patient.answer1 == "Diabetes":
            Test.objects.all()
            list.append(str(test[22]))
            list.append(str(test[107]))
            list.append(str(test[107]))
            list.append(str(test[24]))
            list.append(str(test[25]))
            list.append(str(test[26]))
            list.append(str(test[27]))
            list.append(str(test[28]))
        if patient.answer1 == "Hypertension":
            Test.objects.all()
            list.append(str(test[24]))
            list.append(str(test[25]))
            list.append(str(test[26]))
            list.append(str(test[27]))
            list.append(str(test[28]))
        if patient.answer1 == "Both":
            Test.objects.all()
            list.append(str(test[15]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    if patient.question1=="Do you have trouble falling or staying asleep?":
        if patient.answer1 == "Often" or patient.answer1 == "Everyday":
            Test.objects.all()
            list.append(str(test[11]))
            list.append(str(test[53]))
            list.append(str(test[54]))
            list.append(str(test[43]))
            list.append(str(test[38]))
            list.append(str(test[39]))
            list.append(str(test[94]))
            list.append(str(test[29]))
            list.append(str(test[55]))
            if patient.gender == "Female":
                list.append(str(test[45]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    if patient.question2=="Do you take anything to help you sleep":
        if patient.answer2 == "Medication" or patient.answer2 == "Any other":
            Test.objects.all()
            list.append(str(test[11]))
            list.append(str(test[53]))
            list.append(str(test[54]))
            list.append(str(test[43]))
            list.append(str(test[38]))
            list.append(str(test[39]))
            list.append(str(test[94]))
            list.append(str(test[29]))
            list.append(str(test[55]))
            if patient.gender == "Female":
                list.append(str(test[45]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    if patient.specificquestion2=="Do you have any unusual behavior/ movements during sleep?":
        if patient.specificanswer2 == "Often" or patient.specificanswer2 == "Everyday":
            Test.objects.all()
            list.append(str(test[23]))
            list.append(str(test[29]))
            list.append(str(test[30]))
            list.append(str(test[59]))
            list.append(str(test[4]))
        
            if patient.gender == "Female":
                list.append(str(test[45]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    if patient.specificquestion5=="Do you have difficulty in staying awake during the day?":
        if patient.specificanswer5 == "Often" or patient.specificanswer5 == "Everyday":
            Test.objects.all()
            list.append(str(test[11]))
            list.append(str(test[53]))
            list.append(str(test[54]))
            list.append(str(test[43]))
            list.append(str(test[38]))
            list.append(str(test[39]))
            list.append(str(test[94]))
            list.append(str(test[29]))
            list.append(str(test[55]))
        
            if patient.gender == "Female":
                list.append(str(test[45]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    if patient.specificquestion6=="Are your legs restless or uncomfortable before bed?":
        if patient.specificanswer6 == "Often" or patient.specificanswer6 == "Everyday":
            Test.objects.all()
            list.append(str(test[23]))
            list.append(str(test[29]))
            list.append(str(test[30]))
            list.append(str(test[59]))
            list.append(str(test[4]))
        
            if patient.gender == "Female":
                list.append(str(test[45]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()

    if patient.specificquestion7 =="How often do you wake to urinate 2 or more times at night":
        if patient.specificanswer7 == "Often" or patient.specificanswer7 == "Everyday":
            Test.objects.all()
            list.append(str(test[23]))
            list.append(str(test[83]))
            list.append(str(test[85]))
            list.append(str(test[4]))
            list.append(str(test[27]))

        
            if patient.age >=50:
                list.append(str(test[60]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()

    if patient.specificquestion8 =="How likely are you to doze off or fall asleep in following situations:":
        Test.objects.all()
        list.append(str(test[11]))
        list.append(str(test[53]))
        list.append(str(test[54]))
        list.append(str(test[43]))
        list.append(str(test[38]))
        list.append(str(test[39]))
        list.append(str(test[94]))
        list.append(str(test[29]))
        list.append(str(test[55]))
        if patient.gender == "Female":
            list.append(str(test[45]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    if patient.subgoal == "Mood":
        Test.objects.all()
        list.append(str(test[4]))
        list.append(str(test[52]))
        list.append(str(test[50]))
        list.append(str(test[85]))
        list.append(str(test[43]))
        list.append(str(test[55]))
        list.append(str(test[25]))
        list.append(str(test[24]))
        list.append(str(test[62]))
        list.append(str(test[64]))
        list.append(str(test[23]))
        list.append(str(test[59]))
        list.append(str(test[38]))
        list.append(str(test[58]))
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    #PCOS
    if patient.question1 == "Are you facing any of the following issues:":
        Test.objects.all()
        if count>2:
            list.append(str(test[1]))
        elif count<=2:
            list.append(str(test[0]))
   
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    # POST COVID
    if patient.question2 == "Do you have any of the following?":
        Test.objects.all()

        if count1<2:
            list.append(str(test[16]))
            print(list)
        elif count1 >=2 and count1 <= 3:
            list.append(str(test[17]))
        elif count1>=3:
            list.append(str(test[17]))
            list.append(str(test[83]))

        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()
    # FITNESS
    if patient.healthgoal == "fitness":
        if patient.diet_answer == "veg":
            Test.objects.all()
            list.append(str(test[43]))
            list.append(str(test[11]))
            list.append(str(test[85]))
            list.append(str(test[29]))
            list.append(str(test[39]))
        elif patient.diet_answer == "nonveg":
            Test.objects.all()
            list.append(str(test[26]))
            list.append(str(test[92]))
            list.append(str(test[23]))
            list.append(str(test[43]))
            list.append(str(test[87]))
        elif patient.diet_answer == "Gluten Free":
            Test.objects.all()
            list.append(str(test[26]))
            list.append(str(test[92]))
            list.append(str(test[23]))
            list.append(str(test[43]))
            list.append(str(test[87]))
        elif patient.diet_answer == "Keto":
            Test.objects.all()
            list.append(str(test[11]))
            list.append(str(test[53]))
            list.append(str(test[93]))
            list.append(str(test[94]))
            list.append(str(test[29]))
            list.append(str(test[85]))
            list.append(str(test[38]))
        elif patient.diet_answer == "High Protien":
            Test.objects.all()
            list.append(str(test[83]))
            list.append(str(test[93]))
            list.append(str(test[94]))
            list.append(str(test[10]))
            list.append(str(test[55]))
            list.append(str(test[23]))
        if patient.drinking_answer == "I drink everyday":
            print("her")
            Test.objects.all()
            list.append(str(test[26]))
            list.append(str(test[83]))
            list.append(str(test[23]))
            list.append(str(test[107]))
            list.append(str(test[108]))
            list.append(str(test[109]))
            list.append(str(test[110]))
            list.append(str(test[111]))
        elif patient.drinking_answer == "3-6 days a week":
            print("her")
            Test.objects.all()
            list.append(str(test[26]))
            list.append(str(test[23]))
            list.append(str(test[107]))
            list.append(str(test[108]))
            list.append(str(test[109]))
            list.append(str(test[111]))
        elif patient.drinking_answer == "1-3 days a week":
            Test.objects.all()
            list.append(str(test[23]))
            list.append(str(test[111]))
        if patient.workout_answer == "Don't remember last time I worked out":
            print("her")
            Test.objects.all()
            list.append(str(test[23]))
            list.append(str(test[26]))
            list.append(str(test[92]))
            list.append(str(test[87]))
        elif patient.workout_answer=="1 hour of more, less than 2 days a week":
            print("her")
            Test.objects.all()
            list.append(str(test[23]))
            list.append(str(test[26]))
            list.append(str(test[92]))
            list.append(str(test[87]))
        elif patient.workout_answer == "1 hour of more daily" or patient.workout_answer == "1 hour of more, 3 days a week":
            Test.objects.all()
            list.append(str(test[83]))
            list.append(str(test[11]))
            list.append(str(test[85]))

        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()

    if patient.question1 == "How would you describe your energy levels?":
        if patient.answer1!="I feel energrtic all day":
            Test.objects.all()
            list.append(str(test[105]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    if patient.healthgoal == "weight":
        if patient.age <18 and patient.gender == "Female":
            Test.objects.all()
            list.append(str(test[112]))
            list.append(str(test[29]))
            list.append(str(test[30]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        elif patient.age >18 and patient.age<50 and patient.gender == "Female":
            Test.objects.all()
            list.append(str(test[112]))
            list.append(str(test[29]))
            list.append(str(test[30]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        elif patient.age>50 and patient.gender == "Female":
            Test.objects.all()
            list.append(str(test[85]))
            list.append(str(test[86]))
            list.append(str(test[23]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        if patient.bmi<18.5:
            Test.objects.all()
            list.append(str(test[113]))
            list.append(str(test[23]))
            list.append(str(test[112]))
            list.append(str(test[43]))
            list.append(str(test[29]))
            list.append(str(test[30]))
            list.append(str(test[85]))
            list.append(str(test[114]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()

        if patient.bmi>25:
            Test.objects.all()
            list.append(str(test[113]))
            list.append(str(test[23]))
            list.append(str(test[34]))
            list.append(str(test[77]))
            list.append(str(test[82]))
            list.append(str(test[55]))
            list.append(str(test[85]))
            if patient.gender == "Male":
                list.append(str(test[35]))
                list.append(str(test[104]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        if patient.diet_answer == "veg":
            Test.objects.all()
            list.append(str(test[43]))
            list.append(str(test[11]))
            list.append(str(test[85]))
            list.append(str(test[29]))
            list.append(str(test[39]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        elif patient.diet_answer == "nonveg":
            Test.objects.all()
            list.append(str(test[26]))
            list.append(str(test[92]))
            list.append(str(test[23]))
            list.append(str(test[43]))
            list.append(str(test[87]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        elif patient.diet_answer == "Gluten Free":
            Test.objects.all()
            list.append(str(test[26]))
            list.append(str(test[92]))
            list.append(str(test[23]))
            list.append(str(test[43]))
            list.append(str(test[87]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        elif patient.diet_answer == "Keto":
            Test.objects.all()
            list.append(str(test[11]))
            list.append(str(test[53]))
            list.append(str(test[93]))
            list.append(str(test[94]))
            list.append(str(test[29]))
            list.append(str(test[85]))
            list.append(str(test[38]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
        elif patient.diet_answer == "High Protien":
            Test.objects.all()
            list.append(str(test[83]))
            list.append(str(test[93]))
            list.append(str(test[95]))
            list.append(str(test[27]))
            pk_id=request.session.get("pk_id")
            patient=Patient.objects.get(patient_id=pk_id)
            patient.tests=list
            patient.save()
    if patient.question1 == "Which of the following symptoms best describe your problem?":
        if patient.answer1 == "Gastritis/ Acidity/ GERD":
            Test.objects.all()
            list.append(str(test[80]))
            list.append(str(test[115]))
        elif patient.answer1 == "Belching/ burping/ heart burn / indigestion":
            Test.objects.all()
            list.append(str(test[80]))
            list.append(str(test[115]))
        elif patient.answer1 == "Constipation":
            Test.objects.all()
            list.append(str(test[115]))
        elif patient.answer1 == "Diarrhoea less than 1week":
            Test.objects.all()
            list.append(str(test[4]))
            list.append(str(test[8]))
            list.append(str(test[116]))
            list.append(str(test[117]))
            list.append(str(test[116]))
            list.append(str(test[93]))
            list.append(str(test[94]))
            list.append(str(test[118]))
            list.append(str(test[119]))
            list.append(str(test[120]))

        elif patient.answer1 == "Diarrhoea more than 1 week":
            Test.objects.all()
            list.append(str(test[4]))
            list.append(str(test[8]))
            list.append(str(test[116]))
            list.append(str(test[117]))
            list.append(str(test[116]))
            list.append(str(test[93]))
            list.append(str(test[94]))
            list.append(str(test[118]))
            list.append(str(test[85]))
            list.append(str(test[11]))
            list.append(str(test[43]))
            list.append(str(test[56]))
            list.append(str(test[29]))
            list.append(str(test[30]))
            
            if patient.age>50:
                list.append(str(test[121]))
                list.append(str(test[122]))


        elif patient.answer1 == "Alternating diarrhoea and constipation":
            Test.objects.all()
            list.append(str(test[78]))
        elif patient.answer1 == "Nausea/ vomiting":
            Test.objects.all()
            list.append(str(test[80]))
            list.append(str(test[115]))
        elif patient.answer1 == "Bloating/ Flatulance / Gas":
            Test.objects.all()
            list.append(str(test[80]))
            if patient.age<30:
                list.append(str(test[78]))
        elif patient.answer1 == "Trouble digesting fatty food/ uneasy feeling after fatty meal":
            Test.objects.all()
            list.append(str(test[109]))
            list.append(str(test[123]))
            list.append(str(test[124]))
            list.append(str(test[111]))
            list.append(str(test[110]))
        elif patient.answer1 == "Irritable bowel syndrome/ Irritable bowel disease/ know more":
            Test.objects.all()
            list.append(str(test[115]))
            list.append(str(test[125]))
            list.append(str(test[126]))
            list.append(str(test[8]))

        pk_id=request.session.get("pk_id")
        pk_id=request.session.get("pk_id")
        patient=Patient.objects.get(patient_id=pk_id)
        patient.tests=list
        patient.save()




    
    
    pk_id=request.session.get("pk_id")
    patient=Patient.objects.get(patient_id=pk_id)    
    list2=set(list)          
    x=len(list2) 
    return render(request,'result.html',{'patient_answer1':patient.answer1,'list':list2,'patient_gender':patient.gender,'patient_name':patient.name, 'patient_age':patient.age,'x':x})













count=0
def g(request):
    global count 
    count=count+1
print(count)
def problem1(request):    

    if 'value1' in request.POST:
        ans=request.POST['value1']
        g(request)

    elif 'value2' in request.POST:
        ans=request.POST['value2']
  
    
    elif 'value3' in request.POST:
        ans=request.POST['value3']
   

          
    
    elif 'value4' in request.POST:
        ans=request.POST['value4']
    
        
    elif 'value5' in request.POST:
        ans=request.POST['value5']

    
    elif 'value6' in request.POST:
        ans=request.POST['value6']


    print(count)

    
    

    return render(request,'problem1.html')




def sample(request):
    return render(request,'sample.html')


def underweight(request):
    general2(request)
    b=x
    print("hello")
    print(x)
    return render(request,'underweight.html',{'b': b}) 

def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        contactus = Contactus(name=name, email=email, number=number)
        contactus.save()

    return render(request,'home.html')









