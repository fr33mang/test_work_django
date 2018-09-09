from django.db import models

class VehicleType(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название типа')
    code = models.CharField(max_length=256, verbose_name='Код типа')

    def __str__(self):
        return self.name

class VehicleBrand(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название производителя')
    code = models.CharField(max_length=256, verbose_name='Код производителя')
    create_date = models.DateField(verbose_name='Дата создания')
    web = models.CharField(max_length=512, verbose_name='Веб-сайт производителя')

    def __str__(self):
        return self.name

class VehicleModel(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название модели')
    code = models.CharField(max_length=256, verbose_name='Код модели')
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, verbose_name='Тип техники')
    vehicle_brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, verbose_name='Производитель', related_name='models')

    running_order_mass = models.FloatField(verbose_name='Снаряженная масса', default=0)
    max_capacity = models.FloatField(verbose_name='Максимальная грузоподъемность', default=0)

    def __str__(self):
        return self.name

'''
Класс техники, включает в себя основные параметры любой используемой техники,
подразумевает наследование, для более детализированного представления 
'''
class Vehicle(models.Model):
    board_number = models.CharField(max_length=50, verbose_name='Бортовой номер',)
    info = models.CharField(max_length=512, verbose_name='Информация')
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, related_name='model_vehicles')

    current_mass = models.FloatField(verbose_name='Текущий вес', default=0)
    
    @property 
    def overload(self):
        percent = (self.current_mass - self.vehicle_model.max_capacity - self.vehicle_model.running_order_mass) / self.vehicle_model.max_capacity * 100
        return percent if percent > 0 else 0

    # etc...

    def __str__(self):
        return self.board_number

    def save(self, *args, **kwargs):
        if not self.current_mass:
            self.current_mass = self.vehicle_model.running_order_mass
        super(Vehicle, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Единица техники'
        verbose_name_plural = 'Техника'
'''

class VehicleParam(models.Model):
    #pass
    name = models.CharField(max_length=256, verbose_name='Название параметра')
    code = models.CharField(max_length=256, verbose_name='Код параметра')
    #vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

param_types = [
    (1, ('Числовой')),
    (2, ('Строковый')),
    (3, ('Дата')),
]

class VehicleParamValue(models.Model):
    #pass
    vehicle_param = models.ForeignKey(VehicleParam, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='params')
    value_type = models.IntegerField(choices=param_types, default=1, verbose_name='Тип параметра')
    value_str = models.CharField(max_length=512, verbose_name='Строковое значение', blank=True)
    value_numb = models.FloatField(verbose_name='Числовое значение', blank=True)
    value_date = models.DateField(verbose_name='Дата', blank=True)

'''


    

