from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from requests import session
from app.models import UserOverview, UsageRecord
from app.forms import UserOverviewForm, UsageRecordForm
from django.urls import reverse_lazy

# 一覧表示ビュー
# 検索機能あり
class UserIndexView(ListView):
    # 表示するhtmlの指定
    template_name = "app/useroverview/index.html"
    # modelの指定
    #model = UserOverview
    # オブジェクト名をuseroverviewsに指定
    # htmlにて情報を指定する場合に使用
    # 定義しなかった場合、デフォルトで
    # 'モデルクラス名' (小文字) が設定されることになる
    context_object_name = "useroverviews"
    # ページング機能
    paginate_by = 10
    
    # 検索機能追加の為
    # viewが表示するオブジェクトのクエリセットを
    # 返すために使用
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            # 部分一致
            name_list = UserOverview.objects.filter(name__icontains = query)
        else:
            # 全てを表示
            name_list = UserOverview.objects.all()
        # 降順に整列
        name_list = UserOverview.objects.order_by('-id')
        return name_list

# 詳細表示ビュー
class UserDetailView(DetailView):
    template_name = "app/useroverview/detail.html"
    model = UserOverview
    context_object_name = "userdetailviews"

# 作成ビュー
class UserCreateView(CreateView):
    template_name = "app/useroverview/create.html"
    model = UserOverview
    # form_classの指定 (forms.pyでクラス定義)
    form_class = UserOverviewForm
    # 登録成功時に遷移する
    success_url = reverse_lazy("index")
    
# 更新・編集ビュー
class UserUpdateView(UpdateView):
    template_name = "app/useroverview/update.html"
    model = UserOverview
    form_class = UserOverviewForm
    success_url = reverse_lazy("index")
    
# 削除ビュー
class UserDeleteView(DeleteView):
    template_name = "app/useroverview/index.html"
    model = UserOverview
    success_url = reverse_lazy("index")


# 利用日一覧ビュー
class UR_DateListView(ListView):
    template_name = "app/usagerecord/date_list.html"
    #model = UsageRecord
    context_object_name = "usagerecords"
    paginate_by = 10
    
    def get_queryset(self):
        # 全データを取得
        date_lists = UsageRecord.objects.raw('SELECT * FROM usagerecords')
        # 降順に整列
        date_lists = UsageRecord.objects.order_by('-use_date')
        # 重複を非表示
        date_lists = UsageRecord.objects.values('use_date').distinct()
        
        return date_lists

# 利用日登録ビュー
class UR_CreateView(CreateView):
    template_name = "app/usagerecord/create.html"
    model = UsageRecord
    # form_classの指定 (forms.pyでクラス定義)
    form_class = UsageRecordForm
    # 登録成功時に遷移する
    success_url = reverse_lazy("ur_date_list")

# 利用時間帯一覧ビュー
class UR_UseSessionListView(ListView):
    template_name = "app/usagerecord/session_list.html"
    model = UsageRecord
    context_object_name = "ur_sessionviews"
    paginate_by = 10
    
    def get_queryset(self):
        # 全データを取得
        #session_lists = UsageRecord.objects.all()
        # キーを取得
        date_parameter = self.kwargs['date_para']
        # 選択した日にちのみ
        session_lists = UsageRecord.objects.filter(use_date__iexact = date_parameter)
        # 重複を非表示
        #session_lists = UsageRecord.objects.values('use_session').values('use_date').distinct()

        print(session_lists)
        return session_lists

# 一覧ビュー
class UR_UseListView(ListView):
    template_name = "app/usagerecord/use_list.html"
    model = UsageRecord
    context_object_name = "usagerecords"
    paginate_by = 10

