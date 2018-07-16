# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

noCamerasChoices = (
    ("0",'Selecciona una Opción'),
    ("1",'1 Cámara'),
    ("2",'2 Cámaras'),
    ("3",'3 Cámaras'),
    ("4",'4 Cámaras'),
)
comunicationYN = (
    ("0",'Selecciona una Opción'),
    ("si",'Si'),
    ("no", 'No'),
)

netType = (
    ("0",'Selecciona una Opción'),
    ("no",'No'),
    ("lan",'LAN'),
    ("wlan",'WLAN'),
    )

analogOut = (
    ("1",'Selecciona una Opción'),
    ("0",'0 AOs'),
    ("4",'4 AOs'),
    ("8",'8 AOs'),
    )
digitalOut = (
    ("0",'Selecciona una Opción'),
    ("8",'8 DOs'),
    ("24",'24 DOs'),
    )

class Cotizador(forms.Form):
    #noCameras = forms.CharField(label='No. de Camaras')
    cameras = forms.ChoiceField(widget=forms.Select, choices=noCamerasChoices)
    comunications = forms.ChoiceField(widget=forms.Select, choices=comunicationYN)
    nets = forms.ChoiceField(widget=forms.Select, choices=netType)
    analog_out = forms.ChoiceField(widget=forms.Select, choices=analogOut)
    digital_out = forms.ChoiceField(widget=forms.Select, choices=digitalOut)


#foo = get_gender_display()