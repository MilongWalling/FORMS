from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .forms import MemberForm, AddressForm, FamilyForm
from .models import Member,Family

def member_form_view(request):
    if request.method == 'POST':
        member_form = MemberForm(request.POST,request.FILES)
        address_form = AddressForm(request.POST)
        # family_form = FamilyForm(request.POST)
        if member_form.is_valid() and address_form.is_valid() :
            member_object = member_form.save()
            address = address_form.save(commit=False)
            address.member = member_object
            address.save()
            # family = family_form.save(commit=False)
            # family.member = member_object
            # family.save()
            return redirect(reverse('member_view',kwargs={'member_id':member_object.id}))
    else:
        member_form = MemberForm()
        address_form = AddressForm()
        # family_form = FamilyForm()
    return render(request, 'member_form.html', {'member_form': member_form, 'address_form': address_form})


def member_details_view(request,member_id):
    if request.method == 'GET':
        member_details=Member.objects.get(id=member_id)
        family_members=Family.objects.filter(member1=member_id)
        context={
            'member_details':member_details,
            'family_members':family_members,
        }
        return render(request, 'member_details.html', context)

def add_family_member(request,member_id):
    if request.method == 'POST':
        family_form = FamilyForm(request.POST)
        if family_form.is_valid():
            member_object=Member.objects.get(id=member_id)
            # family = family_form.save(commit=False)
            # family.member = member_object
            family_form.save()
            return redirect(reverse('member_view',kwargs={'member_id':member_object.id}))
    else:
        member_object=Member.objects.get(id=member_id)
        family_form = FamilyForm(initial={'member1':member_object})
        context={
            'family_form':family_form,
            'member_name':member_object.full_name,
        }
    return render(request, 'family_form.html', context)



def members_list_view(request):
    members = Member.objects.all()
    return render(request, 'members_list.html', {'members': members})


def edit_member_view(request, member_id):
    # Fetch the member object using member_id
    member = get_object_or_404(Member, id=member_id)
    
    if request.method == 'POST':
        # Populate MemberForm with the existing member details and the updated data
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        # Populate MemberForm with the existing member details
        form = MemberForm(instance=member)
    
    return render(request, 'edit_member.html', {'form': form, 'member': member})