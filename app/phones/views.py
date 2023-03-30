from django.db.models import Sum, Count
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from knox import views as knox_views
from rest_framework.views import APIView
from rest_framework import serializers
from .permission import IsAuthenticatedOrReadOnlyAndOwner
from .serializer import RegisterS, DelUser, SetUser, SetPassword, AirPods_Seria, Phone_Seria, Phones_comments_Seria, \
    Phones_comments_Seria1, AirPods_comments_Seria, AirPods_comments_Seria1, Buscet_products_Seria, RegisterS2, \
    Buscet_products_Seria2
from .models import AirPods, Phones, Phone_comments, AirPods_comments, Bascet_products
from django_filters import rest_framework as filter

class CharFilterIn(filter.BaseInFilter,filter.CharFilter):
    pass
class PhonesFilter(filter.FilterSet):
    phone = CharFilterIn(field_name='brand',lookup_expr='in')
    corpus = CharFilterIn(field_name='corpus', lookup_expr='in')
    yadra = CharFilterIn(field_name='yadra', lookup_expr='in')
    front_kamera = CharFilterIn(field_name='front_kamera', lookup_expr='in')
    giga_vstoeno = CharFilterIn(field_name='giga_vstoeno', lookup_expr='in')
    giga_operate = CharFilterIn(field_name='giga_operate', lookup_expr='in')
    accumulator = CharFilterIn(field_name='accumulator', lookup_expr='in')
    class Meta:
        model = Phones
        fields = ['phone']
class ApiLogin(APIView):
    permission_classes = ()
    def post(self,request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)
        return Response({
            'user_info':{
                'id':user.id,
                'username':user.username,
                'email': user.email
            },
            'token':token
        })
@api_view(['GET'])
def get_api(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })
    return Response({'error':'not aut'},status=400)

class ApiCreate(APIView):
    permission_classes = ()
    def post(self,request):
        serializer = RegisterS(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        _,token = AuthToken.objects.create(user)
        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
            'token': token
        },status=201)
class ApiSetPassword(APIView):
    permission_classes = ()
    def put(self,request):
        user = request.user
        if not user.is_authenticated:
            return Response({"Error": "oops invalid token:)"})
        instance = User.objects.get(pk=user.id)
        seria = SetPassword(data=request.data,instance=instance)#instance то что сверх
        seria.is_valid(raise_exception=True)
        seria.save()#так как мы указали одновременно instance и data будет вызываться метод uodate
        return Response({'update': seria.data},status=200)
class ApiSetUser(APIView):
    permission_classes = ()
    def put(self,request):
        user = request.user
        if not user.is_authenticated:
            return Response({"Error": "oops invalid token:)"})
        instance = User.objects.get(pk=user.id)
        seria = SetUser(data=request.data,instance=instance)#instance то что сверх
        seria.is_valid(raise_exception=True)
        seria.save()#так как мы указали одновременно instance и data будет вызываться метод uodate
        return Response({'update': seria.data},status=200)
class ApiDelUser(APIView):
    permission_classes = ()
    def put(self,request):
        user = request.user
        if not user.is_authenticated:
            return Response({"Error": "oops invalid token:)"})
        instance = User.objects.get(pk=user.id)
        seria = DelUser(data=request.data,instance=instance)#instance то что сверх
        seria.is_valid(raise_exception=True)
        seria.save()#так как мы указали одновременно instance и data будет вызываться метод uodate
        return Response({'update': seria.data},status=204)
class Phones_APP(viewsets.ModelViewSet):
    queryset = Phones.objects.all() #берёт все данные
    serializer_class = Phone_Seria
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    filterset_class = PhonesFilter
class AirPods_APP(viewsets.ModelViewSet):
    queryset = AirPods.objects.all() #берёт все данные
    serializer_class = AirPods_Seria
class Get_Phone_slug_APP(APIView):
    permission_classes = ()
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)#pk работает как айди объекта
        if not pk:
            return Response({"Error":"wrong slug user"})
        try:
            instance=Phones.objects.get(slug=pk)
        except:
            return Response({"Error":"wrong slug user"})
        return Response({'phone': Phone_Seria(instance).data,
                        'similar': Phone_Seria(Phones.objects.filter(brand__in=[instance.brand]),many=True).data,
                        'also_buy': AirPods_Seria(AirPods.objects.filter(brand__in=[instance.brand]),many=True).data})
class Phones_comments_APP(APIView):
    queryset =  Phone_comments.objects.all()
    serializer_class = Phones_comments_Seria
    permission_classes = [IsAuthenticatedOrReadOnlyAndOwner]
    def get_queryset(self):
        id = self.kwargs['pk']
        jbj = Phone_comments.objects.get(id = id)
        return Phone_comments.objects.filter(id=jbj.id)
    def h1(self,kw,request):
        pk = kw.get('pk', None)  # pk работает как айди объекта
        if request.method == "GET":
            self.instance = Phone_comments.objects.all().filter(phone_id__in=[pk]).select_related('accounts','phone')
            if len(self.instance) == 0:
                raise serializers.ValidationError({1:'ok'})
        elif request.method == "PUT" or request.method == "DELETE":
            self.instance = Phone_comments.objects.get(id=pk)
    def post(self,request):
        user = request.user
        instance = User.objects.get(pk=user.id)
        serializer = Phones_comments_Seria(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user info": {"username":f"{user.username}"},
                                       "comment":"published"},status=201)
    def get(self,request,*args,**kwargs):
        try:
            self.h1(kwargs,request)
        except:
            return Response({"Error": "wrong id phone"})
        return Response(Phones_comments_Seria(self.instance,many=True).data)
    def put(self,request,*args,**kwargs):
        try:
            self.h1(kwargs, request)
        except:
            return Response({"Error": "wrong id phone"})
        serializer = Phones_comments_Seria1(data=request.data, instance=self.instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(Phones_comments_Seria(self.instance).data)
    def delete(self,request,*args,**kwargs):
        try:
            self.h1(kwargs,request)
        except:
            return Response({"Error": "wrong id phone"})
        id = self.instance.phone_id
        self.instance.delete()
        check = Phone_comments.objects.filter(phone_id=id).aggregate(total1=Sum('rate'),total2=Count('rate'))
        phone = Phones.objects.get(id=id)
        phone.rating = check['total1'] / check['total2']
        phone.save()
        return Response(status=204)
class Get_AirPod_slug_APP(APIView):
    permission_classes = ()
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)#pk работает как айди объекта
        if not pk:
            return Response({"Error":"wrong slug user"})
        try:
            instance=AirPods.objects.get(slug=pk)
        except:
            return Response({"Error":"wrong slug user"})
        return Response({'airpod':AirPods_Seria(instance).data,
                         'similar': AirPods_Seria(AirPods.objects.filter(brand__in=[instance.brand]), many=True).data,
                         'also_buy': Phone_Seria(Phones.objects.filter(brand__in=[instance.brand]), many=True).data}
                        )
class AirPods_comments_APP(APIView):
    queryset =  AirPods_comments.objects.all()#.prefetch_related('accounts','phone')
    serializer_class = AirPods_comments_Seria
    permission_classes = [IsAuthenticatedOrReadOnlyAndOwner]
    def get_queryset(self):
        id = self.kwargs['pk']
        jbj = AirPods_comments.objects.get(id = id)
        return AirPods_comments.objects.filter(id=jbj.id)

    def h1(self, kw, request):
        pk = kw.get('pk', None)  # pk работает как айди объекта
        if request.method == "GET":
            self.instance = AirPods_comments.objects.all().filter(airpod_id__in=[pk]).select_related('accounts', 'airpod')
            if len(self.instance) == 0:
                raise serializers.ValidationError({1: 'ok'})
        elif request.method == "PUT" or request.method == "DELETE":
            self.instance = AirPods_comments.objects.get(id=pk)
    def post(self,request):
        user = request.user
        instance = User.objects.get(pk=user.id)
        serializer = AirPods_comments_Seria(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user info": {"username":f"{user.username}"},
                                       "comment":"published"},status=201)
    def get(self,request,*args,**kwargs):
        try:
            self.h1(kwargs,request)
        except:
            return Response({"Error": "wrong id phone"})
        return Response(AirPods_comments_Seria(self.instance,many=True).data)
    def put(self,request,*args,**kwargs):
        try:
            self.h1(kwargs, request)
        except:
            return Response({"Error": "wrong id phone"})
        serializer = AirPods_comments_Seria1(data=request.data, instance=self.instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(AirPods_comments_Seria(self.instance).data)
    def delete(self,request,*args,**kwargs):
        try:
            self.h1(kwargs,request)
        except:
            return Response({"Error": "wrong id phone"})
        id = self.instance.airpod_id
        self.instance.delete()
        check = AirPods_comments.objects.filter(airpod_id=id).aggregate(total1=Sum('rate'),total2=Count('rate'))
        airpod = AirPods.objects.get(id=id)
        airpod.rating = check['total1'] / check['total2']
        airpod.save()
        return Response(status=204)
class Bascet_products_APP(APIView):
    queryset = Bascet_products.objects.all()
    serializer_class = Buscet_products_Seria
    permission_classes = [IsAuthenticatedOrReadOnlyAndOwner]
    def get_queryset(self):
        id = self.kwargs['pk']
        jbj = Bascet_products.objects.get(id = id)
        return Bascet_products.objects.filter(id=jbj.id)

    def h1(self, kw, request):
        pk = kw.get('pk', None)
        user=request.user# pk работает как айди объекта
        if request.method == "GET":
            if user.id == pk:
                self.instance = Bascet_products.objects.filter(accounts_id__in=[pk]) & Bascet_products.objects.filter(product_buy=False)
            else:
                raise serializers.ValidationError({1: 'ok'})
            if len(self.instance) == 0:
                raise serializers.ValidationError({1: 'ok'})
        elif request.method == "DELETE":
            self.instance = Bascet_products.objects.get(id=pk)
            if self.instance.product_buy == True:
                raise serializers.ValidationError({1: 'ok'})
        elif request.method == "PUT":
            self.instance = Bascet_products.objects.get(id=pk)
        elif request.method == "PATCH":
            self.instance = Bascet_products.objects.filter(accounts_id__in=[user.id]) & Bascet_products.objects.filter(
                product_buy=True)
            if len(self.instance) == 0:
                raise serializers.ValidationError({1: 'ok'})
        else:
            raise serializers.ValidationError({1: 'ok'})
    def post(self, request):
        user = request.user
        instance = User.objects.get(pk=user.id)
        serializer = Buscet_products_Seria(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user_info": {"username": f"{user.username}"},
                         "product": "published"}, status=201)
    def get(self,request,*args,**kwargs):
        try:
            self.h1(kwargs,request)
        except:
            return Response({"Error": "wrong id user"})
        return Response(Buscet_products_Seria(self.instance,many=True).data)
    def delete(self,request,*args,**kwargs):
        try:
            self.h1(kwargs,request)
        except:
            return Response({"Error": "wrong id phone"})
        self.instance.delete()
        return Response(status=204)
    def put(self,request,*args,**kwargs):
        try:
            self.h1(kwargs,request)
        except:
            return Response({"Error": "wrong id phone"})
        serializer = Buscet_products_Seria2(data=request.data, instance=self.instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(Buscet_products_Seria(self.instance).data)
    def patch(self,request,*args,**kwargs):
        try:
            self.h1(kwargs,request)
        except:
            return Response({"Error": "wrong id phone"})
        return Response(Buscet_products_Seria(self.instance,many=True).data)