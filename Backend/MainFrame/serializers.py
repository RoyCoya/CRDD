# serializers.py
from rest_framework import serializers
from .models import Test  # 替换成你的模型

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'  # 或者指定需要序列化的字段
