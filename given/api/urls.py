from django.urls import path
from . import views
# URLs for the API endpoints related to donations, donors, and campaigns
urlpatterns = [
    path('', views.getDonationData, name='Get All Donations Data'),
    #--------------------------------------
    path('donor/', views.getDonor, name='Get Donors'),
    path('campaign/', views.getCampaign, name='Get Campaign List'),
    path('campaign/<int:pk>/', views.getCurrencyAmount, name='Donation per Currency'),
    path('campaign/complete/', views.getCompleted, name='Get Completed List'),
]
#=========================End of urls.py====================================