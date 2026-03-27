# Estrutura Inicial do Banco – Conecta Aluno

## Entidades principais

### Usuário
- id
- nome
- email
- senha

### Perfil
- id
- usuario_id
- curso
- periodo
- habilidades

### Serviço
- id
- titulo
- descricao
- categoria
- tempo_estimado
- usuario_id

### Solicitação
- id
- servico_id
- solicitante_id
- status
- data_solicitacao