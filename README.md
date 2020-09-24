# myblog
个人博客网站
* Django 自带的后台管理系统，方便对于文章、用户及其他动态内容的管理
* 文章分类、标签、浏览量统计以及规范的 SEO 设置
* 用户认证系统，在 Django 自带的用户系统的基础上扩展 Oauth2.0 认证，支持微博、Github 等第三方认证
* 文章评论系统，炫酷的输入框特效，支持 markdown 语法，二级评论结构和回复功能
* 信息提醒功能，登录和退出提醒，收到评论和回复提醒，信息管理
* 强大的全文搜索功能，只需要输入关键词就能展现全站与之关联的文章
* RSS 博客订阅功能及规范的 Sitemap 网站地图
* django-redis 支持的缓存系统，遵循缓存原则，加速网站打开速度
* 实用的在线工具，实现在线爬虫的接口调用
* 友情链接和推荐工具网站的展示
* RESTful API 风格的 API 接口
#网站支持
* 前端使用 Bootstrap4 + jQuery 支持响应式；图标使用 Font Awesome
* 后端 Python 3.6.8，Django 1.11.12，其他依赖查看源码中 requirements.txt
* 后台数据库使用 MySQL，缓存数据库使用 Redis
* 网站部署使用 Nginx + gunicorn，之前使用的 Nginx + uwsgi
* bootstrap-admin 用于美化后台管理系统，变成响应式界面
* django-allauth 等用于第三方用户登录
* django-haystack 和 jieba 用于支持全文搜索
* django-redis 缓存
* 使用 django restframework 支持的 RESTful 风格的 API 接口
* 其他依赖查看网站源码解释
