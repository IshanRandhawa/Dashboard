from django.db import models

class L4(models.Model):
    fsf_id = models.IntegerField()
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class L3(models.Model):
    fsf_id = models.IntegerField()
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(L4, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class L2(models.Model):
    fsf_id = models.IntegerField()
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(L3, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class L1(models.Model):
    fsf_id = models.IntegerField()
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(L2, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class L2_calls(models.Model):
    person = models.ForeignKey(L2, on_delete=models.CASCADE)
    Blconsumption = models.FloatField(default = 0)
    BlconsumptionT = models.IntegerField(default = 0)
    Coverage = models.IntegerField(default  =0)
    PNSconsumption = models.FloatField(default = 0)
    PNSconsumptionT = models.IntegerField(default = 0)
    
class L1_calls(models.Model):
    person = models.ForeignKey(L1, on_delete=models.CASCADE)
    Blconsumption = models.FloatField(default = 0)
    BlconsumptionT = models.IntegerField(default = 0)
    Coverage = models.IntegerField(default  =0)
    PNSconsumption = models.FloatField(default = 0)
    PNSconsumptionT = models.IntegerField(default = 0)
    




