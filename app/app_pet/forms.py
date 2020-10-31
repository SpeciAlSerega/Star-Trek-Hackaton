from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from app_pet.models import MyUser
from .models import Tag, Post


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('name', 'avatar', 'Telegram', 'Vk', 'phone', 'shelter', 'people', 'donate', 'data_start_donat')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('name', 'avatar', 'Telegram', 'Vk', 'phone', 'shelter', 'people', 'donate', 'data_start_donat', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'avatar', 'Telegram', 'Vk', 'phone', 'shelter', 'people', 'donate', 'data_start_donat', 'is_active', 'is_admin') # список параметров в админке
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('name', 'password')}),
        ('Personal info', {'fields': ('avatar', 'Telegram', 'Vk', 'phone', 'shelter', 'people', 'donate', 'data_start_donat',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'avatar', 'Telegram', 'Vk', 'phone', 'shelter', 'people', 'donate', 'data_start_donat', 'password1', 'password2','is_admin'), #Здесь добавляются поля в админку
        }),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()

#####################################################################################################################################

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Пост не может быть "Create"')
        return new_slug



class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug',]

        # применение стилей в форме. Результат будет <input class='form-control'>
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Тег не может быть "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Тег должен быть уникальным. Тег "{}" уже существует'.format(new_slug))
        return new_slug