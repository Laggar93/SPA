from django.contrib import messages
import re
from django.views.generic import ListView
from apps.index.models import Spa



def is_valid_string(name, value):
    if name == 'name':
        a = re.compile(r'\W')
        # pattern = r'''[&"']@%\/|.,^#!?><_-+=*()%$~`'''
        print(len(re.findall(a, value)))
        if len(re.findall(a, value)) > 0:
            return False
            print(a)
        return True



def is_valid_number(name, value):
    if name == 'count' or name == 'distance':
        try:
            integer = int(value)
            return True
        except:
            return False



class IndexView(ListView):
    model = Spa
    template_name = 'pages/index.html'
    queryset = Spa.objects.all()
    paginate_by = 5
    context_object_name = 'spa_data'
    print(context_object_name)


    def get_queryset(self):
        if self.request.GET:
            title = self.request.GET.get('column')
            operator = self.request.GET.get('condition')
            quantity = self.request.GET.get('value')


            if title == 'name':
                validate_data = is_valid_string(title, quantity)
                if validate_data:
                    filter = Spa.objects.filter(name__icontains=quantity)
                    return filter
                messages.add_message(self.request, messages.WARNING, 'Недопустимое значение')
                return Spa.objects.all()

            if title == 'count' and operator == 'greater':
                validate_data = is_valid_number(title, quantity)
                if validate_data:
                    filter = Spa.objects.filter(count__gt=int(quantity))
                    return filter
                messages.add_message(self.request, messages.WARNING,
                                     'Недопустимое значение')
                return Spa.objects.all()


            if title == 'count' and operator == 'less':
                validate_data = is_valid_number(title, quantity)
                if validate_data:
                    filter = Spa.objects.filter(count__lt=int(quantity))
                    return filter
                messages.add_message(self.request, messages.WARNING,
                                     'Недопустимое значение')
                return Spa.objects.all()


            if title == 'count' and operator == 'equal':
                validate_data = is_valid_number(title, quantity)
                if validate_data:
                    filter = Spa.objects.filter(count__exact=int(quantity))
                    return filter
                messages.add_message(self.request, messages.WARNING,
                                     'Недопустимое значение')
                return Spa.objects.all()


            if title == 'count' and operator == 'contains':
                validate_data = is_valid_number(title, quantity)
                if validate_data:
                    filter = Spa.objects.filter(count__exact=int(quantity))
                    return filter
                messages.add_message(self.request, messages.WARNING,
                                     'Недопустимое значение')
                return Spa.objects.all()


            if title == 'distance' and operator == 'greater':
                validate_data = is_valid_number(title, quantity)
                if validate_data:
                    filter = Spa.objects.filter(distance__gt=int(quantity))
                    return filter
                messages.add_message(self.request, messages.WARNING,
                                     'Недопустимое значение')
                return Spa.objects.all()


            if title == 'distance' and operator == 'less':
                validate_data = is_valid_number(title, quantity)
                if validate_data:
                    filter = Spa.objects.filter(distance__lt=int(quantity))
                    return filter
                messages.add_message(self.request, messages.WARNING,
                                     'Недопустимое значение')
                return Spa.objects.all()


            if title == 'distance' and operator == 'equal':
                validate_data = is_valid_number(title, quantity)
                if validate_data:
                    filter = Spa.objects.filter(distance__exact=int(quantity))
                    return filter
                messages.add_message(self.request, messages.WARNING,
                                     'Недопустимое значение')
                return Spa.objects.all()

            if title == 'distance' and operator == 'contains':
                validate_data = is_valid_number(title, quantity)
                if validate_data:
                    filter = Spa.objects.filter(distance__exact=int(quantity))
                    return filter
                messages.add_message(self.request, messages.WARNING,
                                     'Недопустимое значение')
                return Spa.objects.all()

        filter = Spa.objects.filter()


        if self.request.GET:
            sort_name = self.request.GET.get('name_sort')
            sort_count = self.request.GET.get('count_sort')
            sort_distance = self.request.GET.get('distance_sort')
            if sort_name == 'greater':
                filter = Spa.objects.order_by('name')
                return filter
            if sort_name == 'less':
                filter = Spa.objects.order_by('-name')
                return filter
            if sort_count == 'greater':
                filter = Spa.objects.order_by('count')
                return filter
            if sort_count == 'less':
                filter = Spa.objects.order_by('-count')
                return filter
            if sort_distance == 'greater':
                filter = Spa.objects.order_by('distance')
                return filter
            if sort_distance == 'less':
                filter = Spa.objects.order_by('-distance')
                return filter

        return filter
