from django.urls import (
    include,
    path,
    re_path
)

from django.contrib import admin

from graphene_django.views import GraphQLView


urlpatterns = [
    path("", include("apps.core.urls")),
    path("admin/", admin.site.urls),
    re_path(r"graphql", GraphQLView.as_view(graphiql=True)),
]
