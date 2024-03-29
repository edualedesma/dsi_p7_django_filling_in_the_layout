from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample_project.views.home', name='home'),
    # url(r'^sample_project/', include('sample_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^about$', 'my_app.views.about', name='about'),
    url(r'^home$', 'my_app.views.home', name='home'),
    url(r'^help$', 'my_app.views.help', name='help'),
    url(r'^$', 'my_app.views.index', name='index'),
    url(r'^contact$', 'my_app.views.contact', name='contact'),
    url(r'^signup$', 'my_app.views.signup', name='signup'),
)