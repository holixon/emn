---
template: adr.html
title: Develop language specification before tooling 
status: accepted
date: 2025-01-01
deciders: Simon Zambrovski, Christian Thiel
# status: {proposed | rejected | accepted | deprecated | … | superseded by [ADR-0005](0005-example.md)}
# date: {YYYY-MM-DD when the decision was last updated}
# deciders: {list everyone involved in the decision}
# consulted: {list everyone whose opinions are sought (typically subject-matter experts); and with whom there is a two-way communication}
# informed: {list everyone who is kept up-to-date on progress; and with whom there is a one-way communication}
---

# Develop language specification before tooling

## Context and Problem Statement

Event Modeling Notation (EMN) is a language specification for Event Modeling, a collaborative method for requirement engineering and solution development 
of event-driven systems. As we develop EMN, we need to decide on our priorities: should we focus first on developing a comprehensive language specification, 
or should we prioritize building tools for editing EMN documents and generating code from them?

This decision impacts our development roadmap, resource allocation, and the overall adoption strategy for EMN.

## Considered Options

* Focus primarily on developing the EMN language specification to completion
* Prioritize building tools for editing EMN documents
* Prioritize developing code generation capabilities from EMN models
* Pursue language specification and tooling development in parallel

## Decision Outcome

Chosen option: "Focus primarily on developing the EMN language specification to completion", because:

* A well-defined, stable language specification provides the foundation upon which all tools must be built. Without it, tool development would be built on shifting ground.
* The language specification defines the semantics, syntax, and visualization rules that make EMN valuable as a modeling approach. These fundamentals must be 
  solidified before meaningful tooling can be created.
* A complete language specification enables community adoption and third-party tool development, creating a broader ecosystem than we could build alone.
* Premature focus on tooling could lead to tools that constrain the language rather than the language defining what tools should support.
* The language specification is the intellectual core of EMN that differentiates it from other modeling approaches. Its clarity and completeness are essential for adoption.
* Event modeling practitioners can already use the language with simple diagramming tools once the specification is clear, even without specialized tooling.
* Focusing on one priority (language specification) allows for more efficient use of limited resources and clearer communication about project status.
* A complete language specification provides a stable target for future tooling development, reducing rework and ensuring tools properly implement the language.

While focusing primarily on the language specification, we will build tools for prototyping the EMN specification, both for editing EMN documents and for code generation. 
This approach will yield several benefits:

* The specification will be validated in the context of actual tools for creation of EMN documents and code generation.
* The adoption of early prototypes in tools will allow us to identify missing pieces in the specification that might be overlooked in a purely theoretical approach.
* This practical validation will ensure that the specification remains grounded in real-world usability while maintaining its conceptual integrity.
* The iterative feedback between specification development and tool prototyping will strengthen the overall quality of the EMN language.
