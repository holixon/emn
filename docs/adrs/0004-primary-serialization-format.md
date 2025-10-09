---
template: adr.html
title: Primary Serialization Format for EMN Documents
status: accepted
date: 2025-01-01
deciders: Simon Zambrovski, Christian Thiel
---

# Primary Serialization Format for EMN Documents

## Context and Problem Statement

Event Modeling Notation (EMN) requires a standardized serialization format for storing and exchanging EMN documents. This format will serve as the foundation for tool interoperability, model persistence, and exchange between different EMN tools and platforms.

The choice of serialization format impacts several critical aspects of the EMN ecosystem:
- How easily EMN documents can be extended with vendor-specific elements
- How effectively EMN documents can be validated against schemas
- How widely the format will be adopted and supported by tools
- How easily developers can work with the format

## Considered Options

* JSON (JavaScript Object Notation)
* YAML (YAML Ain't Markup Language)
* XML (Extensible Markup Language)

## Decision Outcome

Chosen option: "XML (Extensible Markup Language)", because:

* XML provides the strongest support for extensibility through namespaces, which allows collision-free addition of vendor-specific elements
* XML has mature validation capabilities through XML Schema (XSD), Schematron, and other technologies
* XML is already the serialization format used by BPMN 2.x, which aligns with our decision to follow BPMN's specification style (see [ADR-0003](0003-align-specification-style-with-bpmn.md))
* XML's mature tooling ecosystem in enterprise environments ensures broad compatibility with existing systems
* XML's strict parsing rules help ensure document consistency across different implementations

## Comparison of Options

### Extensibility

1. **XML**:
   * Provides namespaces that allow for collision-free extension of documents
   * Supports mixed content models where text and elements can be intermixed
   * Allows for vendor-specific extensions that won't conflict with core elements
   * Enables clear separation between standard EMN elements and custom extensions
   * Supports processing instructions and other extension mechanisms

2. **JSON**:
   * Lacks native namespace support, making collision-free extensions more difficult
   * Extensions typically rely on naming conventions (e.g., prefixes) which are not enforced
   * Requires custom extension patterns that may not be consistently implemented
   * More compact but less expressive for complex hierarchical structures

3. **YAML**:
   * Similar extensibility limitations as JSON
   * Offers tags for type information but lacks a standardized namespace mechanism
   * More human-readable but shares JSON's extension challenges
   * Anchor and alias features can create more complex references but don't solve the namespace issue

### Validation

1. **XML**:
   * Robust validation through XML Schema (XSD) with strong typing and constraints
   * Additional validation through Schematron for complex business rules
   * Validation can be applied even when extensions are present
   * Well-established validation patterns from BPMN and other XML-based standards
   * Validation errors provide precise location information

2. **JSON**:
   * JSON Schema provides validation but is less mature than XML Schema
   * Validation tooling is improving but still not as comprehensive as XML
   * Less capable of validating documents with extensions
   * Simpler validation model that may not capture all EMN constraints

3. **YAML**:
   * Can use JSON Schema for validation with some adaptations
   * Validation is complicated by YAML's more complex features (anchors, aliases)
   * Less standardized validation approach compared to XML
   * Fewer enterprise-grade validation tools

### Adoption and Tool Support

1. **XML**:
   * Widespread enterprise adoption and mature tooling
   * Strong support in all major programming languages
   * Established patterns for model interchange from BPMN, UML, and other standards
   * Consistent parsing behavior across implementations
   * More verbose but well-understood by enterprise developers

2. **JSON**:
   * Excellent support in web and JavaScript environments
   * Simpler parsing model with broad language support
   * More compact representation
   * Popular in REST APIs and modern web applications
   * Less established for complex modeling languages

3. **YAML**:
   * Good human readability for configuration files
   * Growing adoption in configuration management
   * Inconsistent parsing across implementations
   * Complex specification with potential security concerns
   * Less suitable for interchange formats requiring strict consistency

## Alignment with BPMN 2.x

As established in [ADR-0003](0003-align-specification-style-with-bpmn.md), EMN is aligning its specification style with BPMN 2.x. BPMN 2.x uses XML as its 
serialization format, with a clear separation between:

1. The semantic model (what elements mean)
2. The diagram interchange (how elements are visualized)

By adopting XML as our primary serialization format, we maintain consistency with this approach and can leverage established patterns from BPMN 2.x, including:

* Namespace management for extensions
* Separation of semantic and visual concerns
* Schema validation approaches
* Tool interoperability mechanisms

## Implementation Considerations

While XML will be the primary serialization format for EMN documents, tools may provide alternative formats for specific use cases:

* JSON representations may be useful for web-based EMN editors
* YAML might be appropriate for human-editable configuration aspects
* Custom binary formats might be developed for performance-critical applications

However, XML will remain the canonical interchange format for EMN documents, ensuring consistent interpretation across the EMN ecosystem.

## Benefits of XML for EMN

1. **Standardized Extension Mechanism**: XML namespaces provide a clean, collision-free way to extend EMN documents with vendor-specific elements.

2. **Robust Validation**: XML Schema and related technologies enable comprehensive validation of EMN documents, ensuring consistency and correctness.

3. **Enterprise Compatibility**: XML's widespread adoption in enterprise environments ensures EMN can integrate with existing systems and tools.

4. **Alignment with BPMN**: Using XML maintains consistency with BPMN 2.x, leveraging established patterns and reducing the learning curve.

5. **Future-Proofing**: XML's mature specification and stable implementation across platforms provides a solid foundation for long-term EMN development.

By selecting XML as the primary serialization format for EMN documents, we establish a foundation that balances extensibility, validation capabilities, and industry adoption, while maintaining alignment with our decision to follow BPMN's specification approach.
