# Django
## 自定义模板标签
1. 与'views.py'同目录下建立文件夹templatetags，以及其中新建'\_\_init\_\_.py'和自定义的标签文件'my_own_tag.py'
2. 在'settings.py'中注册templatetags  
``` python
import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'项目名/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
            'libraries':{
                'my_own_tag':"项目文件夹名字.templatetags.my_own_tag"
            }
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
        },
    },
]
```
3. 在my_own_tag.py中定义标签
``` python
from django import template

register = template.Library()

@register.simple_tag
def test(v1,v2,v3,v4):
    return v1*v2*v3*v4
```

4. 引用模板
``` html
{% load my_own_tag %}
<!--使用my_own_tag.py文件中的test方法，传四个参数进去-->
{% test 1 2 3 4 %}
```