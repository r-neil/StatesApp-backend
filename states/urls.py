from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<data>.*)', views.ShowStateDetails.as_view(), name='state_details'),
]