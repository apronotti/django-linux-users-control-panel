# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages

# Register your models here.
from django import forms
from .models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple
import sys
from .osprocess import osprocess

class UserAdminForm(forms.ModelForm):
    name = forms.CharField()
    groups = forms.ModelMultipleChoiceField(
            queryset=Group.objects.all(),
            required=False,
            widget=FilteredSelectMultiple(
                verbose_name=_('Groups'),
                is_stacked=False
                )
            )
    sourceGroups = []
    osproc = osprocess()

    class Meta:
        model = User
        fields = ['name','groups']

    def __init__(self, *args, **kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True

        if (self.instance and not(self.instance.pk is None)):
            self.fields['groups'].initial = self.instance.group_set.all()
            self.sourceGroups = list(self.instance.group_set.all())

    def addRemoveGroups(self):
        ori = set(self.sourceGroups)
        newlist = set(self.cleaned_data['groups'])
        # Add user to group
        for g in (newlist - ori):
            self.osproc.addUserToGroup(str(self.cleaned_data['name']), str(g))
        
        # Delete user from group
        for g in (ori - newlist):
            self.osproc.deleteUserFromGroup(str(self.cleaned_data['name']), str(g))
        

    def save(self, commit=True):
        user = super(UserAdminForm, self).save(commit=False)

        if (not(self.instance.pk is None)):
            user.group_set.set(self.cleaned_data['groups'])
            self.addRemoveGroups()

        if commit:
            user.save()

        return user

class UserAddAdminForm(forms.ModelForm):
    name = forms.CharField()
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    passwordrt = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name','password','passwordrt']

    def __init__(self, *args, **kwargs):
        super(UserAddAdminForm, self).__init__(*args, **kwargs)


    def save(self, commit=True):
        user = super(UserAddAdminForm, self).save(commit=False)
        
        if commit:
            user.save()

        return user

    def clean(self):
        cleaned_data = super(UserAddAdminForm, self).clean()
        password = cleaned_data.get('password')
        passwordrt = cleaned_data.get('passwordrt')

        if (password  != passwordrt):
            raise forms.ValidationError('Passwords do no match!')
        
class UserAdmin(admin.ModelAdmin):
        list_display = ('user_list',)
        search_fields = ['name']
        ordering = ('name',)
        form = UserAdminForm

        def get_form(self, request, obj=None, **kwargs):
            if (obj):
                kwargs['form'] = UserAdminForm
            else:
                kwargs['form'] = UserAddAdminForm

            return super(UserAdmin, self).get_form(request, obj, **kwargs)

        def save_model(self, request, obj, form, change):
            from django.contrib import messages

            message = "ok"       
            message = obj.save()
            
            if (len(message.rstrip()) > 0):
                messages.set_level(request, messages.ERROR)
                messages.error(request, message)

                
        def has_delete_permission(self, request, obj=None):
            if ((obj != None) and (len(obj.group_set.all()) > 0)):
                return False
            else:
                return True

        def user_list(self, obj):
            return ("< %s %s )" % (obj.name, "> || GROUPS --> ( "+" , ".join(map(str,obj.group_set.all()))))

        user_list.short_description = 'Names and groups related'
        admin.site.disable_action('delete_selected')
        

class GroupAdminForm(forms.ModelForm):
    name = forms.CharField()
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Users'),
            is_stacked=False
        )
    )
    sourceUsers = []
    osproc = osprocess()

    class Meta:
        model = Group
        fields = ['name','members']
        permissions = ('change')
        
    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True

        if (self.instance and not(self.instance.pk is None)):
            self.fields['members'].initial = self.instance.members.all()
            self.sourceUsers = list(self.instance.members.all())


    def addRemoveUsers(self):
        ori = set(self.sourceUsers)
        newlist = set(self.cleaned_data['members'])
        # Add user to group
        for u in (newlist - ori):
            self.osproc.addUserToGroup(str(u),str(self.cleaned_data['name']))
    
        # Delete user from group
        for u in (ori - newlist):
            self.osproc.deleteUserFromGroup(str(u), str(self.cleaned_data['name']))
   
            
    def save(self, commit=True):
        group = super(GroupAdminForm, self).save(commit=False)
        if (not(self.instance.pk is None)):
            group.members.set(self.cleaned_data['members'])
            self.addRemoveUsers()

        if commit:
            group.save()

        return group

class GroupAddAdminForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Group
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(GroupAddAdminForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        group = super(GroupAddAdminForm, self).save(commit=False)

        if commit:
            group.save()

        return group

class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_list',)
    search_fields = ['name']
    ordering = ('name',)
    form = GroupAdminForm

    def group_list(self, obj):
        return ("< %s %s)" % (obj.name, "> || USERS --> ( "+" , ".join(map(str,obj.members.all()))))

    group_list.short_description = 'Name and users related'

    def save_model(self, request, obj, form, change):
        from django.contrib import messages

        message = "ok"       
        message = obj.save()
        if (len(message.rstrip()) > 0):
            messages.set_level(request, messages.ERROR)
            messages.error(request, message)

       
    # Return False when the group have members
    def has_delete_permission(self, request, obj=None):
        if ((obj != None) and (len(obj.members.all()) > 0)):
            return False
        else:
            return True
        
    def get_form(self, request, obj=None, **kwargs):
        if (obj):
            kwargs['form'] = GroupAdminForm
        else:
            kwargs['form'] = GroupAddAdminForm
        return super(GroupAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)

