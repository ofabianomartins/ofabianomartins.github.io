+++
title = "You Chose It Because You Wanted To! The Drama of Choosing Programming Languages"
slug = "the-drama-of-choosing-programming-languages"
date = "2026-04-18"
+++

Companies don't choose programming languages the same way.
If you've ever worked at a small software company — and by "small," I mean a company that lacks the governance to customize its own development stack — the discussion of which language to use for the next project is always on the table.
The "factions" will defend their preferred language, and this can be a healthy discussion or a real clash!
The real problem is never in that debate itself, but rather in what lies behind it and what truly matters when selecting a programming language.

# A Mature Company

When we use governance as a parameter for a company's size, we mean that the important thing is to have stability in the product's language, allowing for a communication base across all projects and teams.
This is difficult to achieve and shouldn't be perfect, since no one is going to use a web language for embedded device development—and if someone says otherwise, you should question either the depth of your interlocutor's knowledge or whether you understood what they were saying.

The important thing isn't that everyone uses the exact same stack or the same development framework.
The main workflows should allow teams to be changed and recombined according to the company's resource allocation needs.
Relying on a developer's individual ability to switch between projects should be considered, but the reality of the group must be taken into account.

This is because the main differentiator between a senior and a junior professional within a company is the knowledge gained through work experience that makes them capable of solving problems within the organizational structure.
In other words, knowing where to make changes to solve a problem is more important than being a theorist of a language or framework.
Consequently, the more diversified the stack and architecture decisions are, the more dependent we become on key individuals who have mastered those specific areas of knowledge.

# The Performance vs. Delivery Dilemma

When I teach programming, the first topic is the Von Neumann model, to understand how the relationship works between what you are writing and a decent abstraction of the machine where you execute that system.
However, presenting content doesn't guarantee that people will absorb it.
So, for beginners, a demanding language like C is complicated and inefficient for producing results.
There are languages that are much less demanding in terms of syntax and memory mechanism abstraction.
However, this openness to results comes at a cost for a language that must handle the details the developer cannot.
Yet, this ease of use increases the delivery capacity of more experienced developers.

Thus, adopting high-level languages makes it possible for beginners to produce results and makes experienced developers much more productive because they don't have to deal with details that shouldn't be necessary for the final outcome.
But someone has to do it!
So, it's done by the Virtual Machine where the language runs, applying the Garbage Collector to free up memory space that the programmer will no longer use.

This Virtual Machine and the garbage collector are the prices paid for ease and volume of delivery.
In a system where you need to deliver a high volume of features but have few users, this price is very cheap because the goal is actually to handle various processes that aren't execution-critical.
In the case of a system with a high volume of requests, this will become a problem that needs optimization.
Switching languages is not an immediate necessity; however, there will certainly be a refactoring needed to handle the increase in request volume.

# How We Individually Select Our Programming Language

Developmental psychology teaches us that the first trigger for a person to join the social pact is belonging to a group.
In other words: if you don't know much, what's the best way to be accepted?
Repeat the behavior of those who seem the most socially accepted and who fit within your aptitudes.
This ends up being the easiest way to understand why certain languages are widely adopted.
Understanding that we will inherently join majority groups, or at least groups strong enough to protect us, is simply human nature.

Our actions will generally be driven by our personal inclinations, even if we have good excuses.
A person with a risk appetite will always view risky choices as necessary when it's purely a search for adrenaline; a person very attached to routine will be induced toward what they are used to, claiming it's better because it works for them.
This isn't a problem; the problem is not being aware of these inclinations.

I once worked with a guy who would come in every week with some big new thing we should apply because it was better and the market was demanding it.
In reality, he just followed hype and lived for chasing these trends.
He implemented a new company system in one of these hype languages, and when it came time to deliver, he couldn't get it to work.
He was "made available to the market" (let go).

The problem wasn't the language!
He had an inclination to be open to new things, and in his mind, delivering in the hype language was a relevant quality, but working is more important than that.
After he was let go, our manager told me something I've never forgotten: "I don't have a problem with new things, but you need to be able to back up your deliveries."
This is what defines whether your personal choice is fair or not—whether it can be supported by you and/or the team and generate results.
Without that, it makes no difference!

Once, talking to a respected consultant, I started a debate about which language would be the most interesting and competent.
He didn't blink and said Java!
His eyes filled with tears, and he began talking about Java's qualities and how the language has evolved with its versions and how it's been applied in the market.
This had nothing to do with the fact that he had a career of over 20 years with Java and a large portfolio of clients he maintained and rotated between.
That's not a problem!
The problem is knowing whether he will be able to adapt to changing scenarios.
In what he already masters, however, he is fully capable.

I was forged in a technical course that started with Object Pascal, continued with Java, and where I learned PHP.
I had never seen Ruby before finishing the technical course and getting my first junior job in Ruby 1.9.8.
Basically, I've only worked in that stack, adding JavaScript and Python in some test projects.
But what paid my bills for the last 10 years was Ruby on Rails, and it's no surprise that the last time I started a project from scratch was in Ruby on Rails, which was where I felt comfortable developing!
That's not the problem!
The problem is that today I study Rust, and in the end, I'm trying to draw parallels between languages created with different goals and outcomes.

Finally, it's quite clear that having personal choices is not the problem.
The problem lies in the consequences of choices based on inclinations that you later cannot manage.
Explicitly personal choices are not a problem.
The problem is knowing how to measure the consequences of those choices!

# So, After All, Which Decision Should Be Made?

I don't know, but what I do know is that you must always pay attention to three trends when evaluating a development team's decision!

1. The personal bias of whoever makes the final call.
2. The team's bias and their available technical resources.
3. The technical requirements of the business.

The order is from top to bottom.
However, the higher the number of users, the more the order reverses.
Starting with projects with few users, the individual choice of the decision-maker will always prevail.
If the team's needs are relevant enough, the decision might lean toward the team, but the manager will choose what seems most comfortable to them.
And since, in most cases of small software, it makes no difference, any language used with common sense will solve the problem.

The order reverses when infrastructure starts breaking cost limits.
When the volume of bug notifications due to downtime increases.
This makes the team more stressed, having to work overtime to deal with downtime.
And especially when these problems reflect in a loss of conversion rates and customer consumption.
At this point, the decision-making manager just wants the problem solved and the crisis stabilized.
So, the decision will be biased, but what biases it most is the practical result.

And now that the primary focus was the system's needs, you might think that yes, a correct decision was made and this is the right way to make decisions!
And that's not true!
What happened was that the main driver was the need for results and system stabilization, but this passed through the filter of what the team was capable of delivering and what the decision-maker was willing to do.
Biases still exist, but the real problem took precedence.
And even with the real problem being the pivot for change, it's possible the choice is poor due to the team's limitations.

So, is there no such thing as a correct decision?!
Exactly—what exists are decisions that solve today's problems.
And were you able to make a decision that generated gains over time, or was it just a decision biased by circumstances?
The important thing isn't to make the best decision; it's to make a decision that doesn't become a debt later on that you can't pay.
That is the most important point.

# But With AI, All This Is Going to Change!

I'm not so sure.
What AI has done is turn all software developers into banana sellers.
This means their product, which used to be expensive, and the competitive advantage they had due to their skills, has diminished.
There have always been banana sellers, and they paid their bills and supported their families.
Even though today you have better ways to store, transfer, and allocate, intermediaries are still needed to take risks and assume responsibilities.
AI will not make decisions!
It may be able to assist by providing probabilities and helping improve decisions, but it will not be the decision-maker.
It is not an entity capable of taking risks.
And the day it is, programming languages won't be your biggest problem.

# Conclusion

The goal was to show that the decision of which programming language to use is far from purely technical, and that the fact that it isn't purely technical isn't a problem.
What matters is whether the consequences of the chosen decision can be sustained by the development team and, if circumstances change, whether the course can be adjusted.
In short, deciding on a programming language is never a simple task if you're building something that matters.
