from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Profile, Tabs, Orders, Attendance, Sales, Loss, Avaris, Expense, Purchases


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    picture_url = serializers.URLField(read_only=True, source='picture.url')

    class Meta:
        model = Profile
        fields = ('picture_url',)
        # readonly_fields = ('picture',)

    # def get_picture_url(self, obj):
    #     return self.context.build_absolute_uri(obj.picture_url)


class TabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabs
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField()

    # product_name = serializers.CharField(source='product.namePdt')

    class Meta:
        model = Orders
        fields = '__all__'
        # fields = ('product_name', 'product', 'orderNumber', 'quantity', 'amount', 'dateOp')


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class LossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loss
        fields = '__all__'


class AvarisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaris
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class PurchasesSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField()

    class Meta:
        model = Purchases
        fields = '__all__'

