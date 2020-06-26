from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    views = indexes.IntegerField(model_attr='views')

    # 给哪个模型服务
    def get_model(self):
        return Article

    # 返回模型的值
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
