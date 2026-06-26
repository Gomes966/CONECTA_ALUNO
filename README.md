# Conecta Aluno

## Descrição

O Conecta Aluno é uma aplicação web desenvolvida com Django que tem como objetivo conectar estudantes universitários interessados em compartilhar conhecimentos, oferecer monitorias e disponibilizar serviços acadêmicos para outros alunos.

A plataforma permite a divulgação e consulta de serviços relacionados a áreas como programação, design, idiomas, reforço acadêmico e suporte em disciplinas específicas.

---

## Objetivos

* Facilitar a troca de conhecimentos entre estudantes;
* Incentivar a colaboração acadêmica;
* Centralizar a divulgação de serviços oferecidos por alunos;
* Disponibilizar uma plataforma simples para busca e consulta de serviços.

---

## Funcionalidades Implementadas

### Serviços

* Cadastro de serviços;
* Listagem de serviços;
* Visualização detalhada de serviços;
* Pesquisa por título;
* Filtro por categoria.

### Autenticação

* Login de usuários;
* Logout de usuários;
* Controle de acesso para funcionalidades restritas.

### Administração

* Gerenciamento de serviços pelo painel administrativo do Django;
* Gerenciamento de usuários pelo painel administrativo do Django.

---

## Tecnologias Utilizadas

### Backend

* Python 3
* Django 6

### Frontend

* HTML5
* CSS3

### Banco de Dados

* SQLite3

### Controle de Versão

* Git
* GitHub

---

## Estrutura do Projeto

```text
conecta_aluno/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── usuarios/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── static/
│   └── css/
│
├── templates/
│   └── base.html
│
├── manage.py
├── README.md
└── .gitignore
```

---

## Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Acesse a pasta do projeto:

```bash
cd CONECTA_ALUNO
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install django
```

Execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

---

## Funcionalidades Previstas

* Cadastro de usuários pela interface;
* Associação de serviços ao usuário autenticado;
* Edição de serviços;
* Exclusão de serviços;
* Área de gerenciamento de serviços do usuário;
* Sistema de interesse em serviços.

---

## Status

Projeto em desenvolvimento.
MVP funcional implementado para fins acadêmicos.
