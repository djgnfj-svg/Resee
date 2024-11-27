from django.db import models

class TimeStampedModel(models.Model):
    """
    공통적으로 사용하는 생성/수정 시간 필드를 제공하는 추상 베이스 모델.
    """
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시 자동 기록
    updated_at = models.DateTimeField(auto_now=True)      # 저장 시 자동 갱신

    class Meta:
        abstract = True  # 이 모델은 데이터베이스 테이블로 생성되지 않음
