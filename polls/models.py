from django.db import models

# Create your models here.
class Transaction(models.Model):
    iid = models.IntegerField(primary_key=True)
    ttype = models.CharField(max_length=50)
    icode = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def getJSON(self):
        return '"id%s":{"ttype":"%s", "icode":"%s", "desc":"%s"}' % (self.iid, self.ttype, self.icode, self.description)

    def getID(self):
        return self.iid;

class Wfdata(models.Model):
    iid = models.IntegerField(primary_key=True)
    t_id = models.IntegerField()
    barcode = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def getID(self):
        return self.iid

    def getJSON(self):
        return '{"iid":"%s", "t_id":"%s", "barcode":"%s", "quantity":"%s"}' % (self.iid, self.t_id, self.barcode, self.quantity)