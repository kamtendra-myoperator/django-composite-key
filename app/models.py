from django.db import models
from viewflow.fields import CompositeKey

class Temp(models.Model):
    id = models.CharField(max_length=50)
    company_id = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)  # Fixed the typo in 'company_name'
    created_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'temp'  # This matches the table name in your database
        unique_together = (('id', 'company_id'),)  # Ensure the combination is unique

    composite_key = CompositeKey(columns=['id', 'company_id'])  # Define the composite key
