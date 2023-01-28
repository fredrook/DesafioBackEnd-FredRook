# Desafio para vaga Back-end - JUNIOR

Por favor leiam este documento do começo ao fim, com muita atenção.
O intuito deste teste é avaliar seus conhecimentos técnicos com o back-end, para ser mais específico em Python.

O teste consiste em parsear [este arquivo de texto(CNAB)](https://github.com/Kenzie-Academy-Brasil-Developers/desafio-backend-m6/blob/main/CNAB.txt) e salvar suas informações(transações financeiras) em uma base de dados a critério do candidato.

Este desafio deve ser feito por você em sua casa. Gaste o tempo que você quiser, porém normalmente você não deve precisar de mais do que algumas horas.

# Instruções de entrega do desafio

1. Primeiro, crie um repositório público no Github.
2. Em seguida, implemente o projeto tal qual descrito abaixo, em seu clone local.
3. Faça o push do seu projeto local para um repositório público no Github.
4. Por fim, envie no canvas os links dos seus repositórios.

# Descrição do projeto

Você recebeu um arquivo CNAB com os dados das movimentações financeiras de várias lojas.
Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload do [arquivo CNAB](https://github.com/Kenzie-Academy-Brasil-Developers/desafio-backend-m6/blob/main/CNAB.txt), normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

**Sua aplicação web DEVE:**

1. Ter uma tela (via um formulário) para fazer o upload do arquivo
2. Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar corretamente a informação em um banco de dados relacional, **se atente as documentações** que estão logo abaixo.
3. Exibir uma lista das operações importadas por lojas, e nesta lista deve conter um totalizador do saldo em conta
4. Ser escrita obrigatoriamente em Python 3.0+
5. Ser simples de configurar e rodar, de preferência dockerizado e funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.

**Sua aplicação web não precisa:**

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
2. Ser escrita usando algum framework específico (mas não há nada errado em usá-los também, use o que achar melhor).

# Documentação do CNAB

| Descrição do campo | Inicio | Fim | Tamanho | Comentário                                                                                                                |
| ------------------ | ------ | --- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| Tipo               | 1      | 1   | 1       | Tipo da transação                                                                                                         |
| Data               | 2      | 9   | 8       | Data da ocorrência                                                                                                        |
| Valor              | 10     | 19  | 10      | Valor da movimentação. _Obs._ O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo. |
| CPF                | 20     | 30  | 11      | CPF do beneficiário                                                                                                       |
| Cartão             | 31     | 42  | 12      | Cartão utilizado na transação                                                                                             |
| Hora               | 43     | 48  | 6       | Hora da ocorrência atendendo ao fuso de UTC-3                                                                             |
| Dono da loja       | 49     | 62  | 14      | Nome do representante da loja                                                                                             |
| Nome loja          | 63     | 81  | 19      | Nome da loja                                                                                                              |

# Documentação sobre os tipos das transações

| Tipo | Descrição              | Natureza | Sinal |
| ---- | ---------------------- | -------- | ----- |
| 1    | Débito                 | Entrada  | +     |
| 2    | Boleto                 | Saída    | -     |
| 3    | Financiamento          | Saída    | -     |
| 4    | Crédito                | Entrada  | +     |
| 5    | Recebimento Empréstimo | Entrada  | +     |
| 6    | Vendas                 | Entrada  | +     |
| 7    | Recebimento TED        | Entrada  | +     |
| 8    | Recebimento DOC        | Entrada  | +     |
| 9    | Aluguel                | Saída    | -     |

# Avaliação

Seu projeto será avaliado de acordo com os seguintes critérios.

1. Sua aplicação preenche os requerimentos básicos?
2. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
3. Você seguiu as instruções de envio do desafio?
4. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.

Boa sorte!
