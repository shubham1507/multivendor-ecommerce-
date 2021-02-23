from rest_framework import serializers
from .models import *


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('company_name',)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
     

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):

    seller = SellerSerializer(required=True)

    customer = CustomerSerializer(required=True)

    admin = AdminSerializer(required=True)

    class Meta:
        model = User
        fields = '__all__'
        # lookup_field = 'username'
        # fields = ('url', 'username', 'address_line_1', 'address_line_2',
        #           'first_name', 'last_name', 'email', 'phone', 'image',
        #           'password', 'is_seller', 'vendor', 'customer')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data.get('user_type') == 1:
            print(validated_data)
            user_type = validated_data.pop('user_type')
            profile_data = validated_data.pop('seller')
            password = validated_data.pop('password')
            email = validated_data.pop('email')
            username = validated_data.pop('username')
            first_name = validated_data.pop('first_name')
            last_name = validated_data.pop('last_name')
            address_line_1 = validated_data.pop('address_line_1')
            address_line_2 = validated_data.pop('address_line_2')
            contact = validated_data.pop('contact')
            alt_contact = validated_data.pop('alt_contact')
            user = User(email=email,
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        address_line_1=address_line_1,
                        address_line_2=address_line_2,
                        contact=contact,
                        alt_contact=alt_contact)
            user.set_password(password)
            user.is_active = False
            user.save()
            Seller.objects.create(user=user, **profile_data)
            return user

        elif validated_data.get('user_type') == 2:

            profile_data = validated_data.pop('customer')
            password = validated_data.pop('password')
            email = validated_data.pop('email')
            username = validated_data.pop('username')
            user_type = validated_data.pop('user_type')
            address_line_1 = validated_data.pop('address_line_1')
            address_line_2 = validated_data.pop('address_line_2')
            contact = validated_data.pop('contact')
            alt_contact = validated_data.pop('alt_contact')
            user = User(email=email,
                        username=username,
                        address_line_1=address_line_1,
                        address_line_2=address_line_2,
                        phone=phone,
                        contact=contact,
                        alt_contact=alt_contact)
            user.set_password(password)

            # for customer login approval from admin post info check
            user.is_active = False
            user.save()
            Customer.objects.create(user=user, **profile_data)
            return user

        else:

            profile_data = validated_data.pop('admin')
            password = validated_data.pop('password')
            email = validated_data.pop('email')
            username = validated_data.pop('username')
            user_type = validated_data.pop('user_type')
            address_line_1 = validated_data.pop('address_line_1')
            address_line_2 = validated_data.pop('address_line_2')
            contact = validated_data.pop('contact')
            alt_contact = validated_data.pop('alt_contact')
            user = User(email=email,
                        username=username,
                        address_line_1=address_line_1,
                        address_line_2=address_line_2,
                        phone=phone,
                        contact=contact,
                        alt_contact=alt_contact)
            user.set_password(password)

            # for customer login approval from admin post info check
            user.is_active = False
            user.save()
            Admin.objects.create(user=user, **profile_data)
            return user

    def update(self, instance, validated_data):

        if validated_data.get('user_type') == 1:

            profile_data = validated_data.pop('seller')
            # profile = instance.profile
            seller = instance.vendor

            instance.email = validated_data.get('email', instance.email)
            instance.save()
            vendor.deliverylt = profile_data.get('deliverylt',
                                                 vendor.deliverylt)
            vendor.company_name = profile_data.get('company_name',
                                                 seller.company_name)
            
            address_line_1 = profile_data.get('address_line_1',
                                              seller.address_line_1)
            address_line_2 = profile_data.get('address_line_2',
                                              seller.address_line_2)
            contact = profile_data.get('contact', seller.contact)
            alt_contact = profile_data.get('alt_contact', seller.alt_contact)
            seller.save()

            return instance

        elif validated_data.get('user_type') == 2:

            profile_data = validated_data.pop('customer')

            customer = instance.customer

            instance.email = validated_data.get('email', instance.email)

            instance.save()

            
            instance.address1 = validated_data.get(
                'address1', instance.address_line_1)

            instance.address2 = validated_data.get(
                'address2', instance.address_line_2)
            instance.alt_contact = validated_data.get('contact', instance.alt_contact)
            instance.save()
            customer.save()

            return instance

        else:

            profile_data = validated_data.pop('admin')

            customer = instance.customer

            instance.email = validated_data.get('email', instance.email)

            instance.save()

            
            instance.address1 = validated_data.get(
                'address1', instance.address_line_1)

            instance.address2 = validated_data.get(
                'address2', instance.address_line_2)
            instance.alt_contact = validated_data.get('contact', instance.alt_contact)
            instance.save()
            customer.save()

            return instance





    
