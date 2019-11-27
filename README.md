![ArtPress](./documents/images/artpress-logo-small.png)

# 什么是Artpress？
#### 事情是这样的：
从前有一名摄影师，他使用Wordpress搭建了一个属于自己的摄影网站...

用着用着，感觉愈来愈不对劲...为什么Wordpress只是发布一个照片就要用掉一个文章？
未免太浪费了吧！
    
而且，Wordpress跟Shi一样的媒体库，不能分类就算了，
还要把我的照片和一些站点布置用的文件放在一起！

![WordpressMediaLibraryLikeAShit](https://cdn.jiangcx.cn/2019/11/WP_LAJI_Meitiku.png)

*（注：Wordpress的媒体库截图，每次他看到这个都想打人）*

终于有一天，他实在忍不住了。作为工科出身的他，决定开发一套全新的CMS。

**并写下了这篇文档来定义这个全新的CMS是这样的：**

## 页面
#### 我们把整个站点分为前台与后台。

### 前台
关于前台的页面设计，我们希望以图片与视频为主体，再加上少量的文字用于修饰他们。以下几条是页面设计上的原则：
- 减少不必要的干扰。我们希望网站的主角是作品，而不是花里胡巧的效果；
- 考虑到不同人的需求可能不同，因此我们要给Artpress留下应用第三方模板的接口；
- 优化到位，页面的打开速度一定要有够快；
- 在可能的情况下，尽量应用最新的WEB技术。绝对不要使用已经过时的方法！

页面的设计请多多参考 1x.com ，既前卫又不失优雅。

关于页面逻辑：
- 每个作品都应该拥有一个页面；
- 每个作品都应该有一组标签，用于分类作品；
- 每个作品都应该拥有一个作品名与作者命；

我们需要准备一套站内搜索引擎，通过搜索标签、作品名及作者名等关键字来快速寻找作品；
因此在前台部分，我们需要一下几个页面：
主页
作品页面
分类标签页面
搜索引擎页面
另外，我有想过给这个Artpress加入一个简单的博客系统。等我们先把基础功能实现了再说吧。

### 后台
待补充…

 

关于以上更详细的设计方案，请参考另外的页面设计文档。

## 操作逻辑
关于Artpress的主程序
为了保证开发效率，主程序只要包含最基础的功能（整个后台、账户系统、插件模板及API的接口）即可。页面及更细化的功能应该作为另外的插件与模板来加入程序。

后台媒体库
我希望我们能开发出一套像lightroom图库那样的媒体库，不仅能有简单的筛选功能，还能在线修改图片的EXIF、甚至进行一些简单编辑等等。

插件与模板、以及账户系统
关于插件与模板、以及账户系统，我们可以大量借鉴Wordpress。一来、减少用户学习成本，二来、节省团队沟通成本（照着样子做就行，哈哈）。

 

## 借鉴一些其他现有产品的东西
- WordPress

    WordPress的账户管理系统与插件系统都十分优秀，但是我希望我们的插件系统能比Wordpress更强大一些。将整个Artpress模块化：做出最简单的框架，其他的东西统统用插件实现。这样用户可以自行加上或删除自己想要或不要的模块，如果有人想二次开发，那么这么一来也很方便。

- Instagram

    Artpress的灵感就来源于Instagram。5G时代，图片与视频媒体才是互联网的天下，我们要围绕图片视频媒体开发Artpress。

- 1x.com

    1x.com这个摄影网站的前端设计非常符合我的想法。去掉干扰，将注意力集中在作品上。

- Lightroom

    我们需要把我们的媒体库做成一套可以随时随地管理图片的系统。你甚至可以拿着Artpress不做网站，就把他当作一套在线媒体管理器来用！

## 我们设想会用到的技术
- MYSQL

- Django

- Docker

另外，考虑到不是所有艺术家都是技术大牛，我们需要准备一套一键安装器。
一条指令或一个按钮就能在VPS上快速部署Artpress。

# 最简单快速启动ArtPress的方法

一步一步来，绝壁不会错！

## 在Windows
### Step.1 安装Python3.x
建议Python 3.7.0以上

前往 [Python.org](https://www.python.org/downloads/)下载并安装Python。
**注意：请务必勾选Pypi，并将python添加到path中！**

### Step.2 使用pip安装django
打开cmd，输入指令`pip install django`等待完成即可。

在国内，pypi源可能会很慢。你可以考虑使用清华大学tuna提供的镜像源： 
[https://mirror.tuna.tsinghua.edu.cn/help/pypi/](https://mirror.tuna.tsinghua.edu.cn/help/pypi/)

### Step.3 运行它！
使用git clone或下载ZIP文件并解压来获得Artpress源代码，然后到代码根目录
（含有manage.py的目录）打开cmd执行命令：`python manage.py runserver localhost:8000`

如果一切没问题，你应该可以看到以下信息：

    Performing system checks...
    
    System check identified no issues (0 silenced).
    
    November 27, 2019 - 21:17:00
    Django version 2.2.7, using settings 'ArtPress.settings'
    Starting development server at http://localhost:8000/
    Quit the server with CTRL-BREAK.

### Step.4 打开浏览器
访问 [http://localhost:8000/](http://localhost:8000/)，欢迎光临！

## 在Linux
真正会用Linux的人照着Windows文档都能给他装上（我懒


# 我想参与这个项目！
我们团队目前正在招募中！

我们现在需要一些拥有Python、前端开发能力的人才。
（最好熟悉一款前端框架，但不限于Django）

**假如您是学生，想通过写项目提高能力；或者写代码是你的一项业余爱好。**

**且您愿意参与到我们的开发过程中**，欢迎通过邮箱联系我们：<lazyfox158@outlook.com>。

**请不用担心您很忙不便参与项目**，我们会根据实际情况，确保给您的**任务量不会影响您太多学习或工作的时间**！