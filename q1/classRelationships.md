# Class Relationships: Association and Multiplicity

## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: Music Player
Description: Class where it plays an audio file with supporting variables. 

## New Related Class
Class: Music Website
Description: Website where it displays a list of songs with different functions.

## Association
Relationship: Website HAS A Music Player

Explanation:
The Music Website class maintains an association with the Music Player class because a website instance relies on a music player component to handle audio playback functionality. This represents a "has-a" relationship where the website delegates playback tasks to the player.

## Multiplicity
Multiplicity: 1
Explanation:
Each instance of a Music Website utilizes a single active Music Player instance to stream and control audio tracks for users.

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
The association is a compositional or aggregational "has-a" relationship where the Music Website owns or references a Music Player object to execute core playback features.

### What multiplicity did you choose and why?
I chose a 1-to-1 multiplicity because a single web platform interface coordinates one central music player engine to handle track actions.

### How did you implement the relationship in Python?
I implemented it by initializing a Music Player object inside the __init__ method of the Music Website class and storing it as an instance attribute (e.g., self.player = MusicPlayer()).

### Why did you store an object reference instead of copying its data?
Storing a reference ensures that the Music Website interacts with a live, single instance of the player, allowing methods like play() and pause() to modify and track the true playback state correctly without redundant data duplication.

### If your relationship uses many, why is a list appropriate?
A list is appropriate because it dynamically stores, orders, and allows easy iteration over multiple elements while keeping code flexible and scalable.
