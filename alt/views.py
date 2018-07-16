# -*- coding: utf-8
from django.shortcuts import render

#django required modules for send email
import smtplib
from email.mime.text import MIMEText
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
#django render modules
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
#django forms such as Login and ContactForm
from . import forms
#get the static url on views url = static('x.jpg')
from django.contrib.staticfiles.templatetags.staticfiles import static
#from . import forms


# Create your views here.

def home(request):
	Breadcrum = False
	Active = 'home'

	return render(request, 'frontend/home.html', locals())

def electronica(request):
	Breadcrum = True
	Active = 'electronica'
	message = "Electronica"

	return render(request, 'frontend/electronica.html', locals())

def vision(request):
	Breadcrum = True
	Active = 'vision'
	message = "Visión Artificial"

	return render(request, 'frontend/vision.html', locals())

def termografia(request):
	Breadcrum = True
	Active = 'termografia'
	message = "Termografía"

	return render(request, 'frontend/termografia.html', locals())

def instrumentacion(request):
	Breadcrum = True
	Active = 'instrumentacion'
	message = "Instrumentación"

	return render(request, 'frontend/instrumentacion.html', locals())
	

def thermogenius(request):

	return render(request, 'frontend/thermogenius.html', locals())

def job(request):
	Breadcrum = True
	message = "Bolsa de Trabajo"
	active = "Empleo"
	form_class = forms.JobForm
	form = form_class(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			contact_name = request.POST.get('name', '')
			contact_age = request.POST.get('age', '')
			contact_email = request.POST.get('email', '')
			contact_phone = request.POST.get('phone', '')
			contact_position = request.POST.get('position', '')
			contact_salary = request.POST.get('salary', '')
			contact_available = request.POST.get('available', '')
			#contact_product = request.POST.get('subject', '')
			form_content = request.POST.get('content', '')
			template = get_template('frontend/jobemail_template.html')
			context ={
				'url': '',
				'name': contact_name,
				'age': contact_age,
				'email': contact_email,
				'phone': contact_phone,
				'position': contact_position,
				'salary': contact_salary,
				'available': contact_available,
				#'subject': contact_product,
				'form_content': form_content,}
			content = template.render(context)
			email = EmailMessage ('Formulario de Contacto', content, to = {'g.zardain@codelab.mx'}, headers = {'Reply-To': contact_email })
			email.content_subtype = 'html'
			email.send()
			messages.success(request, 'Tu información ha sido enviada.')
	return render(request, 'frontend/empleo.html', locals())





def contact(request):
	Active = 'contacto'
	Breadcrum = True
	message = "Contacte Con Nosotros"
	active = "Contacto"
	form_class = forms.ContactForm
	form = form_class(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			contact_name = request.POST.get('name', '')
			contact_email = request.POST.get('email', '')
			contact_phone = request.POST.get('phone', '')
			contact_company = request.POST.get('company', '')
			contact_product = request.POST.get('subject', '')
			form_content = request.POST.get('content', '')
			template = get_template('frontend/contact_template.html')
			context ={
				'url': '',
				'name': contact_name,
				'email': contact_email,
				'phone': contact_phone,
				'company': contact_company,
				'subject': contact_product,
				'form_content': form_content,}
			content = template.render(context)
			email = EmailMessage ('Formulario de Contacto', content, to = {'g.zardain@codelab.mx'}, headers = {'Reply-To': contact_email })
			email.content_subtype = 'html'
			email.send()
			messages.success(request, 'Tu información ha sido enviada.')
	return render(request, 'frontend/contact.html', locals())



def proyecto_traza(request):
	Breadcrum = True
	Active = 'proyectos'
	return render(request, 'frontend/proyecto.html', locals())

def proyecto_campana(request):
	Breadcrum = True
	Active = 'proyectos'
	return render(request, 'frontend/campana_extractora.html', locals())

def proyecto_monitorizacion(request):
	Breadcrum = True
	Active = 'proyectos'
	return render(request, 'frontend/monitorizacion.html', locals())

def proyecto_oximetro(request):
	Breadcrum = True
	Active = 'proyectos'
	return render(request, 'frontend/oximetro.html', locals())

def proyecto_localizador(request):
	Breadcrum = True
	Active = 'proyectos'
	return render(request, 'frontend/localizador.html', locals())

def proyecto_medidor(request):
	Breadcrum = True
	Active = 'proyectos'
	return render(request, 'frontend/medidor.html', locals())

def proyectos(request):
	Breadcrum = True
	Active = 'proyectos'
	message = "Nuestros Proyectos"
	return render(request, 'frontend/proyectos.html', locals())

def proyecto_ditek(request):
	Breadcrum = True
	Active = 'proyectos'
	return render(request, 'frontend/ditek.html', locals())
