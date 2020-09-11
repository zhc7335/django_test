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

## 2 使用模型

### 2.1 定义模型类

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

### 2.2 生成迁移

- 类似于生成sql脚本

```shell
#在项目目录下执行下面的命令
python manage.py makemigrations
#会生成django_test-->book_app-->migrations目录下的迁移文件
```

### 2.3 执行迁移

- 执行迁移文件，创建表

```shell
python manage.py migrate
```

