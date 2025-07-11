# API de Tarefas com Flask

Este é um projeto de API RESTful desenvolvido com Flask e SQLite, com uma interface simples em HTML/JavaScript para visualizar, criar, editar e excluir tarefas. Ideal para estudos e demonstração de habilidades em backend Python.

---

## Funcionalidades

- Listar tarefas
- Adicionar nova tarefa
- Editar tarefa existente
- Excluir tarefa
- Marcar como concluída/pendente
- Interface web leve com HTML + JavaScript (fetch)

---

## Tecnologias utilizadas

- Python 3
- Flask
- SQLite
- HTML5 / CSS3
- JavaScript (fetch API)
- Git + GitHub

---

## Estrutura do projeto

```

todo\_api/
├── app.py
├── models.py
├── database.db
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md

````

---

## Como rodar o projeto localmente

1. Clone o repositório:

```bash
git clone https://github.com/rcustodio1/flask-todo-api.git
cd flask-todo-api
````

2. Crie o banco de dados:

```bash
py models.py
```

3. Inicie o servidor Flask:

```bash
py app.py
```

Depois, acesse no navegador:

```
http://localhost:5000
```

---

## Observações

* O banco de dados (database.db) é ignorado no Git, então será necessário gerá-lo localmente com `models.py`.
* O projeto foi desenvolvido com foco em aprendizado de backend com Flask.

---

## Autor

Rafael Custódio
Estudante de Análise e Desenvolvimento de Sistemas
LinkedIn: [www.linkedin.com/in/rafaelhcustodio](https://www.linkedin.com/in/rafaelhcustodio)
GitHub: [https://github.com/rcustodio1](https://github.com/rcustodio1)

---