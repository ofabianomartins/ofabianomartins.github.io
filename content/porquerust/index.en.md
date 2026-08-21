+++
title = "Why I Started Learning Rust"
slug = "why-i-started-learning-rust"
date = "2026-04-20"
+++

My last article was about how choosing languages on development teams
is always a choice influenced by biases. The idea of a
100% technical solution is rare and mainly happens in environments where you face
scale problems. Most people will follow biases tied to very common situations
or contextual conveniences. A clear example: React or Vue?
Ask yourself why nobody considers using WebAssembly. It happens because it's more
practical to use the most popular framework: you gain in finding
developers, in paying less for them, and the amount of content and
applied experience available is far superior.

It looks like a technical solution, but it isn't! We're not debating response time
or memory consumption efficiency. It's just what's most convenient for the team and
the business. That's not a problem! What's problematic is thinking that your decision
based on a convenience bias is an objectively grounded technical solution.
That's what most often leads to technical debt and poor choices made in small
and medium-sized businesses.

So was Rust a super objective choice based on purely technical requirements?
Obviously not! But I imagine I'm making a bet on a language with
something to say and new things to deliver. For people who code, what
matters is learning paradigms, not languages. And Rust, with this movement
toward memory safety without garbage collectors (GC), is genuinely an interesting
novelty.

# Before we begin, let's look at some examples

When I started programming in 2013 with Ruby on Rails, I learned two valuable
pieces of information: 1) TDD is a way to build code consistently; 2) Ruby
on Rails taught me that way of working. That was the first time I learned
to instrument my own study and not just follow what externally seemed to make
sense. In that process, I read two books to improve my method of developing
with TDD and not just learning the interfaces. Then I learned that writing TDD isn't just writing
a test before implementing, but understanding that you need two tests to
cover the counterexample. What matters is understanding that the value of the tool lies
in the method it implements.

After that, I had to learn JavaScript/TypeScript frameworks mostly because of the hype,
but I still learned how to structure frontends. How to architect applications where
the entire visual layer is independent—that has its pros and cons.
In every tool or stage where you can learn foundational concepts, that's what
should really be carried forward and incorporated into your repertoire of ideas.

The last major tool I learned that had a big concept behind it
was Apache Kafka and event orientation. I was getting used to always
integrating systems synchronously, with hand-built processes, where it took more
work to create an interface for a backoffice user than to get my hands dirty
in the console. Learning event orientation was a revolution in the way I
design systems. As much as it may seem like enthusiasm for a new toy, it's because
many problems that would have required such heavy orchestration work became
natural and obvious. That came after more than 10 years of studying
programming and computer science. That's the real importance of never
stopping learning.

# And what is Rust's method

The goal of studying Rust, above all, is tied to returning to compiled
languages. After 15 years writing a lot of code and delivering at high volume,
I realized I had grown comfortable not only with frameworks, but also with debugging
conveniences and with not thinking about how to extract maximum efficiency. So I started
looking at all the compiled languages I could study. Among them, I noticed
there was one language that would only remind me how laborious it is to program
without a virtual machine cleaning up after you. Another language that gave
total control to the point of being paranoid.
And, finally, a language that would do what seemed impossible: have the experience of
a garbage collector without the overhead of a virtual machine. There's no free lunch,
so I thought I would have to apply programming concepts that no other
language forced me to implement. That was the point that
made me settle on Rust.

Obviously you can see that choosing Rust wasn't a choice in a vacuum,
as if there were nothing relevant beyond a "match" upon seeing the
language. On the other hand, I didn't want to study C/C++. Not out of rejection, but
because I felt I needed to connect with something more modern, without diminishing the
relevance it has and will continue to have. At that moment, my world revolved around
the web and languages that allowed high productivity. Rust is
a younger language, with goals similar to those of C/C++.

# Conclusion

As they say, "balance is a little poison and a little salad": the
choice of Rust was for the language's purpose and its quality. On the other hand,
it was also the modernization and design of the language—and all the hype built around
it—that led me to appreciate its coding style. As said before,
the problem is never personal preferences; the problem is when they happen
without foundation.
