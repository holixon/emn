---
template: adr.html
title: Element Value Specification Approach
status: accepted
date: 2025-01-01
deciders: Simon Zambrovski, Christian Thiel, Jan Galinski
---

# Element Value Specification Approach

## Context and Problem Statement

Event Modeling Notation (EMN) requires a standardized approach for specifying values of elements within the notation. Following the schema approach established in [ADR-0005](0005-schema-approach-for-message-structures.md), we need to define how actual values should be represented, whether they are embedded directly or referenced externally.

Key considerations include:
- How values should be formatted and structured
- How to handle partial values that don't need to specify all mandatory fields defined in a schema
- How default values and examples can be defined in schemas
- How to maintain consistency with the extensibility principles of EMN

## Considered Options

* Define values only in the native XML format
* Support multiple value formats (JSON, XML) with format specification
* Support only embedded values
* Support both embedded and referenced values
* Require exhaustive values (all schema-defined fields must be provided)
* Allow non-exhaustive values (only relevant fields need to be provided)

## Decision Outcome

Chosen option: "Support multiple value formats with both embedded and referenced values, allowing non-exhaustive specification", because:

* It provides maximum flexibility for users to express values in their preferred format
* It maintains consistency with the schema approach defined in [ADR-0005](0005-schema-approach-for-message-structures.md)
* It allows for partial specification of values, focusing only on the relevant fields
* It enables the definition of defaults and examples in schemas that can be overridden by specific values
* It supports both simple use cases and complex scenarios with external value references

## Detailed Explanation

### Value Format Specification

Values in EMN elements can be specified in multiple formats, with the following approach:

1. A `valueFormat` attribute will indicate the format of the value (e.g., "json", "xml")
2. The value itself can be either:
   - Embedded directly within the element
   - Referenced via a URI to an external resource

This approach allows for flexibility while maintaining clear semantics about how the value should be interpreted.

### Value Structure

The value structure follows these principles:

1. **Format Consistency**: The value must conform to the specified `valueFormat`
2. **Non-Exhaustive Specification**: Values do not need to include all fields defined as mandatory in the schema
3. **Override Mechanism**: Values provided will override defaults defined in the schema
4. **Validation Context**: When validating a complete model, the combination of schema defaults and provided values should satisfy all schema constraints

### Embedded Values

Embedded values are included directly within the EMN document:

```xml
<message id="orderPlaced">
  <schema format="json-schema" src="schemas/order.json"/>
  <value valueFormat="json">
    {
      "orderId": "123",
      "customer": {
        "id": "456"
      }
    }
  </value>
</message>
```

### Referenced Values

Referenced values are linked from external resources:

```xml
<message id="orderPlaced">
  <schema format="json-schema" src="schemas/order.json"/>
  <value valueFormat="json" src="values/sample-order.json"/>
</message>
```

### Default Values and Examples

Schemas can define default values and examples that are used when specific values are not provided:

1. **Default Values**: Defined in the schema and used when a field is not specified in the value
2. **Examples**: Provided in the schema to illustrate valid values but not used as defaults
3. **Override Precedence**: Explicitly provided values take precedence over defaults

For JSON Schema, this leverages the existing `default` and `examples` keywords:

```json
{
  "type": "object",
  "properties": {
    "orderId": {
      "type": "string",
      "default": "new-order"
    },
    "customer": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "type": {
          "type": "string",
          "default": "retail",
          "examples": ["retail", "wholesale", "partner"]
        }
      }
    }
  }
}
```

For XML Schema, default values can be specified using the `default` attribute:

```xml
<xs:element name="orderId" type="xs:string" default="new-order"/>
```

### Non-Exhaustive Value Specification

Values in EMN do not need to specify all fields defined in the schema, even those marked as mandatory. This approach:

1. Allows focusing only on the relevant fields for a particular context
2. Reduces redundancy in value specifications
3. Leverages defaults defined in the schema
4. Enables partial overrides of complex structures

When processing an EMN document, the effective value is determined by:
1. Starting with all default values defined in the schema
2. Overriding with any explicitly provided values
3. Validating the resulting complete value against schema constraints only when required for execution or simulation

### Implementation Considerations

1. **Validation Timing**: Full validation against schemas should be optional and performed only when explicitly requested or when executing/simulating the model
2. **Format Support**: Implementations should support at least JSON and XML formats
3. **Default Handling**: Tools should clearly indicate which values come from defaults versus explicit specifications
4. **Visualization**: EMN editors may choose to display the effective value (including defaults) or only the explicitly provided values

## Benefits of this Approach

1. **Flexibility**: Users can choose the value format that best fits their specific needs and existing technology stack
2. **Conciseness**: Values can focus only on what's relevant in a particular context
3. **Reusability**: Default values and examples in schemas reduce redundancy across multiple value specifications
4. **Interoperability**: Support for multiple formats ensures compatibility with various tools and systems
5. **Consistency**: Alignment with the schema approach from [ADR-0005](0005-schema-approach-for-message-structures.md) provides a coherent overall specification

By supporting multiple value formats with both embedded and referenced values, and allowing non-exhaustive specification, EMN provides a flexible yet structured approach to element value specification that accommodates a wide range of use cases while maintaining clarity and consistency.
