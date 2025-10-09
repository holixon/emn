---
template: adr.html
title: Schema Approach for Message Structures
status: accepted
date: 2025-01-01
deciders: Simon Zambrovski, Christian Thiel, Jan Galinski
---

# Schema Approach for Message Structures

## Context and Problem Statement

Event Modeling Notation (EMN) requires a way to define the structure of messages exchanged between components in an event-driven system. These message structures need to be clearly defined to ensure proper communication and interoperability between different parts of a system.

There are two main approaches to handling message structure definitions:
- Creating a custom type definition language specific to EMN
- Supporting existing schema formats through embedded or external schema references

The choice impacts how developers define message structures, the flexibility of the notation, and its compatibility with existing tools and standards.

## Considered Options

* Create a custom EMN type definition language
* Support embedded or external schema elements via resource references
* Use a specific schema format (e.g., JSON Schema only)
* Omit type definitions entirely from the specification

## Decision Outcome

Chosen option: "Support embedded or external schema elements via resource references", because:

* It provides maximum flexibility for users to choose the schema format that best fits their needs
* It avoids reinventing existing schema definition languages that are already well-established
* It allows EMN to remain schema-format-agnostic while still supporting strong typing
* It enables integration with existing tools and standards for various schema formats
* It future-proofs EMN against changes in schema technology preferences

## Detailed Explanation

### Why Not Create a Custom Type Definition Language

1. **Redundancy**: Many robust schema definition languages already exist (JSON Schema, XML Schema, Apache Avro, Protocol Buffers, etc.) that solve the problem of defining data structures.

2. **Adoption Barrier**: Creating a new language would require users to learn yet another schema definition syntax, increasing the learning curve.

3. **Tool Support**: Existing schema formats already have extensive tooling for validation, code generation, and documentation, which EMN can leverage.

4. **Maintenance Burden**: Developing and maintaining a custom type definition language would require significant ongoing effort that could be better directed elsewhere.

### Schema Element Approach

Instead of a custom type definition language, EMN will support a schema element that can be:

1. **Embedded**: Directly included within the EMN document
2. **Referenced**: Linked to an external resource via URI

The schema element will have:
- A `format` attribute that identifies the schema language being used (e.g., "json-schema", "avro", "xsd", etc.)
- Content that conforms to the specified schema format

This approach allows:
- Any schema format to be used, including JSON Schema, XML Schema, Apache Avro, Protocol Buffers, and others
- Multiple schemas to be defined within a single EMN document
- Reuse of existing schemas across multiple message definitions
- Validation of messages against their schema definitions using existing tools


### Implementation Considerations

1. **Schema Validation**: EMN tools should support validation of messages against their schema definitions, either directly or by delegating to appropriate schema validators.

2. **Schema Discovery**: EMN should provide mechanisms for discovering and retrieving external schema references.

3. **Schema Evolution**: The approach should accommodate schema evolution strategies appropriate to each schema format.

4. **Default Format**: While EMN will support multiple schema formats, implementations may choose to provide better support for certain formats based on their target audience.

## Benefits of the Schema Element Approach

1. **Flexibility**: Users can choose the schema format that best fits their specific needs and existing technology stack.

2. **Interoperability**: EMN can integrate with existing tools and standards for various schema formats.

3. **Future-Proofing**: As new schema formats emerge, they can be supported without changes to the EMN specification.

4. **Reduced Learning Curve**: Users can leverage their existing knowledge of schema formats rather than learning a new one.

5. **Ecosystem Integration**: EMN can participate in broader ecosystems around various schema formats rather than creating its own isolated ecosystem.

By supporting embedded or external schema elements rather than creating a custom type definition language, EMN provides maximum flexibility while avoiding unnecessary complexity, allowing users to leverage existing tools and knowledge for defining message structures.
