from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, CategoryListView, AddCommentView, CategoryView_2, CategoryListView_2

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('category_2/<str:cats>/', CategoryView_2, name='category_2'),
    path('category-list_2/', CategoryListView_2, name='category-list_2'),
    ]