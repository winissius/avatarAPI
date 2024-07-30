# Avatar Characters Web App

## Descrição

Este é um projeto web desenvolvido com Django que exibe uma lista de personagens do universo de "Avatar: The Last Airbender". A aplicação faz requisições a uma API externa, traduz os atributos relevantes dos personagens para o português e exibe essas informações em uma tabela paginada. 

## Funcionalidades

- **Exibição de Personagens:** Lista personagens do universo de "Avatar: The Last Airbender" com suas respectivas imagens, nomes, afiliações, aliados e inimigos.
- **Tradução Automática:** Utiliza a biblioteca `googletrans` para traduzir os atributos dos personagens para o português.
- **Paginação:** Implementa paginação para facilitar a navegação entre os personagens.
- **Design Responsivo:** Layout simples e responsivo para melhor visualização em diferentes dispositivos.

## Estrutura do Projeto

```bash
avatarAPI/
├── app_characters/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── templates/
│       └── index.html
├── avatarAPI/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
