+++
title = "Por que comecei a estudar Rust?"
slug = "porque-rust"
date = "2026-08-20"
+++

Meu último artigo foi sobre como escolher linguagens em times de desenvolvimento
sempre é uma escolha influenciada por vieses. Essa ideia de uma solução
100% técnica é rara e acontece principalmente em ambientes em que você tem problemas
de escala. A maioria vai seguir vieses ligados a situações muito comuns
ou conveniências de contexto. Um exemplo bem claro: React ou Vue?
Pergunte-se por que ninguém considera usar WebAssembly. Isso acontece porque é mais
prático usar o framework mais popular: você ganha em encontrar
desenvolvedores, em pagar menos por eles, e a quantidade de conteúdo e
experiência aplicada disponível é bem superior.

Parece uma solução técnica, mas não é! Não estamos debatendo o tempo de resposta
ou a eficiência do consumo de memória. É só o mais conveniente para o time e
para o negócio. Isso não é um problema! Só é problemático achar que a sua decisão
baseada no seu viés de conveniência é uma solução técnica objetivamente embasada.
Isso é o que mais gera débitos técnicos e escolhas ruins feitas em pequenos
e médios negócios.

Então Rust foi uma escolha super objetiva e baseada em requisitos puramente técnicos?
Óbvio que não! Mas eu imagino que estou fazendo uma aposta numa linguagem com
coisas a dizer e novidades a entregar. Para quem programa, o
importante é aprender paradigmas e não linguagens. E o Rust, com esse movimento
de segurança de memória sem o uso de garbage collectors (GC), é de fato uma novidade
interessante.

# Antes de começar, vamos ver exemplos

Quando eu comecei a programar em 2013 em Ruby on Rails, aprendi duas informações
valiosas: 1) TDD é uma forma de construir código de forma consistente; 2) o Ruby
on Rails me ensinou esse método de trabalho. Essa foi a primeira vez que aprendi
a instrumentalizar o meu estudo e não só obedecer o que externamente parecia fazer
sentido. Nesse processo, li dois livros para aprimorar o meu método de desenvolver
com TDD e não só aprender as interfaces. Então aprendi que escrever TDD não é só escrever
um teste antes de implementar, mas entender que são necessários dois testes para
cobrir o contraexemplo. O importante é entender que o valor da ferramenta está
no método que ela implementa.

Depois disso, tive que aprender frameworks JavaScript/TypeScript mais pelo hype,
mas ainda assim aprendi a estruturar frontends. Como arquitetar aplicações em que
toda a parte visual é independente — isso tem os seus prós e contras.
Em toda ferramenta ou etapa em que você pode aprender conceitos de base, é isso
que realmente deve ser levado e incorporado ao seu repertório de conceitos.

A última grande ferramenta que aprendi e que tinha um grande conceito por trás
foi o Apache Kafka e a orientação a eventos. Eu estava me acostumando a sempre
integrar sistemas de forma síncrona, com processos feitos à mão, em que dava mais
trabalho criar uma interface para um usuário do backoffice do que meter a mão
no console. Aprender orientação a eventos foi uma revolução na minha forma de
projetar sistemas. Por mais que pareça entusiasmado com um brinquedo novo, é porque
muitos problemas que exigiriam um trabalho de orquestração tão grande passaram
a ser naturais e evidentes. Isso depois de mais de 10 anos de estudo
de programação e ciência da computação. Essa é a verdadeira importância de não
parar de estudar.

# E qual é o método do Rust

O objetivo do estudo do Rust, antes de tudo, está ligado a voltar a linguagens
compiladas. Depois de 15 anos escrevendo muito código e com muito volume de entrega,
percebi que estava confortável não só com os frameworks, mas também com facilidades
de debug e em não pensar em como extrair o máximo de eficiência. Logo comecei a
procurar todas as linguagens compiladas que eu poderia estudar. Dentre todas, percebi
que havia uma linguagem que só me faria lembrar como é trabalhoso programar
sem uma máquina virtual limpando a sua sujeira. Outra linguagem que dava
total controle a ponto de ser paranoico.
E, finalmente, uma linguagem que faria o que parecia impossível: ter a experiência de
um garbage collector sem o overhead da máquina virtual. Não existe almoço grátis,
então pensei que eu teria que aplicar conceitos de programação que nenhuma
outra linguagem me obrigava a implementar. Esse foi o ponto que
me fez bater o martelo pelo Rust.

Obviamente você percebe que a escolha de Rust não foi uma escolha no vácuo,
como se não houvesse nada de relevante além de um "match" ao ver a
linguagem. Por outro lado, eu não queria estudar C/C++. Não por rejeitar, mas
porque achei que precisava me conectar com algo mais moderno, sem desmerecer a
relevância que tem e que ainda vai ter. Naquele momento, o meu mundo girava em
torno de web e linguagens que permitiam alta produtividade. O Rust é
uma linguagem mais jovem, com objetivos similares aos de C/C++.

# Conclusão

Como dizem, "o equilíbrio está em um pouco de veneno e um pouco de salada": a
escolha de Rust foi pelo objetivo da linguagem e pela sua qualidade. Por outro lado,
também foi a modernização e o design da linguagem — e todo o hype criado em
torno dela — que me levou a apreciar o seu estilo de código. Como foi dito antes,
o problema nunca são as preferências pessoais; o problema é quando elas acontecem
sem fundamento.
