from django.conf import settings
from django.db import models


class ProductCategory(models.Model):
    """Just categories for products"""

    CREATION_TYPES = (
        'default',
        'user',
    )

    name = models.CharField(max_length=32)
    creation_type = models.CharField(choices=CREATION_TYPES)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Product(models.Model):
    """Base Product model"""

    CREATION_TYPES = (
        'default',
        'user',
    )

    parent_product = models.ForeignKey('self', on_delete=models.PROTECT)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_type = models.CharField(choices=CREATION_TYPES)
    default_product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, null=True)
    name = models.CharField()
    is_active = models.BooleanField(default=True)


class UserList(models.Model):
    """List of products custom user"""

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)


class UsedProduct(models.Model):
    """Products at lists"""

    base_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    list_id = models.ForeignKey(UserList, on_delete=models.CASCADE)
    at_home = models.BooleanField(default=True)
    at_cart = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class SharedList(models.Model):
    """Who has access to the list"""

    user_list = models.ForeignKey(UserList, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
