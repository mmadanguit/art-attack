---
title: 'Sprint 1'
description: Starting up and setting out. 
image: '../../images/textile.jpeg'
---

# Project Goals
Our team came together with a desire to see more art at Olin and create something cool and creative. **This gave rise to our overarching project goal, which was to create a large-scale, impactful installation that has a well integrated system capable of generating engaging patterns of movement.** We wanted to create something that could excite and last within the Olin community, and found inspiration in sculptures that change and respond to the presence of a person. 

![](/images/sprint1/inspiration.jpeg)
*Rozin, Daniel. Wooden Mirror (2014).*

We were interested in creating a piece that would prompt members of the Olin community to pause-- to take a moment out of their busy day to acknowledge and appreciate the space around them and how they might fit into it. 

Early on, we had a conversation about whether we wanted to prioritize scale or precision in our final piece, knowing that we could not have both due to our limited budget. We ultimately chose to prioritize scale because we believed it would be the most impactful and we were more excited by the idea of abstracting a person’s presence rather than replicating it (in the form of a mechanical mirror of some sort). **This conversation informed our MVP which was a 1x1 meter sculpture consisting of a set of motors attached to a textile surface that moves based on how far a person is standing from it.** 

# Team Structure
Alongside these conversations about the art, we were discussing our personal learning goals and dividing ourselves into sub teams based on our technical interests. Jen took on the role of the PM, Elisa and Jen took on the mechanical components, Luke and Jen took on the firmware and electrical components, and Marion and Anna took on the software components.

# Sprint 1 Outcomes
For our first sprint, we worked on brainstorming and prototyping each component of the system so that we could focus our second and third sprints on replication and expansion. 

## Mechanical
Our mechanical team created a working scotch yoke system and prototyped three textile materials for the display, as shown in the figures below. 

![](/images/sprint1/scotch-yoke-2.png)

| | | | 
|-|-|-|
| ![](/images/sprint1/textile-1.gif) | ![](/images/sprint1/textile-2.gif) | ![](/images/sprint1/textile-3.gif) |


## Electrical
Our electrical team explored options for motors and power sources that would allow us to scale our design and found that we could purchase 50 servos with our budget.  

## Firmware
The firmware team wrote a program to move a servo motor and also set up serial communication between Arduino and Python. 

## Software
The software team wrote a program to determine the distance from the computer camera to the face using OpenCV, as shown in the figures below. They found that the program does not work well with masks on and planned to look into whole body recognition algorithms in the next sprint. 

| | | 
|-|-|
| ![](/images/sprint1/detection-1.gif) | ![](/images/sprint1/detection-2.gif) |