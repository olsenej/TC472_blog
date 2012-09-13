from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.index'),
    # url(r'^ecommerce/', include('ecommerce.foo.urls')),

    url(r'^blog/$', 'blog.views.index'),
    url(r'^blog/(?P<blog_id>\d+)/$', 'blog.views.detail'),

    # Adding and viewing comments
    url(r'^comment/(?P<blog_id>\d+)/$$', 'blog.views.comment'),
    url(r'^userComments/$', 'blog.views.userComments'),

    # For deleting comments
    url(r'^delComment/(?P<comment_id>\d+)/$', 'blog.views.delComment'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/kdemaagd/web/images/'})

)
