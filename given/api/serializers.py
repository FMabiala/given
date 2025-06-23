
from rest_framework import serializers
from fundraise.models import Donors, Campaigns, DonationData
#-------------Donations Serializer------------------------1
class DonationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationData # Specify the model to serialize
        fields = '__all__'  # This will include all fields in the model
        
#-------------Donors Serializer----------------------------2
class DonorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donors #
        fields = '__all__'

#-------------Campaign Serializer--------------------------3
class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns       
        fields = '__all__'

#-------------Completed Serializer--------------------------4
class CompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = ['campaign_id', 'completed']

# #-------------Currency Serializer-------------------------5
class UsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = ['campaign_id', 'usd']
#====================end of serializers.py========================
