from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expenses(models.Model):
    CATEGORY_CHOICE=(
        ("food","food"),
        ("bill","bill"),
        ("fuel","fuel")
    )
    PAYMENT_CHOICE=(
        ("UPI","UPI"),
        ("card","card")
    )
    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICE,default="food")
    payment=models.CharField(max_length=100,choices=PAYMENT_CHOICE,default="UPI")

    def __str__(self):
        return f"{self.title} - {self.amount}"