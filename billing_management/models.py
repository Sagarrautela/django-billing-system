from django.db import models
from authentication.models import User
from product_management.models import Product
from customer_management.models import Customer

class Bill(models.Model):
    # Relationship
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_bills')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_bills')
    products = models.ManyToManyField(Product, through='BillProduct')

    # Othe fields
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100, default="Cash")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Bill for {self.customer.name} - ${self.total_amount}"

class BillProduct(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product in the bill

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Bill {self.bill.id}"    
    

    
