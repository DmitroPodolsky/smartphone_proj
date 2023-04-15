from django.db.models import Sum, Count
from rest_framework import serializers, validators
from django.contrib.auth.models import User
from .models import AirPods, Phones, Phone_comments, AirPods_comments, Bascet_products


class RegisterS(serializers.ModelSerializer):
    new_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'new_password', 'email')  # ,'first_name','last_name')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), 'a user have that email'
                    )
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        new_password = self.validated_data['new_password']
        if password != new_password:
            raise serializers.ValidationError({f'password: not correct'})
        user = User.objects.create(
            username=username,
            password=password,
            email=email,
        )
        user.set_password(password)
        user.save()
        return user


class RegisterS2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')  # ,'first_name','last_name')
        extra_kwargs = {
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), 'a user have that email'
                    )
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        user = User.objects.create(
            username=username,
            email=email,
        )
        user.save()
        return user


class SetPassword_No(serializers.ModelSerializer):
    new_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True)
    check_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True)
    your_email = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['new_password', 'check_password', 'your_email']

    def create(self, validated_data):
        check_password = self.validated_data['check_password']
        new_password = self.validated_data['new_password']
        your_email = self.validated_data['your_email']
        if check_password != new_password:
            raise serializers.ValidationError({f'password: not correct password'})
        instance1 = User.objects.get(email=your_email)
        instance1.set_password(check_password)
        instance1.is_active=False
        instance1.save()
        return instance1


class SetPassword(serializers.ModelSerializer):
    new_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True)
    current_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True)

    class Meta:
        model = User
        fields = ['new_password', 'current_password']

    def update(self, instance: User, validated_data):
        current_password = self.validated_data['current_password']
        new_password = self.validated_data['new_password']
        a = instance.check_password(current_password)
        if a is False:
            raise serializers.ValidationError({f'password: not correct password'})
        instance.set_password(new_password)
        instance.save()
        return instance


class SetUser(serializers.ModelSerializer):
    new_user = serializers.CharField(max_length=20, write_only=True)
    current_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['new_user', 'current_password']

    def update(self, instance: User, validated_data):
        current_password = self.validated_data['current_password']
        a = instance.check_password(current_password)
        if a is False:
            raise serializers.ValidationError({f'password: not correct password'})
        new_user = self.validated_data['new_user']
        try:
            a = User.objects.get(username=new_user)
        except:
            instance.username = new_user
            instance.save()
            return instance
        raise serializers.ValidationError({'username': 'this name already exist'})


class DelUser(serializers.ModelSerializer):
    current_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['current_password']

    def update(self, instance: User, validated_data):
        current_password = self.validated_data['current_password']
        a = instance.check_password(current_password)
        if a is False:
            raise serializers.ValidationError({f'password: not correct password'})
        return instance.delete()


class Phone_Seria(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = '__all__'


class AirPods_Seria(serializers.ModelSerializer):
    class Meta:
        model = AirPods
        fields = '__all__'


class Phones_comments_Seria(serializers.ModelSerializer):
    phone_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Phone_comments
        fields = '__all__'  # ('comment','phone_id')

    def update(self, instance, validated_data):
        comments = validated_data.get('comment')
        restorans_id = validated_data.get('phone_id')
        rating = validated_data.get('rate')
        user = Phone_comments.objects.create(
            comment=comments,
            phone_id=restorans_id,
            accounts_id=instance.id,
            rate=rating,
            username=instance.username
        )
        user.save()
        check = Phone_comments.objects.filter(phone_id=restorans_id).aggregate(total1=Sum('rate'), total2=Count('rate'))
        phone = Phones.objects.get(id=restorans_id)
        phone.rating = check['total1'] / check['total2']
        phone.save()
        return user


class Phones_comments_Seria1(serializers.ModelSerializer):
    comments = serializers.CharField(max_length=1000, write_only=True)

    class Meta:
        model = Phone_comments
        fields = ['comments', 'rate']  # ('comment','phone_id')

    def update(self, instance, validated_data):
        new_comment = self.validated_data['comments']
        new_rate = self.validated_data['rate']
        instance.comment = new_comment
        instance.rate = new_rate
        instance.save()
        check = Phone_comments.objects.filter(phone_id=instance.phone_id).aggregate(total1=Sum('rate'),
                                                                                    total2=Count('rate'))
        phone = Phones.objects.get(id=instance.phone_id)
        phone.rating = check['total1'] / check['total2']
        phone.save()
        return instance


class AirPods_comments_Seria(serializers.ModelSerializer):
    airpod_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = AirPods_comments
        fields = '__all__'  # ('comment','phone_id')

    def update(self, instance, validated_data):
        comments = validated_data.get('comment')
        restorans_id = validated_data.get('airpod_id')
        rating = validated_data.get('rate')
        user = AirPods_comments.objects.create(
            comment=comments,
            airpod_id=restorans_id,
            accounts_id=instance.id,
            rate=rating,
            username=instance.username
        )
        user.save()
        check = AirPods_comments.objects.filter(airpod_id=restorans_id).aggregate(total1=Sum('rate'),
                                                                                  total2=Count('rate'))
        airpod = AirPods.objects.get(id=restorans_id)
        airpod.rating = check['total1'] / check['total2']
        airpod.save()
        return user


class AirPods_comments_Seria1(serializers.ModelSerializer):
    comments = serializers.CharField(max_length=1000, write_only=True)

    class Meta:
        model = AirPods_comments
        fields = ['comments', 'rate']  # ('comment','phone_id')

    def update(self, instance, validated_data):
        new_comment = self.validated_data['comments']
        new_rate = self.validated_data['rate']
        instance.comment = new_comment
        instance.rate = new_rate
        instance.save()
        check = AirPods_comments.objects.filter(airpod_id=instance.airpod_id).aggregate(total1=Sum('rate'),
                                                                                        total2=Count('rate'))
        airpod = AirPods.objects.get(id=instance.airpod_id)
        airpod.rating = check['total1'] / check['total2']
        airpod.save()
        return instance


class Buscet_products_Seria(serializers.ModelSerializer):
    class Meta:
        model = Bascet_products
        fields = '__all__'

    def update(self, instance, validated_data):
        group_product = validated_data.get('group_product')
        product_id = validated_data.get('product_id')
        count = validated_data.get('count')
        try:
            if group_product == 1:
                product = Phones.objects.get(id=product_id)
            elif group_product == 2:
                product = AirPods.objects.get(id=product_id)
            else:
                raise serializers.ValidationError({'error': 'this group does not exist'})
        except:
            raise serializers.ValidationError({'error': 'this product does not exist'})
        if not count:
            count = 1
        price = int(product.price) * count
        try:
            check = Bascet_products.objects.filter(slug__in=[product.slug]) & Bascet_products.objects.filter(
                product_buy=False) & Bascet_products.objects.filter(accounts_id__in=[instance.id])
            if len(check) == 0:
                5 / 'ol'
        except:
            user = Bascet_products.objects.create(
                group_product=group_product,
                product_id=product_id,
                accounts_id=instance.id,
                name=product.name,
                price=price,
                count=count,
                slug=product.slug,
                image=product.photo1
            )
        else:
            raise serializers.ValidationError({'slug': 'this slug is already exist1'})
        user.save()
        return user


class Buscet_products_Seria2(serializers.ModelSerializer):
    count = serializers.IntegerField(write_only=True)

    class Meta:
        model = Bascet_products
        fields = ['count']

    def update(self, instance, validated_data):
        count = validated_data.get('count')
        instance.price = (int(instance.price) / instance.count) * count
        instance.count = count
        instance.save()
        return instance
