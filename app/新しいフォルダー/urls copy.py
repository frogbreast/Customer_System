from django.urls import path
from app import views

urlpatterns = [
    # 一覧表示
    path('', views.UserIndexView.as_view(), name='index'),
    # 詳細表示
    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='detail'),
    # 新規登録
    path('create', views.UserCreateView.as_view(), name='create'),
    # int型のプライマリーキーとなる、つまり「update/1/」や「update/2/」など
    # 更新・編集
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='update'),
    # 削除
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete'),
    
    # 利用記録
    # 利用日選択表示
    path('ur_date_list/', views.UR_DateListView.as_view(), name='ur_date_list'),
    # 登録
    path('ur_create', views.UR_CreateView.as_view(), name='ur_create'),
    # 利用時間帯の選択表示
    path('<slug:date_para>/', views.UR_UseSessionListView.as_view(), name='ur_session_list'),
    # 一覧表示
    path('ur_use_list/', views.UR_UseListView.as_view(), name='ur_use_list'),
]
