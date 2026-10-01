# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
A music streaming platform managing track attributes, statistics, lyrics, and website integration.
## Inheritance Relationship
Parent: AudioTrack
Child: Song
Explanation: Song is a type of AudioTrack that shares core properties like artist, views, length, platforms, and ID.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Composition
Explanation: The song creates its own lyrics object internally, meaning the lyrics cannot exist independently if the song is removed.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
I chose Song as a child class of AudioTrack because a song is a type of audio track that shares universal properties like artist, views, length, platforms, and ID.

2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
Inheritance removed the need to rewrite attributes like artist, views, length, platforms, and ID, along with the display_info method, by using super().__init__() to reuse parent code.

3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
My relationship is Composition because the lyrics are instantiated directly within the song and are tied completely to the lifespan of that song object.

4. What is the difference between Association from Part III and the advanced relationship you implemented?
Association links independent classes loosely, whereas advanced relationships like inheritance establish an IS-A hierarchy and composition enforces strict whole-part ownership.

5. How does your design follow the DRY principle?
My design follows the DRY principle by moving shared attributes into a single parent class instead of duplicating the same data fields across multiple files.
