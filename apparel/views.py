from django.views.generic import TemplateView, ListView, DetailView
from .models  import Item


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
