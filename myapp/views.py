from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Generic function to handle CRUD operations
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def api(request, pk=None):
        # Handling GET method
        if request.method == 'GET':
            if pk:
                try:
                    obj = model_class.objects.get(pk=pk)
                    serializer = serializer_class(obj)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            objects = model_class.objects.all()
            serializer = serializer_class(objects, many=True)
            return Response(serializer.data)

        # Handling POST method
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Handling PUT method
        elif request.method == 'PUT':
            try:
                obj = model_class.objects.get(pk=pk)
                serializer = serializer_class(obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except model_class.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        # Handling DELETE method
        elif request.method == 'DELETE':
            try:
                obj = model_class.objects.get(pk=pk)
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except model_class.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    return api  # Return the view function

        

manage_customer = generic_api(Customer, CustomerSerializer)
manage_equipment = generic_api(Equipment, EquipmentSerializer)
manage_payment= generic_api(Payment, PaymentSerializer)
manage_booking= generic_api(Booking, BookingSerializer)
# Now, we can use this generic_api function for different views by passing the appropriate model and serializer.

# Customer CRUD operations
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def customer_view(request, pk=None):
    
#     return generic_api(request, Customer, CustomerSerializer, pk)

# # Equipment CRUD operations
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def equipment_view(request, pk=None):
#     return generic_api(request, Equipment, EquipmentSerializer, pk)

# # Booking CRUD operations
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def booking_view(request, pk=None):
#     return generic_api(request, Booking, BookingSerializer, pk)

# # Payment CRUD operations
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def payment_view(request, pk=None):
#     return generic_api(request, Payment, PaymentSerializer, pk)
