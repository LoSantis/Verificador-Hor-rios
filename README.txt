# Verificador de Disponibilidade de Horários

## Como usar

1. Instale as dependências (apenas uma vez):
   pip install streamlit pandas

2. Rode o programa com:
   streamlit run verifica_horarios.py

3. No navegador, escolha o dia da semana e o horário desejado.

## Como adicionar ou remover pessoas

Abra o arquivo `horarios.csv` e edite como quiser. Cada linha representa uma pessoa, com os horários disponíveis em cada dia da semana.

Formato dos horários: HH:MM-HH:MM (você pode separar vários intervalos com vírgulas)
Exemplo:
08:00-12:00,14:00-17:00

Deixe em branco se a pessoa não estiver disponível naquele dia.