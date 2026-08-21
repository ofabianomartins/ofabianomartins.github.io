+++
title = "Porque que comecei a estudar rust?"
slug = "porque-rust"
date = "2026-04-20"
+++

Meu último artigo foi sobre o fato que escolher linguagens em time de desenvolvimento
sempre é uma escolha influenciada pelos viéses. Essa ideia de uma solução
100% técnica é rara e só acontece principalmente em ambientes que você tem problemas
de escala. A maioria vai seguir vieses que estão ligados a situações muito comuns 
ou conveniências de contexto. Um exemplo bem claro é usar React ou Vue? 
Se pergunte porque ninguém considera usar WebAssembly? Porque claramente é mais 
prático usar o framework mais popular porque você tem o ganho de encontrar 
desenvolvedores, desenvolvedores mais baratos e a quantidade de conteúdo e
experiência aplicada disponível é bem superior. 

Parece uma solução técnica, mas não é! Não estamos debatendo o tempo de resposta
ou a eficiência do consumo de memória. É só o mais conveniente para o time e 
para o negócio. Isso não é um problema! Só problemático achar que a sua decisão 
baseada no seu viés de conveinência é uma solução técnica objetivamente embasada.
Isso é maior responsável por débitos técnicos e escolhas ruins feitos em pequenos,
médios negócios. 

Então Rust foi uma escolha super objetiva e baseada em requisitos puramente técnicos?
Óbvio que não! Mas eu imagino que estou fazendo uma aposta numa linguagem com
coisas a dizer e novas coisas a entregar. Porque para nós o povo que coda, o 
importante é aprender paradigmas e não linguagens. E o Rust com esse movimento
de segurança de memória sem o uso de Garbage Collectors (GC) é de fato uma novidade
interessante. 

# Antes de começar, vamos ver exemplos

Quando eu comecei a programar em 2013 em Ruby On Rails eu aprendi duas informações 
valiozas: 1) TDD é uma forma de construir código de forma consistente; 2) o Ruby
On Rails me ensinou este método de trabalho. Essa foi a primeira vez que eu aprendi
a instrumentalizar o meu estudo e não só obedecer o que externamente parecia fazer 
sentido. Nesse processo eu li dois livro para aprimorar o meu método de desenvolver
TDD e não só aprender as interfaces. Então eu aprendi que escrever TDD não é só escrever
um teste antes de implementar, mas aprender que são necessários dois testes para 
testar o contra exemplo. O importante é entender que o valor da ferramenta está
no método que ela implementa. 

Depois disso, eu tive que aprender frameworks Javascript/Typescript mais pelo hype, 
mas ainda assim eu aprendi a estruturar frontends. Como arquiteturar essas novas 
aplicações que toda a parte visual é independente isso tem os seus prós e contras. 
Em toda ferramenta ou etapa que você pode aprender conceitos de base é o que
realmente deve ser levadas e incorporadas no seu repertório de conceitos. 

A última grande ferramenta que eu aprendi e que tinha um grande conceito por trás
é o Apache Kafka e a orientação a eventos. Eu estava a acostumando a sempre 
integrar sistemas de forma síncrona com processos feitos a mão em que dava mais 
trabalho criar uma interface para um usuário do backoffice do que meter a mão 
no console. Aprender orientação a eventos foi uma revolução na minha forma de
projetar sistemas. Por mais que pareça entusiamos com um brinquedo novo é porque
muitos problemas que eu precisaria de trabalho de orquestração tão grande passou
a ser uma coisa natural e evidente. Isso depois de mais de 10 anos de estudo 
de programação e ciência de computação. Essa é a verdadeira importância de não 
parar de estudar.

# E qual é o método do Rust

O objetivo do estudo do Rust antes de tudo está ligado a voltar a linguagens
compiladas. Depois de 15 anos escrevendo muito código e com muito volume de entrega
eu vi que está confortável não só com os frameworks, mas também com facilidades
de debug e não pensar como extrair o máximo de eficiência. E logo comecei a 
procurar todas as linguagens compiladas que eu poderia estudar. Dentre todas eu
percebi que havia uma linguagem que só me faria lembrar como é trabalhoso programar
sem uma máquina virtual limpando a sua sujeira. Uma outra linguagem que fazia com 
que os total controle a ponto de ser paranóico.
E finalmente uma linguagem que faria o que era impossível: ter a experiência de
um garbage collector sem o overhead da máquina virtual. Não existe almoço grátis,
então pensei que você teria que aplicar conceitos de programação que nenhum
outra linguagem obrigatorimente me obrigava a implementar. Esse foi o ponto que
me fez bater o martelo para o Rust.

Obviamente você percebe que a escolha de Rust não foi uma esolha no vácuo 
simplesmente que não teria nada de relevante a não ser um "match" ao ver a 
linguagem. Por outro lado, eu não queria estudar C/C++. Não por rejeitar, mas 
achei que precisava me conectar com algo mais moderno e não desmerecendo a 
relevância que tem e que ainda vai ter. Naquele momento, o meu mundo girava em 
torno de Web e linguagens que permitiam alta produtividade. O Rust sendo
uma linguagem mais jovem e com objetivos similares a C/C++. 

# Conclusão 

Como dizem "o equilíbrio está em um pouco de veneno e um pouco de salada", a 
escolha de Rust foi pelo objetivo da linguagem e a sua qualidade. Por outro lado, 
também foi a modernização e design da linguagem que tem todo um hype criado em 
volta dela que me levou a apreciar o seu estilo de código. Como foi dito antes, 
o problema nunca são as preferências pessoais, o problema é quando elas acontecem
sem fundamento.
