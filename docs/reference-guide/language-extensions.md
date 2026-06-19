---
title: Language Extensions
---

## Extensions

Extensions provide optional namespaces for information that enriches an EMN model without changing the core EMN language.
Extension elements are placed inside `emn:extensionElements` and are identified by their own XML namespace.
Tools that do not support a specific extension may preserve the extension data without interpreting it.

### Information Completeness Check

The information completeness check extension documents known and accepted gaps in the information passed along an information flow.
It is useful when validating whether the target of a flow receives all required information from the source, while still allowing
modelers to mark selected properties as intentionally ignored.
The check is valid for any `emn:FlowElementType`, including `emn:informationFlowType` and concrete flow node type elements.

#### Namespace

Documents using this extension declare the `emnic` namespace:

```xml
xmlns:emnic="https://holixon.io/spec/EMN/20241231/IC"
```

They may also include the optional schema location for XML validation:

```xml
xsi:schemaLocation="https://holixon.io/spec/EMN/20241231/MODEL EMN.xsd
                    https://holixon.io/spec/EMN/20241231/IC EMNIC.xsd"
```

#### Structure

The extension root element is `emnic:informationCompleteness`. It can contain an optional
`emnic:ignoredProperties` element with zero or more `emnic:ignoredProperty` entries.
The following example shows the extension on an `emn:informationFlowType`.

```xml

<emn:informationFlowType
  id="informationFlowType_1"
  sourceRef="commandType_register_customer"
  targetRef="eventType_customer_registered">
  <emn:extensionElements>
    <emnic:informationCompleteness>
      <emnic:ignoredProperties>
        <emnic:ignoredProperty name="name" comment="Not required by the target"/>
        <emnic:ignoredProperty name="schema" comment="Schema is checked elsewhere"/>
      </emnic:ignoredProperties>
    </emnic:informationCompleteness>
  </emn:extensionElements>
</emn:informationFlowType>
```

#### Semantics

- `emnic:informationCompleteness` defines completeness-check metadata for one EMN flow element type.
- `emnic:ignoredProperties` groups properties that are excluded from the completeness check.
- `emnic:ignoredProperty` identifies one ignored property by name and may explain the reason in `comment`.
- The extension is only valid inside `emn:extensionElements` on elements derived from `emn:FlowElementType`.

#### Attributes of `emnic:ignoredProperty`

| Attribute | Type         | Use      | Description                                      |
|-----------|--------------|----------|--------------------------------------------------|
| `name`    | `xsd:string` | required | Name of the property ignored by the check.       |
| `comment` | `xsd:string` | optional | Reason or note explaining why it is ignored.     |
