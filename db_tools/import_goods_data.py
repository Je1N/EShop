__author__ = 'jeen'

#独立使用Django的model
import sys
import os

#获取当前文件的路径
pwd = os.path.dirname(os.path.realpath(__file__))
#将项目的根目录加入到python的搜索路径下
sys.path.append(pwd + '../')

#设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EShop.settings")

#调用django
import django
django.setup()

#执行操作
from goods.models import Goods,GoodsCategory,GoodsImage
from db_tools.data.product_data import row_data

for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail['name']
    goods.market_price = float(int(goods_detail['market_price'].replace('￥','').replace('元','')))
    goods.shop_price = float(int(goods_detail['sale_price'].replace('￥','').replace('元','')))
    goods.goods_brief = goods_detail['desc'] if goods_detail['desc'] is not None else ''
    goods.goods_desc = goods_detail['goods_desc'] if goods_detail['goods_desc'] is not None else ''
    goods.goods_front_image = goods_detail['images'][0] if goods_detail['images'] else ''

    category_name = goods_detail['categorys'][-1]
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()

    #轮播图
    for goos_image in goods_detail['images']:
        goods_image_instance = GoodsImage()
        goods_image_instance.image = goos_image
        goods_image_instance.goods = goods
        goods_image_instance.save()

