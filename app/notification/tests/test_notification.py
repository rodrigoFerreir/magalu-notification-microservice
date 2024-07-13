import datetime
import pytest

from rest_framework.test import APIClient
from notification.services.NotificationService import NotificationService
from notification.services.SendNotificationService import SendNotificationService

api_client_test = APIClient()
service = NotificationService()

payload = {
    "channel": "EMAIL",
    "message": f"teste_Notificação - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
    "type": "schedule",
    "execution_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    "contact": {
        "name": "teste01",
        "email":"teste01@email.com",
        "phone":"819889954561"
    }
}

# teste de serviços
@pytest.mark.django_db
def test_service_create_notification():
    result = service.create(payload)
    assert type(result) ==  dict
    assert 'id' in result.keys()
    assert "status" in result.keys()
    assert result["status"] == "pending"
    assert result["message"] == payload["message"]

@pytest.mark.django_db
def test_service_get_notification():
    result_create = service.create(payload)
    assert 'id' in result_create.keys()

    result_get = service.get(result_create['id'], status="pending")

    assert isinstance(result_get, list) == True
    assert isinstance(result_get[0], dict) == True
    assert 'id' in result_get[0].keys()
    assert result_get[0]["message"] == payload["message"]

@pytest.mark.django_db
def test_service_delete_notification():
    result_create = service.create(payload)
    result_delete = service.delete(result_create['id'])
    result_get = service.get(result_create["id"])

    assert isinstance(result_delete, bool) == True
    assert len(result_get) > 0
    assert result_get[0].get('status') == 'cancelled'

@pytest.mark.django_db
def test_service_send_notification():
    result_create = service.create(payload)
    SendNotificationService.execute()
    result_get = service.get(result_create["id"])
    
    assert result_get[0].get('status') == 'success'


#teste de api routes
@pytest.mark.django_db
def test_api_schedule_notification():
    response = api_client_test.post("/api/notification/squedule", payload, format='json')

    assert response.status_code == 200
    assert response.data.get('data').get('message') == payload["message"]


@pytest.mark.django_db
def test_api_get_notification():
    response = api_client_test.get("/api/notification/squedule", format='json')

    assert response.status_code == 200
    assert isinstance(response.data.get('data'), list) == True


@pytest.mark.django_db
def test_api_get_notification():
    result = service.create(payload)
    assert isinstance(result, dict)
    assert 'id' in result.keys()

    response = api_client_test.delete(f"/api/notification/squedule?id={result['id']}" , format='json')

    assert response.status_code == 200
    assert response.json().get("message") == "Notificação cancelada com sucesso!"
