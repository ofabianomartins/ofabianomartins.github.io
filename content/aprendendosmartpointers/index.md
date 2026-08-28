+++
title = "Aprendendo Smartpointers"
slug = "aprendendosmartpointers"
date = "2026-08-28"
+++

# Introdução

No ano passado e neste ano, meu investimento em desenvolvimento com Rust foi focado
em desenvolver APIs Web e aplicações para projetos pessoais apenas para aprender
e ganhar tempo de escrita de código, mas sem me aprofundar. Este ano, procurei
desenvolver um projeto mais robusto em Rust e percebi que ainda tinha uma lacuna de
conhecimento sobre as estruturas de manipulação de memória. Com isso, procurei
ajuda e vi que não sabia absolutamente nada de relevante sobre smart pointers.
Então, vamos fazer uma introdução sobre esse assunto e quais são os pontos que
você precisa saber para não ser um júnior em smart pointers.

# Sobre como o ownership atrapalha o desenvolvimento de software

Obviamente é ironia. Na verdade, o interessante em desenvolvimento com Rust é o
novo paradigma que aprimora a forma de escrever o código. Contudo, ainda é mais
desafiador do que codificar com ele. O objetivo é fazer com que o programa tenha
um comportamento mais determinado considerando a alocação de memória.

Todo programa precisa alocar memória para temporariamente criar estruturas de
dados que vão ser usadas para calcular o seu resultado. Isso é indiscutível, mas
isso precisa levar em conta que a memória é limitada e que para o funcionamento
eficiente do programa é necessário manter na memória apenas o que é necessário
para o funcionamento atual do programa. A memória é um recurso limitado, então o
bom uso dela pode permitir uma execução mais eficiente do programa. O ponto é
como garantir isso.

Existiam dois caminhos conhecidos: 1) fazer com que a alocação de memória
seja de total responsabilidade do programador. E isso é ótimo porque é uma abordagem
bem eficiente, permitindo que o programador — aquele que tem todo o conhecimento
do algoritmo que o programa implementa — saiba alocar e desalocar memória no
momento exato. Isso não onera a execução do sistema, mas exige do programador uma
atenção e responsabilidade que nem sempre ele vai ser capaz de cumprir. O peso
da liberdade é a responsabilidade por seus próprios atos; e 2) a utilização de uma
máquina virtual que seria esse intermediário na execução e alocação de
memória. Essa máquina virtual é uma camada intermediária entre os comandos do
programa e as operações em memória. Essa camada gera um custo adicional no momento
de execução porque a máquina virtual precisa fazer essa intermediação e garantir a
eficiência da execução. E isso significa que a MV precisa determinar o que vai
ser mantido na memória e o que vai sair. E isso tudo é feito considerando o código
escrito pelo programador que agora terceiriza sua responsabilidade para a máquina
virtual e paga com custo de eficiência em execução, mas tem em contrapartida um
ganho de produtividade de entrega.

Esses dois pontos eram sempre as escolhas feitas pela linguagem, ou você assume a
responsabilidade e paga o preço ou você delega e paga o preço da mesma forma.
O Rust foi a linguagem que popularizou um caminho intermediário que é aplicar
regras na hora de alocar memória que permitissem ao compilador interpretar
automaticamente quando e onde alocar memória sem que isso fosse feito de forma
explícita, a critério do programador.

Para entender, imagine que você precisa arrumar a sua estante de livros. Você pode
ser do tipo de pessoa que gosta de ordenar do seu próprio jeito e que precisa fazer
isso pessoalmente, porque é a forma mais rápida de o quarto ficar do seu jeito.
Contudo, você pode ser do tipo de pessoa que prefere delegar isso para uma empregada
que você confia e que vai saber organizar a sua estante da melhor forma que ela
puder, mas você não se importa com isso. Porém, você pode ter que achar aquele
livro específico e descobriu que ela trocou ele de prateleira. A proposta do Rust
é que você organize como os livros vão se agrupar, mas quem vai executar isso é
a empregada. Ela vai obedecer o seu agrupamento, mas vai fazer de uma forma tão
alinhada com as suas escolhas que ela vai parecer que você mesmo arrumou os livros
na estante.

O que o Rust faz é impor mais algumas regras relacionadas à alocação de variáveis
e passagem de parâmetros que garantem que o compilador vai ser capaz de detectar
quando e onde a memória precisa ser alocada e quando desalocar. As regras são:

1. Todo valor tem um owner (dono)
2. Você só pode ter um owner por vez
3. Quando o escopo do owner acaba, o valor é desalocado da memória.

As regras servem para que todos os objetos alocados em memória sejam detectados
e se saiba quando entrar e quando sair da memória. Esse é o paradigma do Rust que
aprimora a capacidade de escrever programas garantindo a segurança de memória.

# Porém, ownership não é tudo

Apesar de muito eficiente para resolver a alocação de estruturas de dados na memória,
você encontra uma dificuldade para implementar alguns algoritmos e seguir essas
regras. Por exemplo, ao implementar a lista de adjacências de um grafo você precisa
que as referências apareçam várias vezes para cada aresta à qual aquele vértice
está conectado. Outra dificuldade é trabalhar com estruturas autorreferentes que, usando
as regras de ownership, é impossível calcular o tamanho total da estrutura. Ou até
o caso clássico de criar um vetor dinâmico.

Quando você trabalha com um vetor de tamanho fixo, é possível em tempo de compilação
determinar o tamanho total do vetor durante toda a execução do programa. Para
vetores dinâmicos, não é possível garantir essas regras em tempo de
compilação. Por isso, o Rust implementa estruturas de dados chamadas de
`Smart Pointers` que permitem seguir as regras nesses cenários em que o tempo de
compilação não é capaz de determinar a segurança daquele código.

# Tipos de smart pointers e suas aplicações

Os smart pointers permitem a aplicação das regras de ownership em estruturas que
exigem uma flexibilidade maior ao referenciar os dados em memória. Basicamente,
smart pointers são structs que fazem a gestão de memória na heap usando um bloco
`unsafe` que permite mais flexibilidade ao alocar e desalocar memória. Então, o que
essas estruturas fazem é encapsular a gerência de memória e oferecer interfaces
tão confiáveis quanto o Rust seguro.

## Box<T>

É um ponteiro para um valor salvo na Heap. As variáveis locais geralmente são salvas
na região da stack porque são passageiras. Porém, alguns valores precisam ser
salvos na Heap que é uma região da memória dedicada a dados que precisam persistir
mais tempo que a região da stack.

A mecânica desse componente é salvar na stack o endereço de memória que vai apontar
diretamente para a posição na heap onde o valor está salvo. A mutabilidade
depende do valor apresentado e seu compartilhamento precisa ser explícito no
código.

```rust
fn main() {
    let mut b: Box<i32> = Box::new(10);
    b = 20;

    println!("Valor: {:?}", b);
}
```

## Vec<T> e String

É uma estrutura que permite um vetor de tamanho variável. Os tutoriais não chegam
a tratá-lo com essa abordagem, mas sem o `Vec` é necessário implementar uma
estrutura de vetor dinâmico. O objetivo é criar uma versão do Box que permite uma
série de valores do mesmo tipo T. Esse ponteiro salva na stack o endereço de memória,
a capacidade do vetor e o tamanho.

A mutabilidade desse objeto é mais ligada ao endereço do que aos valores. Para
incluir e remover objetos deve-se usar as funções push, pop, insert e remove.

```rust
fn main() {
    let mut vetor: Vec<u64> = Vec::new();
    let mut i: u64 = 0;

    while i < 10 {
        vetor.push(i);
        i += 1;
    }

    println!("Vetor: {:?}", vetor);
}
```

## Rc<T>

É um ponteiro que pode ser disponibilizado para várias referências ao mesmo tempo.
O uso dele é exclusivo na mesma thread. O Rc pode ser classificado em dois
tipos: 1) Weak, que é uma referência que tem acesso ao borrowed; e 2) Strong, que é o
ponteiro que tem o owned do valor. Conforme suas referências Weak são removidas,
o valor permanece na memória e só deve ser removido da memória quando todas as
referências são removidas, principalmente a Strong. Caso a Strong seja
removida quando ainda existem ponteiros Weak, um ponteiro é movido para ser o
novo Strong.

O objetivo é permitir que estruturas de dados que se autorreferenciam várias vezes
possam ser manipuladas pela linguagem. O exemplo é um grafo que pode ter nós que
conectam a vários outros. Esses nós podem ser referenciados por outros nós;
isso só é possível usando um `Rc<T>` para permitir essas várias referências.

```rust
enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::rc::Rc;

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    let b = Cons(3, Rc::clone(&a));
    let c = Cons(4, Rc::clone(&a));
}
```

## Arc<T>

É um valor que pode ser disponibilizado para várias referências ao mesmo tempo
e pode ser usado por várias threads.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

## RefCell<T>

É um valor imutável que pode ser alterado em memória. O Rust não permite que você
tenha vários acessos mutáveis (capazes de alterar) a uma variável ao mesmo tempo que
acessos imutáveis à mesma variável. Ou seja, você só pode ter uma situação
por vez. O RefCell permite que essa regra seja verificada apenas em tempo de
execução. Isso permite uma série de programas que não seriam aceitos pela
análise estática do compilador Rust, mas que na prática não quebrariam as regras
durante a execução do programa. Acontece que, caso a regra seja quebrada ao usar o
RefCell em execução, ele dispara um `panic` durante a execução do programa.

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
        sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages.borrow_mut().push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(&mock_messenger, 100);

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.borrow().len(), 1);
    }
}
```

## Cow<T>

É um ponteiro que permite que um objeto tenha várias referências, todas elas sendo
borrowed. No momento em que uma delas é atualizada, o objeto se clona e salva o owned desse
novo valor, sem alterar as outras referências. Isso é uma implementação que evita a replicação de dados e garante a independência de posse de cada informação.

```rust
use std::borrow::Cow;

/// Sanitiza um texto: se não houver espaços extras, retorna o dado por
/// referência (&str).
/// Se houver espaços extras, clona e retorna um valor próprio (String).
fn sanitizar_texto<'a>(input: &'a str) -> Cow<'a, str> {
    if input.contains("  ") {
        // Precisa modificar: cria uma versão modificada (Cow::Owned / String)
        let texto_limpo = input.replace("  ", " ");
        Cow::Owned(texto_limpo)
    } else {
        // Não precisa modificar: retorna a própria referência 
        // sem alocar na Heap (Cow::Borrowed / &str)
        Cow::Borrowed(input)
    }
}

fn main() {
    // CASO 1: Texto já está limpo (Zero alocações na Heap)
    let texto_valido = "Rust é incrível!";
    let resultado1 = sanitizar_texto(texto_valido);

    match resultado1 {
        Cow::Borrowed(s) => println!("[Zero Alocação]  referência direta: \"{}\"", s),
        Cow::Owned(s) => println!("[Alocado] Criou uma nova String: \"{}\"", s),
    }

    // CASO 2: Texto precisa de alterações (Ocorre a clonagem/alocação)
    let texto_sujo = "Rust  é  incrível!"; // Espaços duplos
    let resultado2 = sanitizar_texto(texto_sujo);

    match resultado2 {
        Cow::Borrowed(s) => println!("[Zero Alocação] referência direta: \"{}\"", s),
        Cow::Owned(s) => println!("[Alocado] Criou uma nova String: \"{}\"", s),
    }

    // CASO 3: Alterando diretamente via `to_mut()`
    let mut dado: Cow<str> = Cow::Borrowed("texto original");
    
    // Até aqui é apenas uma referência &'static str.
    // O método .to_mut() força a clonagem e transforma o Cow em uma String mutável.
    dado.to_mut().push_str(" (modificado)");

    println!("Resultado final: {}", dado);
}
```

# Conclusão

A proteção de memória é um paradigma que deve ser considerado para aprimorar a qualidade do desenvolvimento de software e voltar ao uso de linguagens compiladas no dia a dia da programação Web. O tempo de aprimoramento do desenvolvedor ainda será maior que em outras linguagens porque o nível de abstração é bem menor, mas o ganho de performance e aproveitamento de recursos será muito superior, valendo o custo-benefício. Por outro lado, novos paradigmas exigem novas estratégias para implementar o código em estruturas que garantem a segurança de memória. Smart pointers são estruturas de ponteiros que permitem manipular a memória usando interfaces seguras para garantir o comportamento do programa que a análise estática de código não consegue prever. Ainda haverá a oportunidade de programas terem problemas durante a sua execução, mas é garantido que uma classe enorme de programas agora terá a sua execução garantida pelas regras do borrow checker.





