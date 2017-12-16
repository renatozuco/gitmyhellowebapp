"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

"""The book web app wanted to delete the above comments, they are the original comments, I decided not to delete them,
also a line added to this urls.py file is url(r'^$','collection.views.index', name='home'), by the book indication"""

from collection.backends import MyRegistrationView
from django.contrib.auth.views import(
	password_reset,
	password_reset_done,
	password_reset_confirm,
	password_reset_complete,
)

#Initially this only had import url(patterns and include is how the book has it in page 24)
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView


#I changed the patterns list [] for the patters function () and imported patterns and include on top as it is showed in the book page 24. This was done because the book shows django 1.9 but this file came edited for django 1.10 and you don't need include and patterns is a list but because my hellowebapp book is in 1.9 I made the necessary changes.
urlpatterns = patterns('',
	url(r'^$', 'collection.views.index', name='home'),
					   
	url(r'^about/$',
		TemplateView.as_view(template_name='about.html'),
		name='about'),
					   
	url(r'^contact/$',
		TemplateView.as_view(template_name='contact.html'),
		name='contact'),
	
	#things
	url(r'^things/$', RedirectView.as_view(pattern_name='browse')),
	url(r'^things/(?P<slug>[-\w]+)/$','collection.views.thing_detail', name='thing_detail'),
	#Renato's notes: For this next url line it looks to me that... inside things (which is the list of elements in the index.html file)there is the element we are gonna call slug and inside the element there is a code or variable with name edit.(JUST A THOUGHT)
	url(r'^things/(?P<slug>[-\w]+)/edit/$', 'collection.views.edit_thing', name='edit_thing'),
					   
					   
	#Browse				   
	url(r'^browse/$', RedirectView.as_view(pattern_name='browse')),
	url(r'^browse/name/$', 'collection.views.browse_by_name', name='browse'),
	url(r'^browse/name/(?P<initial>[-\w]+)/$', 'collection.views.browse_by_name', name='browse_by_name'),
					   
	#password reset urls					   
	url(r'^accounts/password/reset/$', password_reset,
	   {'template_name':'registration/password_reset_form.html'}, name="password_reset"),
	url(r'^accounts/password/reset/done/$', password_reset_done,
	   {'template_name':'registration/password_reset_done.html'}, name="password_reset_done"),
	url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		password_reset_confirm, {'template_name':'registration/password_reset_confirm.html'},
		name="password_reset_confirm"),
	url(r'^accounts/password/done/$', password_reset_complete,
		{'templane_name':'registration/password_reset_complete.html'}, name="password_reset_complete"),
					   
					   
	#Accounts
	#in the book this shows ", include('registration.backends.simple.urls')" pg24
	url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
	url(r'^accounts/create_thing/$', 'collection.views.create_thing', name='registration_create_thing'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
					   
	
	#edited this url so it looks like the book, but initially this was 
    #url(r'^admin/', admin.site.urls), this is because in django 1.10 we don't need include
	url(r'^admin/', include(admin.site.urls)),
	)
