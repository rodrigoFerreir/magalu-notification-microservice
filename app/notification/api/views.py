
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from notification.services.NotificationService import NotificationService

class CreateSqueduledNotificationAPI(APIView):
    service = NotificationService()


    def post(self, request, *args, **kwargs) -> Response:
        result = self.service.create(request.data)
        
        return Response({"message":"Cadastro realizado com sucesso!", "data":result}, status.HTTP_200_OK)
    

    def get(self, request, *args,**kwargs) -> Response:
        notification_id = None
        if request.query_params: 
            notification_id = request.query_params.get("notification_id", None)
            status_notification = request.query_params.get("status", None)
        
        data = self.service.get(notification_id, status_notification)
        
        return Response({"message":"Notificações encontradas com sucesso!", "data": data }, status.HTTP_200_OK)
