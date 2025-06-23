from rest_framework.response import Response
from rest_framework.decorators import api_view
from fundraise.models import DonationData, Donors, Campaigns
from .serializers import DonorsSerializer, CampaignsSerializer
from .serializers import DonationDataSerializer, CompleteSerializer
from .serializers import UsdSerializer
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage
from rest_framework import status
#------------DonationData Views------------------------1
@api_view(['GET'])
def getDonationData(request):
    """
    GET: List all Donations.
    """
    donations = DonationData.objects.all()
    paginator = Paginator(donations, 10)  # 10 items per page
    page = request.GET.get('page', 1)
    # Check if page is an integer
    if not str(page).isdigit():
        return Response(
            {"error": "Page number must be an integer."},
            status=status.HTTP_400_BAD_REQUEST
        )
    page = int(page)
    try:
        donation_page = paginator.page(page)
    except EmptyPage:
        return Response(
            {"error": "Page number exceeds available pages."},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = DonationDataSerializer(donation_page, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
#------------Donors Views------------------------------2
@api_view(['GET'])
def getDonor(request):
    """
    GET: List all donors
    """
    if request.method == 'GET':
        donor_id = Donors.objects.all()
        paginator = Paginator(donor_id, 10) # 10 items per page
        page = request.GET.get('page')
        donor_id = paginator.get_page(page)
        # Serialize the paginated data  
        serializer = DonorsSerializer(donor_id, many=True)
        return Response(serializer.data)   
#-------------Campaign Views---------------------------3
@api_view(['GET'])
def getCampaign(request):
    """
    GET: List all Donations per Campaigns
    """
    if request.method == 'GET':
        campaign_id = Campaigns.objects.all()
        serializer = CampaignsSerializer(campaign_id, many=True)
        return Response(serializer.data)
#--------------------completed--------------------------4
@api_view(['GET'])
def getCompleted(request):
    """
    GET: Completed Status per Campaigns
    """
    if request.method == 'GET':
        completed = Campaigns.objects.all()
        serializer = CompleteSerializer(completed, many=True)
        return Response(serializer.data)   
#---------------Amount per Currency Views-----------------5
@api_view(['GET'])
def getCurrencyAmount(request, pk):
    """
    GET: Campaign Donation per Currency
    """
    if request.method == 'GET':
        # Validate that pk is an integer
        try:
            currency_code = int(pk)
        except (ValueError, TypeError):
            return Response(
                {'error': 'Currency code must be an integer'},
                status=status.HTTP_400_BAD_REQUEST
            )       
        # Validate USD spelling (must be code 1)
        if currency_code != 1:
            return Response(
                {'error': 'Invalid currency code. Use 1 for USD'},
                status=status.HTTP_400_BAD_REQUEST
            )       
        # Get and return USD campaigns
        usd_campaigns = Campaigns.objects.all()
        serializer = UsdSerializer(usd_campaigns, many=True)
        return Response(serializer.data)
#=============End of views.py=============================
