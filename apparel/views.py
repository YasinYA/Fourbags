from django.views.generic import View, TemplateView, ListView, DetailView
from django.http  import JsonResponse
import json
from .models  import Item, Order


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
        item = data['item']

        # get if data has item property
        if item:
            # check if that item exists (double checking)
            try:
                ordered_item = Item.objects.get(pk=item.get('id', ''))
            except Item.DoesNotExist:
                HttpResponse(status=404)
            else:
                # Finally create order object
                Order.objects.create(
                    item=ordered_item,
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    phone=data['phone'],
                    email=data['email'],
                    address=data['address'],
                    quantity=data['item_quantity'],
                    paybal=data['paybal'],
                    cash_on_delivery=data['cash_on_delivery']
                )

        return JsonResponse({
            "success": True
        })
