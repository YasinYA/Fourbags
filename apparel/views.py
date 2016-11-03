import json

from django.conf import settings
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http  import JsonResponse, HttpResponse

from .models  import Item, Order
from utils.email import send_email

class HomeView(TemplateView):
    template_name = 'apparel/apparel_base.html'


class MenPageView(ListView):
    model = Item
    template_name = 'apparel/men_page.html'
    context_object_name = 'men_items'

    def get_queryset(self):
        return Item.objects.filter(gender="Men")


class WomenPageView(ListView):
    model = Item
    template_name = 'apparel/women_page.html'
    context_object_name = 'women_items'

    def get_queryset(self):
        return Item.objects.filter(gender='Women')


class DetailPageView(DetailView):
    model = Item
    template_name = "apparel/detail_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DetailPageView, self).get_context_data(*args, **kwargs)
        return context


class ItemOrderView(TemplateView):
    template_name = 'apparel/ordering_form.html'
    context_object_name = 'item'

    def get_context_data(self, *args, **kwargs):
        context = super(ItemOrderView, self).get_context_data(*args, **kwargs)
        context['item'] = Item.objects.get(pk=kwargs['pk']).serialize()
        return context


class OrderView(View):

    def post(self, request):
        # get the data from request body cos angular sends the data in the request body
        # which django doesn't bother to look at
        # since request body is a byte format try to serialize
        data = json.loads(request.body.decode('utf-8'))
        item = data.get('item', '')

        # check if quantity is sent with the data and it is greater then 0
        if  not data.get('item_quantity') and data['item_quantity'] <= 0:
            return HttpResponse(status=404)

        #  TODO: validate the email using django validation
        # check if there is email
        if data.get('email', ''):
            email_template = 'apparel/email/order_email.html'
            email_subject = "Fourbags"
            ctx = {
                "item": item,
                "firstname": data.get('first_name', ''),
                "lastname": data.get('last_name', ''),
                "phone": data.get('phone', ''),
                "address": data.get('address', ''),
                "quantity": data['item_quantity'],
            }
            to_email = data.get('email')
            from_email = settings.EMAIL_HOST_USER


        # get if data has item property
        if item:
            # check if that item exists (double checking)
            try:
                ordered_item = Item.objects.get(pk=item.get('id', ''))
            except Item.DoesNotExist:
                return HttpResponse(status=404)
            else:
                # Finally create order object
                Order.objects.create(
                    item=ordered_item,
                    first_name=data.get('first_name', ''),
                    last_name=data.get('last_name', ''),
                    phone=data.get('phone', ''),
                    email=data.get('email', ''),
                    address=data.get('address', ''),
                    quantity=data['item_quantity'],
                    paypal=data.get('paypal', False),
                    cash_on_delivery=data.get('cash_on_delivery', True)
                )

                # send the mail
                send_email(email_subject, email_template, ctx, to_email, from_email)
        return JsonResponse({
            "success": True
        })


class OrderThankyouView(TemplateView):
    template_name = 'apparel/order_thankyou.html'

    def get_context_data(self, **kwargs):
        context = super(OrderThankyouView, self).get_context_data(**kwargs)
        context['item'] = Item.objects.get(pk=kwargs['pk']).serialize()
        return context
