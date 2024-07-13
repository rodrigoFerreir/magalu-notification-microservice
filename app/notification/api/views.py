
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import status

from notification.services.NotificationService import NotificationService


logger = logging.getLogger(__name__)

class CreateSqueduledNotificationAPI(APIView):
    service = NotificationService()


    def post(self, request, *args, **kwargs) -> Response:
        try:
            result = self.service.create(request.data)
            
            return Response({"message":"Cadastro realizado com sucesso!", "data":result}, status.HTTP_200_OK)
        except ValidationError as error:
            logger.error(f"{error}")
            return Response({"message":error}, status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            logger.error(f"{err}")
            return Response({"message":err}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    

    def get(self, request, *args,**kwargs) -> Response:
        try:
            notification_id = request.query_params.get("notification_id", None)
            status_notification = request.query_params.get("status", None)
            
            data = self.service.get(notification_id, status_notification)
            
            return Response({"message":"Notificações encontradas com sucesso!", "data": data }, status.HTTP_200_OK)
        except Exception as err:
            logger.error(f"{err}")
            return Response({"message":err}, status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, *args,**kwargs) -> Response:
        try:
            notification_id = request.query_params.get("id")
            if not notification_id:
                return Response({"message":"Paramiter 'id' of notification is obrigatory"}, status.HTTP_400_BAD_REQUEST)

            self.service.delete(notification_id)
            return Response({"message":"Notificação cancelada com sucesso!"}, status.HTTP_200_OK)
        except Exception as err:
            logger.error(f"{err}")
            return Response({"message":err}, status.HTTP_500_INTERNAL_SERVER_ERROR)
