---
template: adr.html
title: Align Specification Style with BPMN
status: accepted
date: 2025-01-01
deciders: Simon Zambrovski, Christian Thiel
---

# Align Specification Style with BPMN

## Context and Problem Statement

Event Modeling Notation (EMN) is a language specification for Event Modeling, a collaborative method for requirement engineering and solution development 
of event-driven systems. As we develop EMN, we need to decide on the style and approach for our specification. Should we align our specification style 
with established standards like BPMN (Business Process Model and Notation), or develop a completely unique approach?

This decision impacts the learnability, adoption, and interoperability of EMN with existing tools and methodologies.

## Considered Options

* Align EMN specification style with BPMN 2.x, focusing on semantics
* Develop a completely unique specification style for EMN
* Adopt specification styles from other modeling languages (UML, ArchiMate, etc.)
* Create a hybrid approach combining elements from multiple specification styles

## Decision Outcome

Chosen option: "Align EMN specification style with BPMN 2.x, focusing on semantics", because:

* We see similarities between the development of Event Modeling and Process Modeling
* Process Modeling initially used a diagram-only, non-interchangeable BPMN 1.0 that limited Business-IT alignment and tool support
* The development of BPMN 2.x enabled tool interchange and helped BPMN become an industry standard
* EMN can follow a similar evolution path, learning from BPMN's successful transition
* Using familiar patterns from BPMN reduces the learning curve for practitioners already familiar with process modeling
* The semantic approach of BPMN 2.x provides a solid foundation for expressing complex event flows and interactions
* Following OMG's approach to language specification creates a more robust specification with clear semantics

## Parallels Between Event Modeling and BPMN Evolution

### Historical Parallels

1. **From Diagram to Interchange Format**: Just as BPMN evolved from a diagram-only notation (BPMN 1.0) to a complete language with interchange format (BPMN 2.x), EMN aims to evolve Event Modeling from a visual technique to a formal, interchangeable specification.

2. **Business-IT Alignment**: BPMN 2.x bridged the gap between business and IT by providing a common language. EMN seeks to achieve the same for event-driven systems.

3. **Tool Support Evolution**: BPMN's widespread adoption was accelerated by the tool interoperability enabled by BPMN 2.x. EMN aims to enable similar tool ecosystem development.

### Semantic Alignment with BPMN 2.x

1. **Flow-Based Modeling**: Both EMN and BPMN 2.x use a flow-based approach to model processes and interactions. EMN's timeline with message flows parallels BPMN's sequence flows.

2. **Event-Centric Approach**: While BPMN includes events as one element type, EMN elevates events to a central role, which aligns with BPMN's event handling capabilities.

3. **Containment Hierarchy**: EMN adopts a similar containment hierarchy to BPMN 2.x, with definitions as the root container organizing all model elements.

4. **Message Flows**: Both notations use message flows to represent communication between elements, though EMN expands on this concept for event-driven systems.

5. **Lanes and Pools**: EMN's lane concept (trigger lanes, interaction lanes, aggregate lanes) parallels BPMN's swimlanes, though adapted for event modeling's specific needs.

6. **Element Types and Instances**: Both notations distinguish between element types (definitions) and their instances in actual models.

7. **Extensibility**: Both specifications are designed with extensibility in mind, allowing for future growth and adaptation.

8. **XML-Based Serialization**: EMN adopts BPMN 2.x's approach of using XML as the serialization format for models, enabling tool interoperability.

### Diagram Interchange Approach

EMN adopts ideas from OMG's Diagram Definition (DD) specification, particularly:

1. **Diagram Interchange (DI)**: EMN will separate the semantic model from its visual representation, allowing multiple visualizations of the same model.

2. **Diagram Context (DC)**: EMN will use concepts from DC to define how diagram elements relate to semantic elements.

3. **Separation of Concerns**: This approach clearly separates the semantic model (what things mean) from the diagram model (how things look), while maintaining the connections between them.

### Semantic Differences and Enhancements

1. **Timeline Focus**: EMN introduces a stronger temporal dimension through its timeline concept, which is implicit but not as central in BPMN.

2. **Specifications**: EMN adds behavior specifications using Given-When-Then patterns, which extends beyond BPMN's process flow to include expected outcomes.

3. **Slices**: EMN's slice concept provides vertical grouping across lanes, which is a unique enhancement not present in BPMN.

4. **Command-Event Distinction**: EMN explicitly models commands and events separately, reflecting the CQRS/ES architectural patterns, which BPMN doesn't specifically address.

5. **Aggregate Concept**: EMN introduces the concept of aggregates from Domain-Driven Design, providing a stronger connection to implementation patterns.

## Benefits of Alignment with BPMN 2.x

1. **Industry Standard Approach**: Following the proven path of BPMN 2.x provides a solid foundation for EMN's development and adoption.

2. **Tool Interoperability**: By adopting BPMN 2.x's approach to model interchange, EMN enables the development of interoperable tools.

3. **Familiar Mental Model**: Practitioners familiar with BPMN can more easily understand EMN's approach to modeling.

4. **Clear Separation of Semantics and Visualization**: Using OMG's DD approach allows EMN to clearly separate semantic meaning from visual representation.

5. **Business-IT Alignment**: Like BPMN 2.x, EMN bridges the gap between business stakeholders and technical implementers.

6. **Ecosystem Development**: A standardized interchange format facilitates the development of a tool ecosystem around EMN.

By aligning EMN's specification style with BPMN 2.x and adopting OMG's Diagram Definition approach, we create a language that builds on established patterns while addressing the specific needs of event modeling. This approach provides the best balance between innovation and familiarity, maximizing EMN's potential for adoption and effectiveness.
