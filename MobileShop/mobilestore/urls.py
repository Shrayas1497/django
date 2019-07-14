
from django.urls import path,include
from .views import Homepage,MobileList, MobileDetail, AddMobile,UpdateMobile,DeleteMobile

app_name ='mobilestore'
#urlpatterns = [	
# 	path('',('mobilestore.urls',namespace='mobilestore')),
  
# ]
urlpatterns=[

 	path('',Homepage ,name='cssintro'),
	path('MobileList/',MobileList ,name='mobilelist'),
	path('MobileList/<int:id>',MobileDetail ,name='MobileDetail'),
	path('AddMobile/',AddMobile ,name='AddMobile'),
	path('mobileupdate/<int:id>',UpdateMobile,name='mobileupdate'),
	path('mobiledelete/<int:id>',DeleteMobile,name='mobiledelete'),

]
