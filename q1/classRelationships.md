# Class Relationships: Association and Multiplicity

## Previous Work

[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class

Class: EditorialWriting

Description: A writing category for journalism. It is the voice of a publication.

## New Related Class

Class: ColumnWriting

Description: Another writing category for journalism. It shows the opinions and personal experiences of the columnist. 

## Association

Relationship: EditorialWriting contains references for ColumnWriting. 

Explanation: 

## Multiplicity

Multiplicity: One-to-Many

Explanation: One editorial can serve as a reference for many columns and opinion articles. 

## UML Class Relationship Diagram

![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation

[View Python Source](classRelationships.py)

## Test Run

![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram

![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis

### What is the association between your two classes?

### What multiplicity did you choose and why?

### How did you implement the relationship in Python?

### Why did you store an object reference instead of copying its data?

### If your relationship uses many, why is a list appropriate?
