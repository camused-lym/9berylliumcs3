## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)


## Design Revision
Describe any changes made to your original class.
Added a new private property, "id"


## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Artist| STR| PUBLIC| Artist has to be visible for their own benefit.|
| Views| INT| PUBLIC| We need to measure popularity somehow.|
| Length| INT| PUBLIC| To show if the song is about to end.|
| Platforms| STR| PUBLIC| To show if the song is available on different platforms.|
|  ID|  INT|  PRIVATE|  Hidden due to protect it from outside variables.|


## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)


## Python Implementation
[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private? Because the ID needs to be permanent and other parts of public code may change the song ID
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
