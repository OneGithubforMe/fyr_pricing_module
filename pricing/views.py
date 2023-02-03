from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import DistanceBasePricing, TimeMultiplierFactor, DistanceAdditionalPrice

class CalculatePricing(View):
    def get(self, request):
        compulsory_keys = ['hour', 'distance']
        params_values = {}
        for key in compulsory_keys:
            if key in request.GET:
                value = float(request.GET.get(key))
                if value == 0:
                    return JsonResponse({"price": 0})
                params_values[key] = value
            else:
                return HttpResponse(f"{key} not provided")

        is_successful, price = self.calculate_price(**params_values)
        if not is_successful:
            return HttpResponse(price)
        context = {
            "price": price
        }
        return JsonResponse(context)


    def calculate_price(self, hour, distance):
        distance_based_pricing = DistanceBasePricing.objects.filter(is_active=True, up_to_distance__lte=distance)\
            .order_by('-up_to_distance').first()
        if distance_based_pricing:
            additional_distance = distance - distance_based_pricing.up_to_distance
        else:
            distance_based_pricing = DistanceBasePricing.objects.filter(is_active=True) \
                .order_by('up_to_distance').first()
            if not distance_based_pricing:
                return False, "Distance based pricing is not defined (Contact Admin)"
            additional_distance = 0
        distance_based_price = distance_based_pricing.price

        distance_additional_price = 0
        if additional_distance:
            distance_additional_pricing = DistanceAdditionalPrice.objects.filter(is_active=True).first()
            if not distance_additional_pricing:
                 return False, "Distance Additional Price is not defined (Contact Admin)"
            distance_additional_price = distance_additional_pricing.price

        time_based_pricing = TimeMultiplierFactor.objects.filter(is_active=True, up_to_time__gte=hour) \
            .order_by('up_to_time').first()
        if not time_based_pricing:
            time_based_pricing = TimeMultiplierFactor.objects.filter(is_active=True) \
                .order_by('-up_to_time').first()
            if not time_based_pricing:
                return False, "Time based pricing is not defined (Contact Admin)"
        time_based_factor = time_based_pricing.factor

        price = (distance_based_price + (additional_distance * distance_additional_price)) * time_based_factor
        return True, price
