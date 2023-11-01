from django.shortcuts import render, redirect
from . import forms  # 导入物品表单
from .models import Item, Orders  # 导入物品模型
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from User.models import OrdinaryUser
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'base.html')


def show_item(request):
    itemList = Item.objects.all()  # 或其他相应的查询
    available_items = [item for item in itemList if item.itemStatus == 0]
    context = {
        'itemList': available_items,
        'available_count': len(available_items),
    }
    return render(request, 'Market/itemList.html', context)


def publish(request):
    if not request.session.get('is_login', None):
        return redirect('User/login.html')

    if request.method == 'POST':
        item_form = forms.ItemForm(request.POST, request.FILES)
        message = "请检查填写的内容！"
        if item_form.is_valid():
            category = item_form.cleaned_data.get('category')
            item_name = item_form.cleaned_data.get('itemName')
            purchase_year = item_form.cleaned_data.get('purchaseYear')
            price = item_form.cleaned_data.get('price')
            item_photo = item_form.cleaned_data.get('item_photo')
            item_desc = item_form.cleaned_data.get('itemDesc')
            location = item_form.cleaned_data.get('location')
            new_old_degree = item_form.cleaned_data.get('new_old_degree')

            new_item = Item(
                category=category,
                itemName=item_name,
                purchaseYear=purchase_year,
                price=price,
                item_photo=item_photo,
                itemDesc=item_desc,
                location=location,
                new_old_degree=new_old_degree,
                itemStatus=0
            )
            seller_id = request.session['user_id']
            seller = OrdinaryUser.objects.filter(user_id=seller_id).first()
            new_item.seller = seller
            new_item.save()
            message = '发布成功！'
            return render(request, 'Market/success.html', locals())
        else:
            return render(request, 'Market/publish.html', locals())

    item_form = forms.ItemForm()
    return render(request, 'Market/publish.html', locals())


def get_order(request, item_id):
    item = get_object_or_404(Item, itemId=item_id)
    buyer_id = request.session['user_id']
    user = OrdinaryUser.objects.filter(user_id=buyer_id).first()
    order = Orders.objects.create(item=item, buyer=user, seller=item.seller, order_price=item.price, order_status=0)
    order.save()
    return redirect("Market:show_order")


def show_order(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/User/login/')

    template_name = 'Market/my_order.html'

    user_id = request.session['user_id']
    user = OrdinaryUser.objects.filter(user_id=user_id).first()
    context = {
        'order_list': Orders.objects.filter(buyer=user),
    }
    return render(request, template_name, context)


def payment(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    # 在这里添加处理支付的代码，比如修改订单状态、记录支付信息等
    order.order_status = 1
    order.save()
    item = order.item
    item.itemStatus = 1
    item.save()
    return HttpResponseRedirect('/Market/order/')  # 支付完成后重定向到订单页面


def cancel_order(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    # 在这里添加处理取消订单的代码，比如修改订单状态、记录取消信息等
    order.delete()  # 举例：删除订单
    return HttpResponseRedirect('/Market/order/')  # 取消订单后重定向到订单页面


def admin(request):
    context = {
        'itemList': Item.objects.all(),
    }
    return render(request, 'Market/admin.html', context)


def admin_remove(request, item_id):
    item = get_object_or_404(Item, itemId=item_id)
    item.itemStatus = 2
    item.save()
    return redirect("Market:admin")
