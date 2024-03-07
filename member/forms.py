from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Member, Area, Hop, Zone

class MembershipForm(forms.ModelForm):
   
    first_name = forms.CharField(label='', max_length= 50, required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='', max_length= 50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = Member
        exclude = ("user",)


"""     address = forms.CharField(label='', max_length= 150,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))  
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    phone_number = forms.CharField(label='', max_length= 50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    occupation = forms.CharField(label='', max_length= 50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Occupation'}))
    date_of_birth = forms.DateField()
    sex = forms.ChoiceField(choices=Member.SEX)
    status = forms.ChoiceField(choices=Member.STATUS)
    marital_status = forms.ChoiceField(choices=Member.MARITAL)
    NPA_status = forms.ChoiceField(choices=Member.NPA)
    invited_by = forms.CharField(label='', max_length= 50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Invited By'}))
    day_to_be_visited = forms.DateField()
    visited = forms.CharField(label='', max_length= 50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Visited'}))
    remarks = forms.CharField(label='', max_length= 50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Remarks'}))
    comment = forms.CharField(label='', max_length= 50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Comment'})) """

