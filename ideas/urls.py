from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url("^$", "ideas.views.index", name="idea-index"),
    url("(?P<idea_pk>\d+)/vote/(?P<amount>\d+)/$",
        "ideas.views.vote",
        name="idea-vote"
    ),
    url("(?P<idea_pk>\d+)/edit/$", "ideas.views.edit", name="idea-edit"),
    url("(?P<idea_pk>\d+)/$", "ideas.views.detail", name="idea-detail"),
    url("popular/$", "ideas.views.popular", name="idea-popular"),
    url("new/$", "ideas.views.new", name="idea-new"),
)
