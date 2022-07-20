# 如何开发 API

如何高效地开发 API 是 Zealot 项目主要关注的内容。但我们并没有直接在项目中增加示例代码（因为你还需要手动删除它们，多此一举）。

下面将推荐一种我们偏好的实践方案。

## 使用 `inject_serializer` 标准化你的 API

`inject_serializer` 本质上是一个语法糖，借助 [Serializer](https://www.django-rest-framework.org/api-guide/serializers/) 定义了任意 API 的输入输出协议。

有兴趣也可以阅读 [这篇博文](https://emergencyexit.xyz/make-serializer-as-dependency-injector.html) 来了解开发它的起因。

使用示例：

```python
# api/{{cookiecutter.api_name}}/foo_app/views.py

from blue_krill.web.drf_utils  import inject_serializer
from rest_framework import serializers, viewsets

from {{cookiecutter.api_name}}.foo_app.models import Foo


class InputSerializer(serializers.Serializer):
    foo  = serializers.CharField()
    bar  = serializers.IntegerField()

    
class OutputSerializer(serializers.Serializer):
    out = serializers.DictField()

    
class FooSerializer(serializers.ModelSerializer):
    """Foo Model SLZ"""
    
    class Meta:
        model = Foo
    
        
class ExampleViewSet(viewsets.GenericViewSet):

    @inject_serializer(query_in=InputSeralizer, out=OutputSeralizer)
    def get(self, validated_data: dict):
        return {"out": {validated_data["foo"]: validated_data["bar"]}}

    
class SomeModelViewSet(viewsets.ModelViewSet):

    @inject_serializer(query_in=InputSeralizer, out=FooSerializer)
    def get(self, validated_data: dict):
        foo = self.get_object()
        ...
        # do some cool stuff
        return foo

```


## 使用 DRF Router 来简化 `urls.py` 配置

我们推荐使用 [DRF Router](https://www.django-rest-framework.org/api-guide/routers/) 来简化 `urls.py` 的配置



```python
# api/{{cookiecutter.api_name}}/foo_app/urls.py

from rest_framework.routers import SimpleRouter


from . import views 

router = SimpleRouter()
router.register("api/v1/foo", views.SomeModelViewSet)

```



增加 `action` 装饰器为非标准 API 提供元信息。

```python
# api/{{cookiecutter.api_name}}/foo_app/views.py
    
class SomeModelViewSet(viewsets.ModelViewSet):

    @inject_serializer(query_in=InputSeralizer, out=FooSerializer)
    @action(detail=True, methods=["POST"])
    def other_method(self, validated_data: dict):
        foo = self.get_object()
        ...
        # do some cool stuff
        return foo

```

### 自动生成的文档

当 API 开发完成后，可以访问 `http://localhost:{{cookiecutter.local_dev_port}}/swagger/` 来查看自动生成的文档。