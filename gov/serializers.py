from django.contrib.auth.models import User, Group
from rest_framework import serializers
from gov.models import Gov_history


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # gov = serializers.HyperlinkedRelatedField(many=True, view_name='gov-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GovSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Gov_history
        fields = ('url', 'id', 'vin', 'productNo', 'created', 'color_code', 'paperNo', 'COANo', 'owner')

    # id = serializers.IntegerField(read_only=True)
    # vin = serializers.CharField(required=False)
    # productNo = serializers.CharField(required=False)
    # color_code = serializers.CharField(required=False)
    # paperNo = serializers.CharField(required=False)
    # COANo = serializers.CharField(required=False)
    #
    # def create(self, validated_data):
    #     """
    #     根据提供的验证过的数据创建并返回一个新的`gov`实例。
    #     """
    #     return Gov_history.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     根据提供的验证过的数据更新和返回一个已经存在的`gov`实例。
    #     """
    #     instance.vin = validated_data.get('vin', instance.vin)
    #     instance.productNo = validated_data.get('productNo', instance.productNo)
    #     instance.color_code = validated_data.get('color_code', instance.color_code)
    #     instance.paperNo = validated_data.get('paperNo', instance.paperNo)
    #     instance.COANo = validated_data.get('COANo', instance.COANo)
    #     instance.save()
    #     return instance


