from django.urls import (
    include,
    path,
    re_path
)
from django.conf import settings
from django.contrib import admin
from django.views import static

from graphene_django.views import GraphQLView


urlpatterns = [
    path("", include("apps.core.urls")),
    path("admin/", admin.site.urls),
    re_path(r"graphql", GraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    import warnings


    try:
        import debug_toolbar
    except ImportError:
        warnings.warn(
            "The debug toolbar was not installed. Ignore the error. \
            settings.py should already have warned the user about it."
        )
    else:
        urlpatterns += [
            re_path(r"^__debug__/", include(debug_toolbar.urls))  # type: ignore
        ]

    # urlpatterns += static("/media/", document_root=settings.MEDIA_ROOT) 
