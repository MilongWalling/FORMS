
from django import forms
from .models import Member,Address,Family

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['full_name', 'member_type', 'gender', 'date_of_birth', 'occupation', 'marital_status','profile_picture','remarks']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address  # Change to Member model
        fields = ['street_address', 'city', 'state', 'country','zip_code']  # Update fields


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['member1', 'member2', 'relationship']
        widgets = {
            'relationship': forms.Select(choices=Family.RELATIONSHIP_CHOICES),
            'member1': forms.HiddenInput(),
        }