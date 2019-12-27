![ArtPress](./documents/images/artpress-logo-small.png)


[English](/README.md) | [中文文档](/README-zh.md) | [日本語](/README-jp.md)

[API Document](/documents/apis.md)

# What is ArtPress？
ArtPress is a media-based website management system.



# Fast run ArtPress

**Waring: For security, please DO NOT use this method of installation in a production environment!**

## In Windows
### Step.1 Install Python3.x
Suggest python3.7 or above.

Go [Python.org](https://www.python.org/downloads/) Download and installation the python.

**Attention: Please installation Pypi，and make sure the python in the PATH.**


### Step.2 Clone the code, and install requirements
Use the GIT:

```
git clone https://github.com/JiangCX3/ArtPress.git
```

Or Download the [ZIP file](https://github.com/JiangCX3/ArtPress/archive/master.zip)

Next, install the requirements:
```
cd ./ArtPress
pip install -r requirements.txt
```

In some location, Pypi source will be very slow. You can try these mirror:
 
China (Tsinghua University): 
`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

Japan (Python.jp):
`pip install -r requirements.txt -i http://pypi.python.jp/ --trusted-host pypi.python.jp`


### Step.4 Run it.
Make Database Migrations:
```
python manage.py makemigrations
python manage.py migrate
```

Run Test Server:
```
python manage.py runserver 8000
```

Visit [http://localhost:8000/](http://localhost:8000/)，Welcome！



## In Linux
等我哪天想起来了再写
