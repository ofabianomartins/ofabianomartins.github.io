+++
title = "Escolheu porque quis!"
slug = "escolheu-porque-quis"
date = "2026-04-18"
+++

Se você já trabalhou em alguma empresa pequena de software, e quando eu 
chamo de pequena é uma empresa que não tem governança para
personalizar o sua própria stack de desenvolvimento, sempre vai estar
na mesa a discussão de qual a linguagem a ser usada num próximo projeto. 
As "facções" vão defender a sua linguagem de preferência e isso pode ser
uma discussão saudável ou um verdadeiro embate! O verdadeiro problema nunca 
está nesse debate, mas o que está porque trás dele e o que realmente importa
na seleção de um linguagem de programação.

# Uma empresa amadurecida

Quando colocamos a governança como parâmetro de tamanho de
um empresa estamos querendo dizer que o importante é ter uma estabilidade na linguagem dos produtos que permita uma base de comunicação entre todos os projetos
e times. Isso é difícil de ser feito e não deve ser perfeito, até porque ninguém vai usar uma linguagem web 
para desenvolvimento de dispositivos embarcados e se alguém falar isso questione a profundidade de conhecimento do seu interlocutor ou se você entendeu o que ele está falando. 

O importante não que é todos usem exatamente a mesma stack ou que todos usem o mesmo framework para desenvolvimento. 
Os principais fluxos de trabalhos devem permitir que os times possam ser alterados e recombinados dado a necessidade de alocação de recursos da empresa. 
Ficar contando com a aptidão individual do desenvolvedor para intercambiar entre projetos deve ser considerado. Porém a realidade do grupo deve ser levado em consideração.

Porque o principal diferencial da um profissional sênior de um júnior dentro de uma empresa são os conhecimentos obtidos dentro da experiência de trabalho que o fazem capaz de resolver problemas dentro da estrutura organizacional. Ou seja, sabe aonde mexer para resolver um problema é mais importante do que ser um teórico de uma linguagem ou framework. E com isso quanto mais diversificado forem as decisões de stack e de arquitetura mais dependendente dos indívíduos chave que dominaram esses conhecimentos específicos.

# O dilema de performance versus entrega

Quando eu leciono programação o primeiro assunto é ensinar o modelo de von newman para entender como funciona o relacionamento entre o que você está escrevendo e uma abstração decente da sua máquina em que você executa esse sistema. Só que aprensentar um conteúdo não é o mesmo que ser absorvido pelas pessoas. Então para iniciantes uma linguagem exigente com C é complicado e pouco eficiente para a pessoa produzir resultados. Existem linguagens bem menos exigentes do ponto de vista de sintaxe e abstração dos mecanismo de memória. Porém, esse abertura para resultados tem seu custo para um linguagem que consiga lidar com os detalhes que o desenvolvedor não pode lidar. Só que essa facilidade aumenta a entrega de desenvolvedores mais experientes.

Logo, a doação de liguagem de mais auto nível torna possível iniciantes produzirem resultados e torna experiente muito mais produtivos porque eles não precisam lidar com detalhes que não devem ser necessários para o resultado final. Porém, alguém tem que fazer isso! Então quem faz é o Virtual machine que essa linguagem executa aplicando o Garbage Collector para liberar o espaço de memória que o programador não vai usar mais. 

Essa virtual machine e o garbage collector são os preços a serem pagos pela facilidade e o volume de entrega. Numa sistema em que você precisa entregar um grande volume de features, mas são poucos usuários esse preço é bem barato porque o objetivo de fato vai ser em lidar com vários processo que não tem uma execução crítica. No caso de um sistema com alto volume de requisições isso vai ser um problema a ser otimizado. A troca de linguagem não é uma necessidade imediata, mas pode com certeza haverá uma refatoração a ser feita para lidar com o aumento do volume de requisições.

# Como selecionamos nossa liguagem de programação individualmente 

A psicologia desenvolvimentista nos ensina que o primeiro gatilho para que uma pessoa faça parte do pacto social é o pertencimento a um grupo. Ou seja, você não sabe muita coisa e qual a melhor forma de ser aceito? Repita o comportamento de quem aparece ser o mais socialmente aceito e que cabe dentro das suas aptidões. Isso acaba sendo a forma mais fácil de entender porque determinadas linguagens são adotadas amplamente. Compreender que nós inerentemente vamos nos juntar a grupo majoritários ou que pelo menos sejam fortes o suficiente para nos proteger é humano e não outra coisa.

As nossas ações geralmente serão conduzidas pelas nossas inclinações pessoais mesmo que tenhamos boas desculpas. Uma pessoa com apetite ao risco sempre vai fazer escolhas arriscadas como necessárias quando é pura busca por adrenalina, uma pessoa muito presa a rotina vai induzir ao que ela está acostumanda alegando que é melhor porque funciona para a ela. Isso não é um problema, o problema é você não ter noção dessas inclinações. Uma vez trabalhei com um cara que chegava toda semana com uma grande novidade que deveríamos aplicar que era melhor e o mercado estava demandando. Na verdade, ele só seguia hype e vivia perseguindo essas trends. Ele implementou um novo sistema da empresa nessas linguagens do hype, na hora de entregar ele não conseguiu fazer funcionar. Ele foi disponibilizado ao mercado. 

O problema não era a linguagem! Ele tinha a inclinação de estar aberto a novidades e na cabeça dele estar entregando na linguagem do hype era uma qualidade que seria relevante, mas funcionar é mais importante que isso. Depois dele ser disponibilizado ao mercado, nosso gestor me disse algo que eu nunca esqueci: "eu não tenho problema com novidades, mas você precisa conseguir bancar suas entregas". Isso é o que define se sua escolha pessoal é justa ou não, se ela consegue ser bacanda por você e/ou pelo time e gerar resultado. Sem isso tanto faz!

Uma vez eu conversando com um consultor respeitado comecei um debate sobre qual linguagem seria a mais interessante e competente. Ele não piscou e falou de Java! Seu olhos se encheram de lágrimas e ele começou a falar as qualidades do Java e como a linguagem tem evoluído com as versões e tem sido aplicada no mercado. Isso não tem nada a ver com o fato que ele tinha um carreira de mais de 20 anos com Java e que tinha uma grande carteira de clientes que ele dava manutenção e ficava rodando entre eles. Isso não é um problema! O problema é se ele não for capaz de adequar a mudanças de cenários. O que ele é plenamente capaz!

Fui forjado num curso técnico que começou com Object Pascal, continuou com Java e aprendemos PHP. Eu nunca tinha visto ruby antes de sair do técnico e ter conseguido meu primeiro emprego com júnior em Ruby 1.9.8. Basicamente, eu só trabalhei nessa stack acrescentando Javascript e python em alguns projetos de teste. Mas o que pagou as minhas contas nos últimos 10 anos foi Ruby on Rails, e não é de surpreender que a última vez que eu iniciei um projeto do zero foi em Ruby on Rails que era aonde eu me sentia confortável para desenvolver! Isso não é o problema! O problema é que hoje eu estudo Rust e no final eu estou querendo traçar paralelos entre linguagens que foram criadas com objetivos e resultados diferentes. 

Por fim, fica bem claro que ter escolhas pessoais não é o problema. O problema são as consequências das escolhas que são baseadas em inclinações e você despois não consegue dar conta. Escolhas declaradamente pessoais não são um problema. O problema é saber medir as consequências dessas escolhas!

# Tá, qual é p**** da decisão que eu tenho que tomar? 

Eu não sei, mas o que eu sei é que você tem que sempre prestar atenção em três tendências ao avaliar a decisão de um time de desenvolvimento!

1. Tendência pessoal de quem bate o martelo
2. Tendência do time e seus recursos técnicos disponíveis
3. Requisitos técnicos do negócio.

A ordem é de cima para baixo. Porém, quanto maior é a quantidade de usuários a ordem se inverte. Começando com projetos de poucos usuários, sempre quem vai prevalecer é a escolha individual de quem decide. Se a necessidades do time forem relevante o suficiente a decisão pode ser tendenciosa para o time, mas o gestor vai escolher o que mais lhe parece confortável. E como na maioria dos casos de software pequenos tanto faz, qualquer linguagem utilizada com bom senso vai resolver o problema.

A ordem se inverte quando a infra começa romper o limite de custo. Quando o volume de notificações de bug por indisponibilidade aumenta. Isso induz o time a ficar mais estressado tendo que fazer horas extras da dar conta de indisponibilidade. E principalmente, quando esses problemas se refletem numa perda da taxa de conversão e consumo dos clientes. Nesse ponto o gestor que toma a decisão só quer que o problema seja resolvido e a crise se estabilize. Então a decisão vai ser enviesada, mas o que enviesa mais é o resultado prático. 

E agora, que o foco principal foi a necessidade do sistema você deve pensar que sim foi tomada uma decisão correta e esse é a forma correta de tomar decisões! E não é verdade! O que aconteceu é que o que mais impulsionou foi a necessidade de entrega de resultado e estabilizaão do sistema, mas isso passou pelo filtro do que o time era capaz de entregar e o que o tomador de decisão estava disposto a fazer. Continua tendo vieses, mas a preponderância foi o problema real. E mesmo com o problema real sendo o pivô da mudança é possível que a escolha seja ruim pela limitação do time. 

Então não existe decisão correta?! Isso, o que existe são decisões que resolvem os problemas de hoje e se você foi capaz de tomar uma decisão que ao longo do tempo gerou ganhos ou foi somente uma decisão enviesada pelas circusntâncias? O importante não é tomar a melhor decisão o importante é tomar uma decisão que não vire um débito depois ou que você não consiga pagar. Esse é o ponto mais importante. 

# Mas com ia agora isso tudo vai mudar!

Eu não tenho tanta certeza. O que a ia fez foi transformar todos os desenvolvedores de software em vendedores de bananas. Isso significa que o produto deles que era caro e a diferença competitiva que eles tinham por causa da qualificação diminuiu. Sempre houve vendedores de banana e eles pagaram suas contas e sustentaram suas famílias. Por mais que hoje você tenha uma melhor forma de estocar, transferir e alocar ainda são necessários intermediários para tomar risco e assumir responsabilidades. A IA não vai tomar decisões! Ela pode ser capaz de auxiliar informando probabilidades e ajudando a melhorar as decisões, mas ela não vai ser o tomador de decisão. Ela não é um ente capaz de tomar riscos. E no dia que ela for, a linguagem de programação não vai ser o seu maior problema. 

# Conclusão

O objetivo era mostrar que a decisão de qual linguagem de programação está longe de ser uma decisão puramente técnica ou que não ser puramente técnica é um problema. O que importa é se as consequências da decisão escolhidas são capazes de serem bacadas pelo time de desenvolvimento e se as cincurstâncias mudarem é possível ajustar a rota. Enfim, decidir a linguagem de programação nunca é uma tarefa simples se você está fazendo algo que importa. Espero que um dia tenha a oportunidade de ver a diferença entre essas decisões.
