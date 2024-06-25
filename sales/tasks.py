from celery import shared_task
from django.core.cache import cache
from django.db.models import Sum
from sales.models import salesData
import json

@shared_task
def aggregateSalesData():
    # Task to aggregate sales data by month and cache the result.
    # Aggregate sales data by month
    
    aggregatedData = salesData.objects.values('saleDate__month').annotate(totalAmount=Sum('amount')).order_by('saleDate__month')
    
    # Convert query results to a dictionary
    data = {item['saleDate__month']: float(item['totalAmount']) for item in aggregatedData}

    # Cache for 1 hour
    cache.set('monthlySalesData', json.dumps(data), timeout=60*60) 
