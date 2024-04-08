from rest_framework import serializers
from .models import Bill, BillProduct
from product_management.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']
        ref_name = 'BillingProduct'

class BillProductSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    product = ProductSerializer(read_only=True)  # Reference the model directly

    class Meta:
        model = BillProduct
        fields = ['product_id', 'product', 'quantity']

class BillSerializer(serializers.ModelSerializer):
    products = BillProductSerializer(source='billproduct_set', many=True)

    class Meta:
        model = Bill
        fields = ['id', 'customer', 'products', 'total_amount', 'created_at']

class BillCreateSerializer(serializers.ModelSerializer):
    products = BillProductSerializer(many=True)

    class Meta:
        model = Bill
        fields = ['id', 'customer', 'products']

    def create(self, validated_data):
        products = validated_data.pop('products')  # Get product IDs from data
        
        total = 0
        product_ids = []
        for product in products:
            product_ids.append(product['product_id'].id)
            total += product['product_id'].price * product['quantity']
        validated_data['total_amount'] = total

        bill = Bill.objects.create(**validated_data)
        bill.products.set(product_ids)  # Associate existing products using .set()
        return bill