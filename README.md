# Resolvendo o Desafio Backend da Magalu usando Django:

Este é um projeto de exemplo com base em um video do youtube https://www.youtube.com/watch?v=af4W9Q4vB1s
No video é utilizado o framework Spring boot, resolvi recria-lo usando Django e Django Rest Framework.
Foram aplicados conceitos de Clean Architecture e TDD

# Descrição:
Um microserviço de agendamento de notificações onde é possivel enviar notificações via [EMAIL, SMS e WHATSAPP]

Comunicação com o banco e dados:
- [x]  Iniciando o projeto Django (Web, Django REST, Postgres)
- [x]  Configurando o Postgres no Docker
- [x]  Configurando a comunicação do Django com o Postgres
- [x]  Configurar o Celery para envio de notificações agendadas

Funcionalidade de solicitação de agendamento de notificação:
- [x]  Mapear as entidades (Notification, Channel e Status)
- [x]  Criar config de inicialização das tabelas (Channel e Status)
- [x]  Criar API de solicitação de agendamento de notificação
- [x]  Criar serviço de persistência da solicitação
- [x]  Testar o fluxo (api → service → postgres)

Funcionalidade de consultar a situação de agendamento de notificação:
- [x]  Criar API de consulta de solicitação de agendamento de notificação
- [x]  Criar serviço de consulta
- [x]  Testar a API

Funcionalidade de cancelamento de agendamento de notificação:
- [x]  Criar API de cancelamento de agendamento de notificação
- [x]  Criar serviço de cancelamento
- [x]  Testar a API

Rotina de checagem e envio de notificação:
- [x]  Criar rotina de checagem via Celery
- [x]  Testar se a rotina está funcionado
- [x]  Criar serviço de consulta de notificações disponíveis para envio
- [x]  Criar serviço que atualiza o status da notificação
- [x]  Testar o fluxo completo (api → agendamento → rotina → envia notificaçãos → atualiza base)

# run docker services
`docker-compose up`

# run celery
`app/entrypoint-celery.sh `

# run app in kubernet cluster
`kubectl apply -k k8s/`

