import json
import datetime

import stripe
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import redirect
from django.views import View
from django.conf import settings
from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .models import Phones,Bascet_products,AirPods

stripe.api_key = settings.STRIPE_SECRET_KEY


'''class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class ProductLandingPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        product = Bascet_products.objects.get(id=1)
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context'''

@csrf_exempt
def CreateCheckoutSessionView(request, *args, **kwargs):
    if request.method == 'POST':
        product_id = kwargs['pk']
        product = Bascet_products.objects.filter(accounts_id=product_id) & Bascet_products.objects.filter(product_buy=False)
        product = product.aggregate(total1=Sum('price'))
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': round(product['total1']/11386)*100,
                        'product_data': {
                            'name': 'общая сумма всех товаров'
                            # 'images' тут изображение может быть товара
                        }

                    },
                    'quantity': 1,
                },
            ],
            metadata={'id':product_id},
            mode='payment',
            success_url='http://smartshopcenter.org:3000',
            cancel_url='http://smartshopcenter.org:3000',
        )
        #stripe_checkout_url = f'https://checkout.stripe.com/c/pay/{checkout_session.id}'
        return JsonResponse({'id': checkout_session.url})


'''@csrf_exempt
def stripe_webhook(request):
    payload = request.body

    # For now, you only need to print out the webhook payload so you can see
    # the structure.
    print(payload)

    return HttpResponse(status=200)'''#для проверки перехвата запросов с нашего сайта stripe

def get_time():
    delta = datetime.timedelta(hours=5,minutes=0)
    return datetime.datetime.now(datetime.timezone.utc)+delta

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = event['data']['object']
        customer_email = session['customer_details']['email']
        print(customer_email)
        products = Bascet_products.objects.filter(accounts_id=session['metadata']['id']) & Bascet_products.objects.filter(product_buy=False)
        check_in=0
        check_in_inf = False
        for i in products:
            a=0
            if i.group_product == 1:
                change = Phones.objects.get(id=i.product_id)
                change.count-=i.count
                if change.count < 0:
                    change.count += i.count
                    a = 1
                    send_mail(
                        subject=f"{change.name}",
                        message=f"к сожалению данного продукта пока нету в наличии. вся оплата будет возращена за данный товар. С вами свяжеться техническая поддержка в ближайшое время доставки в ближайшое время",
                        recipient_list=[customer_email],
                        from_email="matt@test.com"
                    )
                else:
                    change.save()
            elif i.group_product == 2:
                change = AirPods.objects.get(id=i.product_id)
                change.count-=i.count
                if change.count<0:
                    change.count+=i.count
                    a=1
                    send_mail(
                        subject=f"{change.name}",
                        message=f"к сожалению данного продукта пока нету в наличии. вся оплата будет возращена за данный товар. С вами свяжеться техническая поддержка в ближайшое время доставки в ближайшое время",
                        recipient_list=[customer_email],
                        from_email="matt@test.com"
                    )
                else:
                    change.save()
            if a==0:
                check_in_inf = True
                i.product_buy = True
                i.time = get_time()
                i.save()
            else:
                check_in=1
        if check_in==0:
            send_mail(
                subject=f"Вот ваши товары",
                message=f"Спасибо за оплату. Ваши товары уже в заказе и в пути. С вами свяжеться служба доставки в ближайшое время",
                recipient_list=[customer_email],
                from_email="matt@test.com"
            )
        elif check_in==1 and check_in_inf==True:
            send_mail(
                subject=f"Вот ваши товары",
                message=f"Спасибо за оплату. Ваши товары уже в заказе и в пути.Некоторые товари были отменены в ходе оплаты, вам деньги компенсирует администрация. С вами свяжеться служба доставки в ближайшое время",
                recipient_list=[customer_email],
                from_email="matt@test.com"
            )
        else:
            send_mail(
                subject=f"Отмена покупки",
                message=f"Данные товари которые вы заказывали были отменены так как их в наличии нету,вам в ближайшое время компенсируют полностью затраты",
                recipient_list=[customer_email],
                from_email="matt@test.com"
            )
    '''elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        stripe_customer_id = intent["customer"]
        stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

        customer_email = stripe_customer['email']
        product_id = intent["metadata"]["product_id"]

        product = Bascet_products.objects.get(id=product_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.price}",
            recipient_list=[customer_email],
            from_email="matt@test.com"
        )'''
    # Passed signature verification
    return HttpResponse(status=200)
class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            product_id = self.kwargs["pk"]
            product = Bascet_products.objects.get(id=product_id)
            intent = stripe.PaymentIntent.create(
                amount=product.price,
                currency='usd',
                customer=customer['id'],
                metadata={
                    "product_id": product.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({ 'error': str(e) })