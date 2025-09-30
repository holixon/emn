---
title: Usage and Tools
---

EMN can be applied using a variety of tools.
Initially, the language is designed to be supported in diagramming environments that implement the OMG DI standard.
Over time, editors, converters, and validators will make it easier to integrate EMN into modeling workflows.
Tools may include standalone diagramming software, IDE plugins, or integrations with documentation frameworks.
Adoption of EMN aims to improve collaboration, model consistency, and system documentation.
This page highlights both current tools and the roadmap for wider adoption.

## Editors

### EMN-JS

EMN JS is a web-based modeler based on famous diagram-js framework that is currently being developed. In the current 
development stage it already support creation of EMN JS diagrams including the full support of the language specification.


## Code Generation

### EMN-Kotlin-Axon

Currently in the early development, a Code Generator creating system implementation based on Spring Boot, 
Axon Framework 5 and Kotlin. Heavily based on definition of structures in Apache Avro specifications it aims to
be packaged as a Apache Maven build-plugin, that runs generation during the build of your software continuously
and handles `.emn` files as part of the solution.
