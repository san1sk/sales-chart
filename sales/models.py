from django.db import models

# Create your models here.

class salesData(models.Model):
    
    # SalesData model to store sales records.
    id=models.AutoField(primary_key=True)
    saleDate=models.DateField()
    amount=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        # String representaion of of salesData instance
        return f"Sale on {self.saleDate} for {self.amount}"



