from django.urls import path
from sdk_app.views import linviews, winviews

urlpatterns = [

    # windows平台
    path('sdk_manage/', winviews.sdk_manage),
    path('sdk_test/', winviews.sdk_test),
    path('upload/', winviews.upload),

    # linux平台
    path('linsdk_manage/', linviews.linsdk_manage),
    path('linsdk_test/', linviews.linsdk_test),
    path('linupload/', linviews.linupload)
]
