import datetime
import stripe
from django.core.mail import send_mail
from django.db.models import Sum
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Phones, Bascet_products, AirPods

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def CreateCheckoutSessionView(request, *args, **kwargs):
    if request.method == 'POST':
        product_id = kwargs['pk']
        product = Bascet_products.objects.filter(accounts_id=product_id) & Bascet_products.objects.filter(
            product_buy=False)
        product = product.aggregate(total1=Sum('price'))
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': round(product['total1'] / 11386) * 100,
                        'product_data': {
                            'name': 'общая сумма всех товаров'
                        }

                    },
                    'quantity': 1,
                },
            ],
            metadata={'id': product_id},
            mode='payment',
            success_url='http://localhost:3000',#'http://smartshopcenter.org:3000',
            cancel_url='http://localhost:3000'#'http://smartshopcenter.org:3000',
        )
        return JsonResponse({'id': checkout_session.url})


def get_time():
    delta = datetime.timedelta(hours=5, minutes=0)
    return datetime.datetime.now(datetime.timezone.utc) + delta


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
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session['customer_details']['email']
        print(customer_email)
        products = Bascet_products.objects.filter(
            accounts_id=session['metadata']['id']) & Bascet_products.objects.filter(product_buy=False)
        check_in = 0
        check_in_inf = False
        for i in products:
            a = 0
            if i.group_product == 1:
                change = Phones.objects.get(id=i.product_id)
                change.count -= i.count
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
                change.count -= i.count
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
            if a == 0:
                check_in_inf = True
                i.product_buy = True
                i.time = get_time()
                i.save()
            else:
                check_in = 1
        if check_in == 0:
            send_mail(
                subject=f"Вот ваши товары",
                message=f"Спасибо за оплату. Ваши товары уже в заказе и в пути. С вами свяжеться служба доставки в ближайшое время",
                recipient_list=[customer_email],
                from_email="matt@test.com"
            )
        elif check_in == 1 and check_in_inf == True:
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
    return HttpResponse(status=200)
