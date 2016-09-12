#!/usr/bin/env python
'''
__author__ = "Neil R"
__copyright__ = "Copyright 2016"

__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Neil R"
__website__ = "www.neil-r.com"
__status__ = "Production"

View will provide a General overview page on the base URL.
View will response with a JSON View if baseurl.com/state%20name
or baseurl.com/state_abbrev is used.

'''

from django.shortcuts import render
from django.http import	HttpResponse
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date


from . import models
from . import serializers

def home_view(request):
	'''
	Shows simple home page when user goes to base URL.
	'''
	return render(request, 'states/home.html')

class ShowStateDetails(APIView):
	def empty_view(self):
		'''
		Returns standard "No State Details" Message 
		'''
		raise APIException("No State Details")

	def search_state_code(self,state_code):
		'''
		Queries for State Data using two character Abbreviation. 

		Parameter: Data - Two character String
		Returns: API Response 
		'''
		state_info = models.State.objects.filter(state_abbrev=state_code.upper())
		if len(state_info) == 0:
			return self.empty_view()

		serializer = serializers.StateSerializer(state_info, many=True)
		return Response(serializer.data)

	def search_state(self,state):
		'''
		Queries for State Data using full name of state.

		Parameter: Data - String of State Name
		Returns
		'''
		state_info = models.State.objects.filter(state_name=state.title())
		if len(state_info) == 0:
			return self.empty_view()
		serializer = serializers.StateSerializer(state_info, many=True)
		return Response(serializer.data)

	def get(self, request, data, format=None):

		if len(data) == 2:
			return self.search_state_code(data)
		else:
			return self.search_state(data)

		return self.empty_view()
