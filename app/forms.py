from django.forms import ModelForm
from app.models import UserOverview, UsageRecord

class UserOverviewForm(ModelForm):
    class Meta:
        # modelの指定
        model = UserOverview
        # 入力をする項目を指定
        fields = ("name", "birthday", "gender", "zip_code1", "zip_code2", "address", "phone_number", "temperature",)
   
class UsageRecordForm(ModelForm):
    class Meta:
        model = UsageRecord
        fields = ("useroverview_fk","use_session",)
