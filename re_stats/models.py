from django.db import models


class Data(models.Model):
    original_row_id = models.IntegerField()
    data_status = models.CharField("Date data was last updated", max_length=5)
    msn = models.CharField("Data Series Names", max_length=5)
    statecode = models.CharField(max_length=2)
    year = models.IntegerField()
    data = 	models.FloatField("Value for given MSN. Units may vary")
