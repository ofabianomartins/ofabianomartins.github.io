+++
title = "Learning Smart Pointers"
slug = "learning-smart-pointers"
date = "2026-08-28"
+++

# Introduction

Last year and this year, my investment in Rust development was focused on building
Web APIs and applications for personal projects just to learn and get more coding
time, but without going deep. This year, I set out to build a more robust project
in Rust and realized I still had a gap in my knowledge of memory management
structures. With that, I looked for help and saw that I knew absolutely nothing
relevant about smart pointers. So let's do an introduction to this topic and
cover the points you need to know so you're not a junior when it comes to smart
pointers.

# How ownership gets in the way of software development

Obviously, that's irony. In reality, what's interesting about Rust development is
the new paradigm that improves the way you write code. Still, it's more challenging
than coding with it. The goal is to make the program behave in a more deterministic
way when it comes to memory allocation.

Every program needs to allocate memory to temporarily create data structures that
will be used to compute its result. That's indisputable, but it has to account for
the fact that memory is limited and that, for the program to run efficiently, only
what is needed for its current operation should stay in memory. Memory is a limited
resource, so using it well can allow the program to run more efficiently. The
question is how to guarantee that.

There were two well-known paths: 1) make memory allocation entirely the programmer's
responsibility. That's great because it's a very efficient approach, allowing the
programmer—the one who has full knowledge of the algorithm the program
implements—to allocate and deallocate memory at exactly the right moment. That
doesn't burden system execution, but it demands attention and responsibility from
the programmer that they won't always be able to meet. The weight of freedom is
responsibility for your own actions; and 2) using a virtual machine as that
intermediary in execution and memory allocation. That virtual machine is an
intermediate layer between the program's commands and memory operations. That layer
adds an extra cost at execution time because the virtual machine has to mediate and
ensure execution efficiency. And that means the VM has to determine what stays in
memory and what goes away. All of that is done based on the code written by the
programmer, who now outsources their responsibility to the virtual machine and pays
with execution efficiency, but gains delivery productivity in return.

Those two options were always the choices made by the language: either you take
responsibility and pay the price, or you delegate and pay the price just the same.
Rust was the language that popularized an intermediate path: applying rules when
allocating memory that let the compiler automatically infer when and where to
allocate memory without the programmer doing it explicitly.

To understand, imagine you need to organize your bookshelf. You might be the kind of
person who likes to sort things your own way and needs to do it yourself, because
that's the fastest way to get the room the way you want it. Or you might be the
kind of person who prefers to delegate that to a housekeeper you trust, who will
organize your shelf as best she can, and you don't mind. But then you might need to
find a specific book and discover she moved it to another shelf. Rust's proposal is
that you decide how the books will be grouped, but the housekeeper executes it. She
will follow your grouping, but in a way so aligned with your choices that it will
look like you organized the shelf yourself.

What Rust does is impose a few more rules related to variable allocation and
parameter passing that ensure the compiler can detect when and where memory needs
to be allocated and when to deallocate it. The rules are:

1. Every value has an owner
2. You can only have one owner at a time
3. When the owner's scope ends, the value is deallocated from memory.

These rules exist so that all objects allocated in memory are tracked and you know
when they enter and leave memory. That's Rust's paradigm, which improves your
ability to write programs while guaranteeing memory safety.

# But ownership isn't everything

Although it's very effective for solving the allocation of data structures in
memory, you'll run into difficulty implementing some algorithms while following
these rules. For example, when implementing a graph's adjacency list, you need
references to appear multiple times for each edge that vertex is connected to.
Another difficulty is working with self-referential structures that, using
ownership rules, make it impossible to compute the structure's total size. Or even
the classic case of creating a dynamic vector.

When you work with a fixed-size vector, it's possible at compile time to determine
the vector's total size for the entire program execution. For dynamic vectors, it's
not possible to guarantee these rules at compile time. That's why Rust implements
data structures called `Smart Pointers` that allow you to follow the rules in
scenarios where compile time can't determine the safety of that code.

# Types of smart pointers and their uses

Smart pointers allow ownership rules to be applied to structures that require
greater flexibility when referencing data in memory. Basically, smart pointers are
structs that manage heap memory using an `unsafe` block that allows more flexibility
when allocating and deallocating memory. So what these structures do is encapsulate
memory management and offer interfaces as reliable as safe Rust.

## Box<T>

It's a pointer to a value stored on the heap. Local variables are usually stored in
the stack region because they're short-lived. However, some values need to be stored
on the heap, a memory region dedicated to data that must persist longer than the
stack region.

The mechanics of this component are to store on the stack the memory address that
points directly to the position on the heap where the value is stored. Mutability
depends on the value presented, and sharing it must be explicit in the code.

```rust
fn main() {
    let mut b: Box<i32> = Box::new(10);
    b = 20;

    println!("Valor: {:?}", b);
}
```

## Vec<T> and String

It's a structure that allows a variable-size vector. Tutorials don't always treat
it this way, but without `Vec` you need to implement a dynamic vector structure
yourself. The goal is to create a version of Box that allows a series of values of
the same type T. This pointer stores on the stack the memory address, the vector's
capacity, and its length.

This object's mutability is more tied to the address than to the values. To add and
remove items, you should use the push, pop, insert, and remove functions.

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

It's a pointer that can be made available to several references at the same time.
Its use is exclusive to the same thread. Rc can be classified into two types: 1)
Weak, which is a reference that has access to the borrowed value; and 2) Strong,
which is the pointer that owns the value. As Weak references are removed, the value
remains in memory and should only be removed when all references are removed,
especially the Strong one. If the Strong reference is removed while Weak pointers
still exist, a pointer is moved to become the new Strong.

The goal is to allow data structures that self-reference multiple times to be
handled by the language. The example is a graph that can have nodes connecting to
several others. Those nodes can be referenced by other nodes; that's only possible
using an `Rc<T>` to allow those multiple references.

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

It's a value that can be made available to several references at the same time and
can be used by several threads.

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

It's an immutable value that can be changed in memory. Rust doesn't allow you to
have several mutable accesses (capable of changing) to a variable at the same time
as immutable accesses to the same variable. In other words, you can only have one
situation at a time. RefCell allows that rule to be checked only at runtime. That
allows a range of programs that wouldn't be accepted by Rust's static analysis, but
that in practice wouldn't break the rules during program execution. However, if the
rule is broken when using RefCell at runtime, it triggers a `panic` during program
execution.

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

It's a pointer that allows an object to have several references, all of them
borrowed. When one of them is updated, the object clones itself and stores the
owned copy of that new value, without changing the other references. This is an
implementation that avoids data duplication and guarantees independent ownership of
each piece of information.

```rust
use std::borrow::Cow;

/// Sanitizes text: if there are no extra spaces, returns the data by
/// reference (&str).
/// If there are extra spaces, clones and returns an owned value (String).
fn sanitize_text<'a>(input: &'a str) -> Cow<'a, str> {
    if input.contains("  ") {
        // Needs modification: creates a modified version (Cow::Owned / String)
        let clean_text = input.replace("  ", " ");
        Cow::Owned(clean_text)
    } else {
        // No modification needed: returns the reference itself
        // without allocating on the heap (Cow::Borrowed / &str)
        Cow::Borrowed(input)
    }
}

fn main() {
    // CASE 1: Text is already clean (zero heap allocations)
    let valid_text = "Rust is amazing!";
    let result1 = sanitize_text(valid_text);

    match result1 {
        Cow::Borrowed(s) => println!("[Zero Allocation] direct reference: \"{}\"", s),
        Cow::Owned(s) => println!("[Allocated] Created a new String: \"{}\"", s),
    }

    // CASE 2: Text needs changes (cloning/allocation occurs)
    let dirty_text = "Rust  is  amazing!"; // Double spaces
    let result2 = sanitize_text(dirty_text);

    match result2 {
        Cow::Borrowed(s) => println!("[Zero Allocation] direct reference: \"{}\"", s),
        Cow::Owned(s) => println!("[Allocated] Created a new String: \"{}\"", s),
    }

    // CASE 3: Changing directly via `to_mut()`
    let mut data: Cow<str> = Cow::Borrowed("original text");

    // Up to here it's just a &'static str reference.
    // The .to_mut() method forces cloning and turns Cow into a mutable String.
    data.to_mut().push_str(" (modified)");

    println!("Final result: {}", data);
}
```

# Conclusion

Memory protection is a paradigm that should be considered to improve software
development quality and bring compiled languages back into everyday web programming.
The time it takes for a developer to improve will still be longer than with other
languages because the level of abstraction is much lower, but the performance gains
and resource utilization will be far superior, making the trade-off worthwhile. On
the other hand, new paradigms require new strategies to implement code in structures
that guarantee memory safety. Smart pointers are pointer structures that allow you
to manipulate memory using safe interfaces to guarantee program behavior that static
code analysis can't predict. There will still be room for programs to have problems
during execution, but it's guaranteed that an enormous class of programs will now
have their execution guaranteed by the borrow checker's rules.

