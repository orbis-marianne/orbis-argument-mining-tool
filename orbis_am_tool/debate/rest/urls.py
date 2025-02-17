from django.urls import re_path

from debate.rest import views

app_name = "debate.rest"
urlpatterns = [
    re_path(
        r"author/(?P<identifier>[0-9a-f]{16})/$",
        views.AuthorView.as_view(),
        name="author-detail",
    ),
    re_path(
        r"debate/(?P<identifier>[0-9a-f]{16})/$",
        views.DebateView.as_view(),
        name="debate-detail",
    ),
    re_path(
        r"statement/(?P<identifier>[0-9a-f]{16})/$",
        views.StatementView.as_view(),
        name="statement-detail",
    ),
]
