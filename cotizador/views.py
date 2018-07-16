# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render

#django render modules
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.db.models import Q
from django.contrib.staticfiles.templatetags.staticfiles import static
from . import forms, models

def cotizador(request):
	Breadcrum = True
	Active = 'cotizador'
	message = "Cotizador"
	form = forms.Cotizador()	
	return render(request, 'frontend/cotizador.html', locals())

def get_cotizador(request):
	if request.method == 'POST':
		form = forms.Cotizador(request.POST or None)
		data_dict = []
		if form.is_valid():
			success = 'success'
			cameras = int(request.POST.get('cameras', ''))
			comunications = request.POST.get('comunications', '')
			nets = request.POST.get('nets', '')
			analog_out = int(request.POST.get('analog_out', ''))
			digital_out = int(request.POST.get('digital_out', ''))
			if cameras >= 3:
				object = models.ThermoGenius.objects.get(name='Modelo L')
			elif cameras == 2:
				object = models.ThermoGenius.objects.get(name='Modelo M')
			elif cameras == 1:
				object = models.ThermoGenius.objects.get(name='Modelo S')
			if digital_out == 24 or analog_out == 8:
				object = models.ThermoGenius.objects.get(name='Modelo L')
			
			list = models.Especifications.objects.filter(thermogenius=object)
			ul = '''<ul>'''
			
			for obj in list:
				ul = ul+'''<li>{}</li>'''.format(obj.name)
			ul = ul +'''</ul>'''
			data_dict.append({'form_id':'id_product_name', 'form_value':unicode(object.name)})
			data_dict.append({'form_id':'id_product_description', 'form_value':unicode(object.description)})
			data_dict.append({'form_id':'id_product_price', 'form_value':unicode('$'+ object.price)})
			data_dict.append({'form_id':'id_product_image', 'form_value':unicode(object.image.url)})
			data_dict.append({'form_id':'id_product_especification', 'form_value':unicode(ul)})
		
		else:
			success ='error'
			for data in form.errors:
				result = {"form_id":form[data].auto_id, "error":form[data].errors}
				errors_dict.append(result)
		to_json = {'success':success,}
		data_seri =json.dumps({'to_json':to_json,'data_dict':data_dict}, indent=3)
		return HttpResponse(data_seri, content_type="application/json")
			
	else:
		raise Http404
	