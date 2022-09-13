# Desafio Técnico DevOps Júnior

Esse é um desafio feito para conhecer um pouco mais de cada candidato a vaga de DevOps na Varsomics. Não se trata de um teste objetivo, capaz de gerar uma nota ou uma taxa de acerto, mas sim de um estudo de caso com o propósito de conhecer os conhecimentos, experiências e modo de trabalhar de um cadidato. Sinta-se livre para desenvolver sua solução para o problema proposto.

## Descrição
No diretório `api` existe uma simples api feita utilizando o FastAPI. Para que a api funcione é necessário passar 2 variáveis de ambiente chamada `ADMIN_USER` e `ADMIN_PASS` que serão as credenciais de administrador para acessar a rota pricipal da api. Para executqr a api utilize o comando `uvicorn main:app --reload`.

Seu objetivo é **DESCREVER** o processo de deploy da api utilizando os serviços da AWS em um arquivo `parte1.md` com os todos os passos necessários para faze-lo. Devemos poder reproduzir o processo descrito da sua resposta em uma conta da AWS. A seguir alguns pontos de atenção:

- Assume-se que o deploy será feito em uma conta AWS sem nenhum recurso de infraestrutura criado previamente.
- Existem diversas formas de realizar o deploy da aplicação utilizando os recursos da AWS. Sinta-se a vontade para escolher qualquer uma delas.
- Você pode alterar o código da api ou adicionar novos arquivos para que sua forma de deploy funcione.
- Diagramas da infraestrutura necessária para o deploy são bem vindos. :smile:

## Entrega

1. Efetue o fork deste repositório e crie um branch com o seu nome e sobrenome. (exemplo: fulano-dasilva)
2. Após finalizar o desafio, crie um Pull Request.
3. Envie um e-mail com o link de seu PR e aguarde algum contribuidor realizar o code review.

Boa sorte!

#### NÃO É NECESSÁRIO SUBIR O RECURSOS EM ALGUM CONTA AWS PRÓPRIA, SOMENTE A DESCRIÇÃO DOS PASSOS É NECESSÁRIA!
