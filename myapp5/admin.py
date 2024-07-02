from django.contrib import admin

from myapp2.models import Product, Order, User


@admin.action(description="Сбросить количество в 0")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список заказов"""
    list_display = ["product_name",
                    "description",
                    "price",
                    "quantity",
                    "date_create",
                    "rating"]
    list_filter = ['date_create',
                   'quantity',
                   "price"
                   ]
    # fields = ["product_name",
    #           "description",
    #           "price",
    #           "quantity",
    #           "date_create",
    #           "rating"
    #           ]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['product_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating'],
            }
        ),
    ]

    ordering = ['-quantity']
    search_fields = ['product_name']
    search_help_text = 'Поиск по полю названия продукта продукта(product_name)'
    actions = [reset_quantity]


class UserAdmin(admin.ModelAdmin):
    """Список заказов"""
    list_display = ["name",
                    "email",
                    "phone",
                    "address",
                    "date_create",
                    ]
    list_filter = ['name',
                   "email",
                   "phone",
                   "address",
                   "date_create",
                   ]
    ordering = ['-date_create']
    search_fields = ['phone']
    search_help_text = 'Поиск по полю Телефон в заказе продукта(phone)'


class OrderAdmin(admin.ModelAdmin):
    """Список заказов"""
    list_display = ["total_price",
                    "date_ordered",
                    ]
    list_filter = ["date_ordered"]
    ordering = ['-date_ordered']
    search_fields = ['customer']
    search_help_text = 'Поиск по полю Заказчик в заказе продукта(customer)'


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)
