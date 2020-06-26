from django.urls import path 
from .views import IndexView,ArchiveView,DetailView,CategoryView,TagView,TimelineView,AboutView,MySearchView

app_name = 'blog'

urlpatterns = [
	path('', IndexView.as_view(), name='index'),#主页自然排序
    path('hot/', IndexView.as_view(), {'sort': 'v'}, name='index_hot'),#主页按照浏览量排序
	path('archive/', ArchiveView.as_view(), name='archive'),#归档页面
	path('article/<int:pk>/', DetailView.as_view(), name='detail'),  # 文章内容页
	path('category/<int:pk>/', CategoryView.as_view(), name='category'),#分类
    path('category/<int:pk>/hot/', CategoryView.as_view(), {'sort': 'v'},name='category_hot'),
    path('tag/<int:pk>/', TagView.as_view(), name='tag'),#标签
    path('tag/<int:pk>/hot/', TagView.as_view(), {'sort': 'v'}, name='tag_hot'),#标签
    path('timeline/', TimelineView.as_view(), name='timeline'),#timeline页面
    path('about/', AboutView, name='about'),  # About页面
    path('search/', MySearchView.as_view(), name='search_view'),#全文搜索
]