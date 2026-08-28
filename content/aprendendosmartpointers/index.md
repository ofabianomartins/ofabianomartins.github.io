+++
title = "Aprendendo Smartpointers"
slug = "aprendendosmartpointers"
date = "2026-08-26"
+++

# Introdução

No ano passado e esse ano o meu investimento em desenvolvimento com Rust foi focado
em desenvolver apis Web e aplicações para projetos pessoais apenas para aprender
e ganhar tempo de escrita de código, mas sem se profundar. Esse ano eu procurei
desenvolver um projeto mais robusto em Rust e percebi que ainda tinha um gap de
conhecimento sobre as estruturas de manipulação de memória. Com isso, eu procurei
ajuda e vi que não sabia absolutamente nada de relevante sobre smartpointers. 
Então, vamos fazer uma introdução sobre esse assunto e o quais os pontos que 
você precisa saber para não ser um júnior em smartpointers.

# Sobre como o ownership atrapalha o desenvolvimento de software

Obviamente é ironia. Na verdade, o interesante em desenvolvimento com Rust é o
novo paradigma que aprimora a forma de escrever o código. Contudo, ainda é mais
desafiador do que condificar com ele. O objetivo é fazer com que o programa tenha
um comportamento mais determinado considerando a alocação de memória. 

Todo programa precisa alocar memória para temporariamente criar estruturas de
dados que vão ser usadas para calcular o seu resultado. Isso é indiscutível, mas
isso precisa levar em conta que a memória é limitada e que para o funcionamento
eficiente do programa é necessário manter na memória apenas o que é necessário
para o funcionamento atual do programa. A memória é um recurso limitado então o 
bom uso dela pode permitir uma execução mais eficiente do programa. O ponto é 
como garantir isso.

Existiam dois caminhos conhecidos: 1) fazer com que a alocação de memória
seja total responsabilidade do programador. E isso é ótimo porque é uma abordagem
bem eficiente permitindo que o programador sendo aquele que tem todo conhecimento
do algoritmo que o programa implementa vai saber alocar e desalocar memória no 
momento exato. Isso não onera a execução do sistema, mas exige do programador uma
atenção e responsabilidade que nem sempre ele vai ser capaz de cumprir. O peso
da liberdade é a responsabilidade por seus próprios atos; e 2) a utilização de uma
máquina virtual que ela iria ser esse intermediário na execução e alocação de 
memória. Essa máquina virtual é uma camada intermediária entre as comandos do 
programa e as operações em memória. Essa camada gera um custo adicional no momento
de execução porque a máquina virtual precisa fazer essa intermediação e garantir a 
eficiência da execução. E isso significa que o MV precisa determinar o que vai 
ser mantido na memória e o que vai sair. E isso tudo é feito considerando o código
escrito pelo programador que agora terceiriza sua responsabilidade para a máquina
virtual e paga com custo de eficiência em execução, mas tem em contrapatirda um
ganho de produtividade de entrega. 

Esses dois pontos eram sempre as escolhas feitas pela linguagem, ou você assume a 
responsabilidade e paga o preço ou você delega e paga o preço da mesma forma. 
O Rust foi a linguagem que popularizou um caminho intermediário que é aplicar 
regras na hora de alocar memória que permitissem ao compilador interpretar
automaticamente quando e onde alocar memória sem que isso fosse feito de forma 
explícita dependendo da ordem do programador.

Para entender, imagine que você precisa arrumar a sua estante de livros. Você pode
ser do tipo de pessoa que gosta de ordenar do seu próprio jeito e precisa que você
mesmo faça isso sempre que é a forma mais rápida do seu quarto ficar do seu jeito. 
Contudo, você pode ser do tipo da pessoa que prefere delegar isso para uma empregada
que você confia e que vai saber organizar a sua estante da melhor forma que ela 
puder, mas você não se importa com isso. Porém, você pode ter que achar aquele
livro específico e descobriu que ela trocou ele de prateleira. A proposta do Rust 
é que vocẽ organize como os livros vão se agrupar, mas quem vai executar isso é
a empregada. Ela vai obedecer o seu agrupamento, mas vai fazer de uma forma tão
alinhada com as suas escolhar que ela vai parecer que você mesmo arrumou os livros 
na estante. 

O que o Rust faz é impor mais algumas regras relacionadas ao alocação de variáveis
e passagem de parâmetros que garantem que o compilador vai ser capaz de detectar
quando e onde a memória precisa ser alocada e quando desalocar. As regras são:

1) Todo valor tem um owner (dono)
2) Você só pode ter um onwer por vez
3) Quando o escopo do owner acaba, o valor é desalocado da memória.

As regras servem para que todos os objetos alocados em memória sejam detectados
e se sabia quando entrar e quando sair da memória. Esse é o paradigma do Rust que
aprimora a capacidade de escrever programas garantindo a segurança de memória.

# Porém, ownership não é tudo

Apesar de muito eficiente para resolver a alocação de estruturas de dados na memória, 
você encontra uma dificuldade para implementar alguns algoritmos e seguir essas
regras. Por exemplo, ao implementar a lista de adjacências de um grafo você precisa
que as referências apareçam várias vezes para cada aresta que aquele vértice é 
conectado. Outra dificuldade é trabalhar com estruturas auto referentes que usando
as regras de onwership é impossível calcular o tamanho total da estrutura. Ou até
o caso clássico de criar uma vetor dinãmico. 

Quando você trabalha com um vetor de tamanho fixo é possível em tempo de compilação
determinar o tempo total do vetor durante toda a execução do programação. Isso 
não é possível para vetores dinâmicos se certificar dessas regras em tempo de 
compilação. Por isso, o Rust implementa estruturas de dados chamadas de 
`Smartpointers` que permitem seguir as regras nesses cenários em que o tempo de 
compilação não é capaz de determinar a segurança daquele código.

# Tipo de smartpoints e suas aplicações

Os Smartpointers permitem a aplicação das regras de onwership em estruturas que
exigem uma flexibilidade maior ao referenciar os dados em memória. Basicamente, 
Smartpointers são structs que fazem a gentão de memória na Heap usando um bloco
unsafe que permite mais flexibilidade ao alocar e desalocar memória. Então, o que
essas estruturas fazem é encapsular a gerência de memória e oferecer interfaces 
mais tão confiáveis quanto o Rust safe.

## Box\<T\>

É um ponteiro para um valor salvo na Heap. As variáveis locais geralmente são salvas
na região da stack porque são passageiras. Porém, alguns valores precisam ser
salvos na Heap que é uma região da memória dedicada a dados que precisam persistir
mais tempo que a região da stack. 

A mecânica desse componente é salvar na stack o endereço de memória que vai apontar
diretamente para a posição da heap que salva endereço do valor. A mutabilidade 
depende do valor apresentado e seu compartilhamento precisa ser explícito no 
código.

```rust
fn main() {
    let mut b: Box<i32> = Box::new(10);
    b = 20;

    println!("Valor: {:?}", b);
}
``` 

## Vec\<T\> e String

É uma estrutura que permite um vetor de tamanho varíavel. Os tutoriais não chegam
a tratar ele com essa abordagem, mas sem o Vec é necessário implementar uma 
estrutura de vetor dinâmico. O objetivo é criar uma versão do Box que permite uma
série de valores do mesmo tipo T. Esse ponteiro salva na stack o endereço de memória,
a capacidade do vetor e o tamanho.

A mutabilidade desse objeto é mais ligada ao endereço do que ao valores. Para
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

## Rc

É um ponteiro que pode ser diiaponibilizado para várias referências ao mesmo tempo.
O uso dele é exclusivo na mesma thread. O Rc pode ser classificao em dois 
tipos: 1) weak que é uma referências que tem acesso ao borrowed; e 2) Strong que é uma 
o ponteiro que tem o owned do valor. Conforme suas referências weak são removidas
o valor permanece na memória e só deve ser removido da memória quando todas as
referências são removidas da memória principalmente a Strong. Caso a Strong seja
removida quando ainda existem ponteiros Weak, um ponteiro é movido para ser o 
novo Strong. 

O objetivo é permitir que estruturas de dados que se alto referenciam várias vezes
podem ser manipuladas pela linguagem. O exemplo é um grafo que pode ter nós que 
conectam com vários outros. Esses nós podem ser referenciados por outros nós, 
essas só é possível se for usando um Rc\<T\> para permitir essas várias referências.

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

## Arc

É um valor que pode ser disponibilizado para várias referências ao mesmo tempo 
que poder ser usado por várias threads.

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

## RefCell

É um valor imutável que pode ser alterado em memória. O Rust não permite que você
tem tenha
vários acesso mutáveis(capazes de alterar) de uma variável ao mesmo tempo que 
acessos imutáveis de uma mesma variável. Ou seja, você só pode ter uma situação
por vez. O RefCell permite que essa regra seja verificada apenas em tempo de 
execução. Isso permite uma série de programas que não seriam aceitos pela 
análise estática do compilador Rust, mas que na prática não iria quebrar as regras
durante a execução do programa. Acontece que caso a regra seja quebrada ao usar o 
RefCell em execução ele dispara um `panic` durante a execução do programa

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


## Cow

É um ponteiro que permite que um objeto tenha várias referências e todos elas sendo
borrowed. No momento que uma delas é atualizada, o objeto se clona e salva o owned desse
novo valor não alterando as outras referências,



você atualiza a referência ele é torma o owned dessa referência sem apontar 
uma criação de mensagem

## Mutex

É um mutex que bloqueia o acesso quando o lock é obtido pro uma thread. Permite uma escrita.

## Rwlock

É um Mutex que permite a leitura de várias threads ao mesmo tempo, mas são bloqueadas
quando a uma thread usa a escrita.

# Conclusão


















