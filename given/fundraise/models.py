from django.db import models
#--------Donation Data Model-------------------------------1
class DonationData(models.Model):
    donation_id = models.IntegerField(primary_key=True)
    donor_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    donation_date = models.TextField(blank=True, null=True)
    campaign_id = models.IntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donation_data'
#--------Donors Model--------------------------------------2
class Donors(models.Model):
    donor_id = models.IntegerField(primary_key=True)
    total_amount_by_donor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    completed = models.CharField(max_length=50, blank=True, null=True)
    failed = models.CharField(max_length=50, blank=True, null=True)
    pending = models.CharField(max_length=50, blank=True, null=True)
    usd = models.CharField(db_column='USD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    zar = models.CharField(db_column='ZAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    eur = models.CharField(db_column='EUR', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'donors'
#--------Campaign Model End-------------------------------3
class Campaigns(models.Model):
    campaign_id = models.IntegerField(primary_key=True)
    total_amount_per_campaign = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    usd = models.CharField(db_column='USD', max_length=10, blank=False, null=True)
    zar = models.CharField(db_column='ZAR', max_length=10, blank=False, null=True)
    eur = models.CharField(db_column='EUR', max_length=10, blank=False, null=True)
    total_donors_per_campaign_id = models.CharField(max_length=10, blank=True, null=True)
    completed = models.CharField(max_length=10, blank=False, null=True)
    failed = models.CharField(max_length=10, blank=True, null=True)
    pending = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaigns'
#==================End of models.py=============================
