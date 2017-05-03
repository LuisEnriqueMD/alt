# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
 
age = RegexValidator(regex=r'^[0-9]{2}$', message="numérico 2 dígitos")
phone_val = RegexValidator(regex=r'^[0-9]{10}$', message="numérico 10 dígitos")
email_val = RegexValidator(regex=r'^[^@]+@[^@]+\.[^@]+', message="dirección de correo no válido")



class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre y Apellido *',
        required=True, 
        max_length=50, 
        min_length=8, 
        widget=forms.TextInput(attrs={
            'placeholder':'Nombre Completo*', 
            'class': 'form-control'}
            )
        )
    email = forms.CharField(
        label='E-Mail *',
        required=True, 
        max_length=50, 
        min_length=8,
        widget=forms.TextInput(attrs={
            'placeholder':'Dirección de E-Mail*', 
            'class': 'form-control'}
            ),
        validators=[email_val]
        )
     
    phone = forms.CharField(
        label='Teléfono *',
        required=False,
        max_length=30,
        min_length=7,
        widget=forms.TextInput(attrs={
            'placeholder':'Teléfono',
            'class':'form-control'}
            ),
        validators=[phone_val]
        )
     
    company = forms.CharField(
        label='Empresa ',
        required=True, 
        max_length=50,
        min_length=4,
        widget=forms.TextInput(attrs={
            'placeholder':'Nombre de tu Empresa',
            'class': 'form-control'}))
     
    subject = forms.CharField(
        label='Asunto ',
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder':'Asunto de Interés',
            'class': 'form-full form-control'}) )
     
    content = forms.CharField(
        label='Mensaje *',
        required=True, 
        min_length=4,
        max_length=2000, 
        widget=forms.Textarea(attrs={
            'placeholder':'Información Adicional',
            'class': 'form-control'}))
     
    def is_valid(self):
        ret = forms.Form.is_valid(self)
        for f in self.errors:
            self.fields[f].widget.attrs.update({'class': self.fields[f].widget.attrs.get('class', '') + ' error'})
        return ret


class JobForm(forms.Form):
    name = forms.CharField(
        label='Nombre y Apellidos *',
        required=True, 
        max_length=50, 
        min_length=1, 
        widget=forms.TextInput(attrs={
            'placeholder':'Nombre Completo*', 
            'class': 'form-control'}
            )
        )

    age = forms.CharField(
        label='Edad *',
        required=True, 
        max_length=2, 
        min_length=1, 
        widget=forms.TextInput(attrs={
            'placeholder':'Edad *', 
            'class': 'form-control'}
            ),
        validators=[age]
        )

    email = forms.CharField(
        label='E-Mail *',
        required=True, 
        max_length=50, 
        min_length=8,
        widget=forms.TextInput(attrs={
            'placeholder':'Dirección de E-Mail*', 
            'class': 'form-control'}
            ),
        validators=[email_val]
        )
     
    phone = forms.CharField(
        label='Teléfono *',
        required=True,
        max_length=30,
        min_length=7,
        widget=forms.TextInput(attrs={
            'placeholder':'Teléfono',
            'class':'form-control'}
            ),
        validators=[phone_val]
        )
     
    position = forms.CharField(
        label='Puesto * ',
        required=True, 
        max_length=50,
        min_length=4,
        widget=forms.TextInput(attrs={
            'placeholder':'Programador Web',
            'class': 'form-control'}))


    salary = forms.CharField(
        label='Salario ',
        required=False, 
        max_length=50,
        min_length=4,
        widget=forms.TextInput(attrs={
            'placeholder':'Expectativa Económica',
            'class': 'form-control'}))
     
    available = forms.CharField(
        label='Coche y Lic de Conducir',
        required=False, 
        widget=forms.TextInput(attrs={
            'placeholder':'Inmediata',
            'class': 'form-full form-control'}) )
     
    content = forms.CharField(
        label='Mensaje *',
        required=True, 
        min_length=4,
        max_length=2000, 
        widget=forms.Textarea(attrs={
            'placeholder':'Información Adicional',
            'class': 'form-control'}))
     
    def is_valid(self):
        ret = forms.Form.is_valid(self)
        for f in self.errors:
            self.fields[f].widget.attrs.update({'class': self.fields[f].widget.attrs.get('class', '') + ' error'})
        return ret