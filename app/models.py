from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# 利用者概要のモデル
class UserOverview(models.Model):
    # 性別選択リスト
    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'その他'),
    )
    
    # 主キー カード番号
    id = models.AutoField(
        verbose_name = 'カード番号',
        primary_key = True,
    )

    # 名前
    name = models.CharField(
        verbose_name = '氏名',
        max_length = 200,  
    )
    
    # 生年月日
    birthday = models.DateField(
        verbose_name = '生年月日',
    )
    
    # 性別
    gender = models.IntegerField(
        verbose_name = '性別',
        choices = GENDER_CHOICES,
        default = 1,
    )
    
    # 郵便番号1
    zip_code1 = models.CharField(
        verbose_name = '郵便番号1',
        max_length = 3,
    )
    # 郵便番号2
    zip_code2 = models.CharField(
        verbose_name = '郵便番号2',
        max_length = 4,
    )

    # 住所
    address = models.CharField(
        verbose_name = '住所',
        max_length = 200,
    )
    
    # 電話番号
    phone_number = models.CharField(
        verbose_name = '電話番号',
        max_length = 20,
    )
    
    # 体温
    temperature = models.DecimalField(
        verbose_name = '体温',
        max_digits = 3,
        decimal_places = 1,
    )
    
    # 作成日
    created_date = models.DateField(
        verbose_name = '作成日',
        auto_now_add = True,
    )
    
    # 以下は管理サイト上の表示設定
    def __str__(self):
        return str(self.id)

    class Meta:
        # verbose_name = '利用者概要'
        # ↑ 下記が明記されている場合は上記は要らず
        # ↓ 複数形のsを付けないために必要
        verbose_name_plural = '利用者概要'
        

# 利用記録のモデル
class UsageRecord(models.Model): 
    # 利用日
    use_date = models.DateField(
        verbose_name = '利用日',
        auto_now_add = True,
    )
    
    # 利用時間帯リスト
    SESSION_CHOICES = (
        (1, '午前の部'),
        (2, '午後の部'),
        (3, '夜の部'),
    )
    
    # 利用時間帯(何の部か)
    use_session = models.IntegerField(
        verbose_name = '利用時間帯',
        choices = SESSION_CHOICES,
        default = 1,
    )
    
    # 外部キー 利用者概要 カード番号
    useroverview_fk = models.ForeignKey(
        UserOverview, 
        on_delete = models.CASCADE,
        to_field = 'id',
    )
        
    # 以下は管理サイト上の表示設定
    def __str__(self):
        # 文字列にしないとエラーを起こす為
        return str(self.use_date)

    class Meta:
        # ↑ 下記が明記されている場合は上記は要らず
        # ↓ 複数形のsを付けないために必要
        verbose_name_plural = '利用記録'


