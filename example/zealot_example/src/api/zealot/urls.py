""""""
from django.contrib import admin
from django.urls import include, path, re_path

from zealot.account import urls as account_urls
from zealot.apis import urls as apis_urls
from zealot.common.views import WebPageViewSet

urlpatterns = [
    path("", include(account_urls)),
    path("", include(apis_urls)),
    path("adminUydhfe75W2/", admin.site.urls),
    # 其余路由转发到前端页面处理
    re_path(r"^", WebPageViewSet.as_view({"get": "index"}), name="index"),
]