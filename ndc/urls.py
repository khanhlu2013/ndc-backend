from django.contrib import admin
from django.conf.urls import url,include
from rest_framework_jwt.views import obtain_jwt_token
import event.urls
import member.urls

urlpatterns = [
	url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^event_api/', include(event.urls)),  
    url(r'^member_api/', include(member.urls)),      
    url(r'^admin/', admin.site.urls),    
]

