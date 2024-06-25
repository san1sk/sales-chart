from django.shortcuts import render
from django.core.cache import cache
from .tasks import aggregateSalesData
import json

def salesChart(request):
    """Renders the sales data chart.
    This view retrieves aggregated monthly sales data from the cache.
    If the data is not present in the cache, it triggers the Celery task
    to aggregate the data and store it in the cache.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered HTML page with the sales chart."""
    # Force refresh the cache
    aggregateSalesData()
    data = cache.get('monthlySalesData')

    if not data:
        from django.db.models import Sum
        from .models import SalesData
        aggregatedData = SalesData.objects.values('saleDate__month').annotate(totalAmount=Sum('amount')).order_by('saleDate__month')
        data = {item['saleDate__month']: float(item['totalAmount']) for item in aggregatedData}
        cache.set('monthlySalesData', json.dumps(data), timeout=60*60)

    data = json.loads(data)
    return render(request, 'sales/chart.html', {'data': data})
