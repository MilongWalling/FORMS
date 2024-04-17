from django.db import models
from misc import models as miscModels

# In member_form/models.py

class Member(models.Model):
    MEMBER_STATUS = [
        ('M', 'Member'),
        ('AM', 'Attende'),
        ('V', 'Visitor'),
        ('N', 'Non Longer Attends'),
        ('U','Unassigned'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Un','Unassigned')
    ]

    OCCUPATION_CHOICES = [
        ('E', 'Employed'),
        ('UE', 'Unemployed'),
        ('S', 'Student'),
        ('R', 'Retired'),
        ('D', 'Deceased'),
    ]

    MARITAL_STATUS=[
        ('M','Married'),
        ('S','Single'),
        ('W','Widowed'),
        ('D','Divorced'),
        ('Un','Unassigned'),
        ('S','Separated'),
    ]
    full_name = models.CharField(max_length=100)
    member_type = models.CharField(max_length=2, choices=MEMBER_STATUS)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    year_of_birth = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=2, choices=OCCUPATION_CHOICES)
    marital_status=models.CharField(max_length=2,choices=MARITAL_STATUS,blank=True)
    profile_picture=models.ImageField(upload_to="profile_pics/%Y/%m/",null=True,blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
    
class Address(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='address')
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(miscModels.State, to_field='uuid', on_delete=models.CASCADE,related_name='adddress_state')
    country = models.ForeignKey(miscModels.Country, to_field='uuid', on_delete=models.CASCADE,null=True,related_name='adddress_country')
    # test = models.ForeignKey(miscModels.State, to_field='uuid', on_delete=models.CASCADE,related_name='test')
    zip_code = models.CharField(max_length=10)


class Family(models.Model):
    RELATIONSHIP_CHOICES = [
        ('F', 'Father'),
        ('M', 'Mother'),
        ('S', 'Sister'),
        ('B', 'Brother'),
        ('D', 'Daughter'),
        ('N', 'Son'),
    ]

    relationship = models.CharField(max_length=1, choices=RELATIONSHIP_CHOICES, blank=True)
    member1 = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='family_member1')
    member2 = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='family_member2')

    def __str__(self):
        return f"{self.member1.full_name} {self.member2.full_name} : {self.relationship}"