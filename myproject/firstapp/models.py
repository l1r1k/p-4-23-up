from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Название категории',
        help_text='В поле укажите название категории, например "Обувь".'
    )
    description = models.TextField(
        max_length=255,
        verbose_name='Описание категории',
        null=True,
        default='Отсутствует',
        help_text='Указывайте описании категории только в том случае, если категория неочивидна.'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Collection(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Название коллекции',
        help_text='В поле укажите название коллекции, например "Обувь".'
    )
    description = models.TextField(
        max_length=255,
        verbose_name='Описание коллекции',
        null=True,
        default='Отсутствует',
        help_text='Указывайте описании коллекции только в том случае, если коллекция неочивидна.'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

class Clothe(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название одежды'
    )
    description = models.TextField(
        max_length=512,
        verbose_name='Описание одежды'
    )
    price = models.DecimalField(
        verbose_name='Цена одежды',
        max_digits=8,
        decimal_places=2,
        help_text='Чтобы указать цену необходимо ввести положительное число с точностью до копеек.'
    )
    size = models.PositiveSmallIntegerField(
        verbose_name='Размер одежды'
    )
    photo = models.ImageField(
        upload_to='imgs/%Y/%m',
        verbose_name='Фото одежды',
        help_text='Прикрепить фото одежды',
        null=True,
        blank=True,
        default=''
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания карточки одежды',
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения карточки одежды',
        editable=False
    )
    is_exists = models.BooleanField(
        verbose_name='Доступен к заказу?',
        default=True
    )

    category = models.ForeignKey(
        Category,
        verbose_name='Категория одежды',
        on_delete=models.PROTECT
    )
    collections = models.ManyToManyField(
        Collection,
        verbose_name='Коллекция одежды'
    )

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'

class Order(models.Model):
    DELIVERY_TYPES = [
        ('SH', 'Самовывоз'),
        ('CR', 'Курьер'),
        ('PP', 'Пункт выдачи заказов'),
    ]

    buyer_lastname = models.CharField(
        max_length=100,
        verbose_name='Фамилия пользователя'
    )
    buyer_firstname = models.CharField(
        max_length=50,
        verbose_name='Имя пользователя'
    )
    buyer_middlename = models.CharField(
        max_length=100,
        verbose_name='Отчетство пользователя',
        null=True,
        blank=True,
        default='Отсутствует'
    )
    comment = models.TextField(
        max_length=256,
        verbose_name='Комментарий к заказу',
        null=True,
        blank=True,
        default='Отсутствует'
    )
    delivery_address = models.CharField(
        max_length=512,
        verbose_name='Адрес доставки',
        null=True,
        blank=True,
        default='Самовывоз'
    )
    delivery_type = models.CharField(max_length=2, choices=DELIVERY_TYPES, default='SH', verbose_name='Тип доставки')
    datetime_create = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Дата создания заказа'
    )
    datetime_finish = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата завершения заказа'
    )

    clothes = models.ManyToManyField('Clothe', through='Pos_Order', verbose_name='Позиции заказа')

    def __str__(self):
        return f'№{self.pk} - {self.buyer_lastname} {self.buyer_firstname} {self.buyer_middlename if self.buyer_middlename != 'Отсутствует' else ''}. {self.datetime_create}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Pos_Order(models.Model):
    clothes = models.ForeignKey(Clothe, on_delete=models.PROTECT, verbose_name='Одежда')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveSmallIntegerField(default=1, verbose_name='Количество одежды')
    discount = models.PositiveSmallIntegerField(default=0, verbose_name='Скидка')

    def __str__(self):
        return f'№{self.order.pk} - {self.order.buyer_lastname} {self.order.buyer_firstname} {self.order.buyer_middlename if self.order.buyer_middlename != 'Отсутствует' else ''} - {self.clothes.name}'

    class Meta:
        verbose_name = 'Позиция в заказе'
        verbose_name_plural = 'Позиции в заказе'
