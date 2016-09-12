from rest_framework import serializers
import datetime

from . import models

class StateSerializer(serializers.ModelSerializer):
	joined_union = serializers.SerializerMethodField('format_date')

	class Meta:
		fields = (
			'state_name',
			'state_abbrev',
			'capital',
			'population',
			'population_rank',
			'joined_union',
			'nicknames'
			)
		model = models.State

	def format_date(self, obj):
		'''
		Takes a date and returns 'Month 00, 1800'
		Workaround due to limitation of strftime with dates before 1900
		'''
		year, month, day = obj.joined_union.isoformat().split('-')
		month_str = datetime.date(1900, int(month), 1).strftime('%B')
		return '{} {}, {}'.format(month_str, day, year)
 