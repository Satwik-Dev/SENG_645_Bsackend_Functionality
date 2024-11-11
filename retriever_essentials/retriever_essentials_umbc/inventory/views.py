#inventory/views.py
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Item, ItemClassification
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'inventory/index.html')

#def inventory_list(request):
#    items = Item.objects.all()
#    classifications = ItemClassification.objects.all()
#    
#    # Filter by classification if a classification is selected
#    classification_id = request.GET.get('classification')
#    if classification_id:
#        items = items.filter(classification_id=classification_id)
#    
#    return render(request, 'inventory/inventory_list.html', {
#        'items': items,
#        'classifications': classifications,
#    })

def inventory_list(request):
    items = Item.objects.all()
    classifications = ItemClassification.objects.all()

    # Filter items if classification is selected
    classification_id = request.GET.get('classification')
    if classification_id:
        items = items.filter(classification_id=classification_id)
    
    # Check if request is AJAX for JSON response
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        items_data = [
            {
                'id': item.id,
                'name': item.name,
                'quantity': item.quantity,
                'classification': item.classification.name,
                'expiry_date': item.expiry_date.isoformat() if item.expiry_date else None
            }
            for item in items
        ]
        return JsonResponse({'items': items_data})

    # Render regular template for non-AJAX requests
    return render(request, 'inventory/inventory_list.html', {
        'items': items,
        'classifications': classifications,
    })


#def update_inventory(request, item_id):
#    item = get_object_or_404(Item, id=item_id)
#    if request.method == 'POST':
#        new_quantity = request.POST.get('quantity')
#        if new_quantity:
#            item.quantity = new_quantity
#            item.save()
#        return HttpResponseRedirect(reverse('inventory_list'))
#    return render(request, 'inventory/update_inventory.html', {'item': item})

@csrf_exempt  # Only if CSRF token issues persist in AJAX
def update_inventory(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        new_quantity = request.POST.get('quantity')
        if new_quantity:
            item.quantity = new_quantity
            item.save()
            return JsonResponse({'success': True, 'new_quantity': item.quantity})
    return JsonResponse({'success': False}, status=400)
