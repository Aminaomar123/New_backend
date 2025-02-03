from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, default='Customer')  
    email = models.EmailField(max_length=100, default='email.@gmail.com')  
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Equipment(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='General')  
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='equipment_images/', null=True, blank=True)  

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.customer.name} - {self.equipment.name}"

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateTimeField(auto_now_add=True, blank=True, null= True)
    status = models.CharField(max_length=20, default='Pending')  

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.status}"
