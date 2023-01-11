from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import SchoolModel, CityModel, AgeModel, LearnFormatModel


class CitySerializer(ModelSerializer):
    class Meta:
        model = CityModel
        # fields = '__all__'
        fields = ('id', 'name')


class AgeSerializer(ModelSerializer):
    class Meta:
        model = AgeModel
        # fields = '__all__'
        fields = ('id', 'name')


class LearnFormatSerializer(ModelSerializer):
    class Meta:
        model = LearnFormatModel
        # fields = '__all__'
        fields = ('id', 'name')


class SchoolSerializer(ModelSerializer):
    cities = CitySerializer(many=True, read_only=False)
    ages = AgeSerializer(many=True, read_only=False)
    learn_formats = LearnFormatSerializer(many=True, read_only=False)

    # logo = serializers.ReadOnlyField()

    # city = CitySerializer()

    class Meta:
        model = SchoolModel
        # read_only = ('logo',)
        fields = (
            'id', 'name', 'about', 'about', 'logo',
            'created_at', 'updated_at',
            'cities', 'ages', 'learn_formats'
        )
        extra_kwargs = {'logo': {'required': False}}
        # extra_kwargs = {
        #     'logo': {
        #         'read_only': True,
        #         'required': False
        #     }
        # }

        # exclude = ('user',)read_only=True

    # def create(self, validated_data):
    #     order = Order.objects.get(pk=validated_data.pop('event'))
    #     instance = Equipment.objects.create(**validated_data)
    #     Assignment.objects.create(Order=order, Equipment=instance)
    #     return instance

    def update(self, instance, validated_data):
        # Override tags_data = validated_data.pop('tags')
        # this way
        # request = self.context['request']
        # tags_data = request.data.get('tags', [])

        return instance

    def save(self, **kwargs):
        print('save')
        return super().save(**kwargs)


class AddLogoSerializer(ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = ('logo',)
        extra_kwargs = {
            'logo': {
                'read_only': False,
                'required': True
            }
        }
