from django.db import models


class Bmi(models.Model):
    height=models.IntegerField()
    weight=models.IntegerField()


class Contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models. EmailField()
    number=models.IntegerField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    patient_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=20, default="none")
    number=models.IntegerField()
    healthgoal=models.CharField(max_length=50, default="not chosen")
    gender=models.CharField(max_length=50, default="not specified")
    age=models.IntegerField(default=0)
    height=models.IntegerField(default=0)
    weight=models.IntegerField(default=0)
    bmi=models.IntegerField(default=0)
    bmi_result=models.CharField(max_length=50,default="Normal")
    diet_answer=models.CharField(max_length=50, default="none")
    workout_answer=models.CharField(max_length=50, default="none")
    smoking_answer=models.CharField(max_length=50, default="none")
    drinking_answer=models.CharField(max_length=50, default="none")
    subgoal=models.CharField(max_length=50,default="none")
    question1=models.CharField(max_length=100,default="none")
    answer1=models.CharField(max_length=200,default="none")
    question2=models.CharField(max_length=100,default="none")
    answer2=models.CharField(max_length=400,default="none")
    specificquestion1=models.CharField(max_length=100,default="non")
    specificanswer1=models.CharField(max_length=200,default="non")
    specificquestion2=models.CharField(max_length=100,default="non")
    specificanswer2=models.CharField(max_length=100,default="non")
    specificquestion3=models.CharField(max_length=100,default="non")
    specificanswer3=models.CharField(max_length=100,default="non")
    specificquestion5=models.CharField(max_length=100,default="non")
    specificanswer5=models.CharField(max_length=100,default="non")
    specificquestion6=models.CharField(max_length=100,default="non")
    specificanswer6=models.CharField(max_length=100,default="non")
    specificquestion7=models.CharField(max_length=100,default="non")
    specificanswer7=models.CharField(max_length=100,default="non")
    specificquestion8=models.CharField(max_length=100,default="non")
    specificanswer8=models.CharField(max_length=100,default="non")
    specificquestion9=models.CharField(max_length=100,default="non")
    specificanswer9=models.CharField(max_length=100,default="non")
    specificquestion10=models.CharField(max_length=100,default="non")
    specificanswer10=models.CharField(max_length=100,default="non")
    tests=models.CharField(max_length=1000,default="none")

    def __str__(self):
        return self.name


class Test(models.Model):
    test=models.CharField(max_length=50,default="")
    test_code=models.IntegerField(default=0)


    def __str__(self):
        return self.test