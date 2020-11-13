# DJANGO

## 1 创建项目

```python
django-admin startproject projectname

django-admin startproject django_test
```

## 2 创建应用

- 进入项目目录

```shell
cd django_test
```

- 创建应用

```shell
python manage.py startapp book_app
```

- 设置settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book_app',#加上这一行——创建的应用
]
```

- 目录结构

![image-20200910201859402](C:\Users\zhanghuachao-ghq\AppData\Roaming\Typora\typora-user-images\image-20200910201859402.png)

## 3 使用模型

### 3.1 定义模型类

- models.py

```python
from django.db import models


# Create your models here.
# 定义如下两个模型类，即两张表
class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField()


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

```

### 3.2 生成迁移

- 类似于生成sql脚本

```shell
#在项目目录下执行下面的命令
python manage.py makemigrations
#会生成django_test-->book_app-->migrations目录下的迁移文件
```

### 3.3 执行迁移

- 执行迁移文件，创建表

```shell
python manage.py migrate
```

## 4 数据操作

```python
 C:\python\django_test>python manage.py shell
Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from book_app.models import BookInfo

In [2]: b=BookInfo()

In [3]: b.title='射雕英雄传'

In [4]: from datetime import date

In [5]: b.pub_date=date(2020,1,1)

In [6]: b.save()

In [7]: BookInfo.objects.all()
Out[7]: <QuerySet [<BookInfo: BookInfo object (1)>]>


C:\python\django_test>python manage.py shell
Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from book_app.models import BookInfo

In [2]: BookInfo.objects.all()
Out[2]: <QuerySet [<BookInfo: 射雕英雄传>]>

In [3]: b=BookInfo.objects.get(id=1)

In [6]: b.title='shendiaoxialv'

In [7]: b.save()

In [9]: BookInfo.objects.all()
Out[9]: <QuerySet [<BookInfo: shendiaoxialv>]>

In [10]: b.delete()
Out[10]: (1, {'book_app.BookInfo': 1})

In [11]: BookInfo.objects.all()
Out[11]: <QuerySet []>

In [12]: b=BookInfo()

In [13]: b.title='shendiaoxialv'

In [14]: from datetime import date

In [15]: b.pub_date=date(2020,1,1)

In [16]: b.save()

In [17]: BookInfo.objects.all()
Out[17]: <QuerySet [<BookInfo: shendiaoxialv>]>

In [19]: from book_app.models import HeroInfo

In [20]: h=HeroInfo()

In [21]: h.name='guojing'

In [23]: h.gender=True

In [24]: h.content='xianglongshibazhang'

In [25]: h.book=BookInfo.objects.get(id=2)

In [26]: h.save()

In [27]: HeroInfo.objects.all()
Out[27]: <QuerySet [<HeroInfo: HeroInfo object (1)>]>

In [28]: book=BookInfo.objects.get(id=2)

In [29]: book
Out[29]: <BookInfo: shendiaoxialv>

In [30]: book.heroinfo_set.all()#根据书的名字查询含有哪些英雄
Out[30]: <QuerySet [<HeroInfo: HeroInfo object (1)>]>
```

## 5 后台管理

- admin.py

```python
from django.contrib import admin
from book_app.models import *


# Register your models here.

#下面两个类是将两个表的column显示在后台管理
class BookinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']


class HeroinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'gender', 'book']


#将两个表的信息注册到admin管理平台
admin.site.register(BookInfo, BookinfoAdmin)
admin.site.register(HeroInfo, HeroinfoAdmin)
```

- settings.py

```python
#让后台管理显示为中文
LANGUAGE_CODE = 'zh-Hans'
#定义时区
TIME_ZONE = 'Asia/Shanghai'
```

- 运行

```shell
C:\python_workspace\django_test>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 09, 2020 - 15:27:42
Django version 3.1.1, using settings 'django_test.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[09/Nov/2020 15:27:45] "GET / HTTP/1.1" 200 16299
#上面的http://127.0.0.1:8000/即为后台管理地址,
```

