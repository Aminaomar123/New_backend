# myapp/serializers.py
from rest_framework import serializers
from .models import Customer, Equipment, Booking, Payment

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' 


# myapp/serializers.py
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__' 

# myapp/serializers.py
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  

# myapp/serializers.py
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  # Include all fields of the Payment model



