from django.contrib import admin

from . import models


class StateAdmin(admin.ModelAdmin):
	list_display = ['state_name', 'state_abbrev', 'capital', 'population','population_rank', 'joined_union', 'nicknames']
	#list_editable = ['']
	ordering = ('population_rank',)


admin.site.register(models.State, StateAdmin)
