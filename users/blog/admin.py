from django.contrib import admin
from .models import Article, Tag, Category, Carousel, FriendLink, Timeline


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
    list_display = ('id', 'title', 'author', 'create_date', 'update_date')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'content', 'img_url', 'url')

@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'link', 'create_date', 'is_active', 'is_show')
    date_hierarchy = 'create_date'
    list_filter = ('is_active', 'is_show')

@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('title', 'side', 'update_date', 'icon', 'icon_color',)
    fieldsets = (
        ('图标信息', {'fields': (('icon', 'icon_color'),)}),
        ('时间位置', {'fields': (('side', 'update_date', 'star_num'),)}),
        ('主要内容', {'fields': ('title', 'content')}),
    )
    date_hierarchy = 'update_date'
    list_filter = ('star_num', 'update_date')


# 自定义管理站点的名称和URL标题
admin.site.site_header = '网站管理'
admin.site.site_title = '博客后台管理'


 
 

 