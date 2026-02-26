from django import forms
from .models import Student
from django.core.validators import RegexValidator

class personalDetailsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' 
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}) 
         } # this enables the browser calendar
         # 
#     name = forms.CharField(label="Enter Your Name",min_length=6,error_messages={'required':'Enter your name it is mandatory',
#                                                                                 'min_length':'Name should be at least 6 characters long'})
#     #email = forms.EmailField(label="Enter Your Email",widget=forms.EmailInput)

#     email = forms.EmailField(
#         label="Enter Your Email",
#         error_messages={
#             'required': 'Email is mandatory',
#             'invalid': 'Enter a valid email address'
#         }
#     )
#     p_number=forms.CharField(
#                     label="Enter your Mobile Number",
#                     validators=[
#                     RegexValidator(
#                     regex=r'^\d{10}$',
#                     message='Enter a valid 10 digit contact number',

#                     )
#                     ],
#                     error_messages={
#                         'required':"Mobile Number is mandatory",
#                         "invalid":"Enter valid 10 digit contact number",
#                     }

#     )
#     dob=forms.DateField(label="Enter your dob",
#                         error_messages={
#                             'required':"Date of birth is mandatory",
#                             'invalid':"Enter date in valid format YYYY-MM-DD"
#                         },
#                         widget=forms.DateInput(
#                         attrs={'type': 'date'}  # This enables the browser calendar
#         )
#                         )
#     gender=forms.ChoiceField(label="Select your gender",
#                             choices=[('male','Male'),('female','Female'),('other','Other')],
#                             error_messages={
#                                 'required':'It is mandatory to select',
#                                 'invalid_choice':'select the gender  among the given choices'
#                             },
#                             widget=forms.Select()
#     )

#     department=forms.ChoiceField(label="Select your Department",
#                                 choices=[('cse','CSE'),('ece','ECE'),('mech','MECH'),('it','IT')],
#                                 widget=forms.Select()
#     )
#     yostudy=forms.ChoiceField(label="Select Year of Study",
#                               choices=[('1st','1st'),('2nd','2nd'),('3rd','3rd'),('4th','4th')],
#                               widget=forms.Select()
#     )
#     rollnumber=forms.CharField(label="Enter your Roll Number",max_length=10,
#                                widget=forms.TextInput(),
#     )
#     address=forms.CharField(label="Enter your Address",
#                             widget=forms.Textarea(
#                                 attrs={'rows':4,'cols':15}
#                             )
#     )
#     state=forms.ChoiceField(label="Enter your state",
#                           choices=[('AndhraPradesh','andhrapradesh'),('Telangana','telangana'),('Karnataka','karnataka'),('Tamilnadu','tamilnadu')],
#                           widget=forms.Select()
#     )
#     pincode=forms.CharField(label="Enter your Pincode",
#                             error_messages={
#                                 'required':'Pincode is mandatory',
#                                 'invalid':'Enter valid pincode'
#                             }
#     )
#     technical_Skills=forms.ChoiceField(label="Select your Technical Skills",
#                                                choices=[('python','Python'),('java','Java'),('c++','C++'),('webdevelopment','Webdevelopment')],
#                                                widget=forms.Select()
#     )
#     preferred_mode=forms.ChoiceField(label="Select your Preferred Mode of Learning",
#                                      choices=[('online','Online'),('offline','Offline')],
#                                      widget=forms.Select()
#     )
#     resume_upload=forms.FileField(label="Upload your Resume",
#                                 #   choices=[('Pdf','pdf'),('Doc','doc')],
#                                 #   widget=forms.Select()
#     )
#     about_yourself=forms.CharField(label="About yourself",
#                             widget=forms.Textarea(
#                                 attrs={'rows':4,'cols':15})
#     )
#     aggree=forms.BooleanField(
#                             required=True,
#                             label="I agree to the Terms and Conditions",
#                             error_messages={'required': 'You must agree to the terms to proceed.'}

#     )

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = "__all__"









# class signupform(forms.Form):
#     name = forms.CharField(label="enter name:", min_length=5, error_messages={'required': 'please enter name', 'min_length': 'minimum 5 characters required'})
#     password = forms.CharField(label="enter password:", widget=forms.PasswordInput)