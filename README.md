# Double Solitaire

# Description
What?

Double solitaire is just like the original solitaire, but played competetively. Two players will go head to head to complete their game of solitaire first. The player with the best completeion time wins. 

Why?

Ever wanted to destory your friends at solitaire? Well now you can.

How?

Both players are given the same game of solitaire to play. A timer will count how long it takes each player to complete their game. In the event that neither player finishes, whoever got the closest to finishing will win.

# Requirements
This program requires installation of ngrok and the Pygame module.

# Getting Started and Installation
- Choose the directory you would like to download to then type the following commands into your command line:
$ cd YOURDIRECTORY
$ git clone https://github.com/dominicks12/Double-Solitaire.git


- On one machine only, navigate to where you downloaded ngrok and run the following commands in command line:
$ ngrok tcp 12000

- Copy the port number on the line labeled 'forwarding' (leave ngrok running)
- Navigate to where you downloaded the git project
- Open the 'Solitaire' file and edit the 'serverPort' variable to equal the port number you just copied
- Save and exit

- Run the 'server' file (only on machine that is running ngrok)
- Run the 'playGame' file (person on other machine must also run their 'playGame' file)


# Deliverables

1. Double Solitaire frontend
2. Double Solitaire backend
3. Documentation
4. GUI

# Plan
* Week 1 (Oct 22nd - Oct 29th)  
- Design the GUI 

* Week 2 (Oct 29th - Nov 5th)   
- Implement the GUI 

* Week 3 (Nov 5th - Nov 12th)   
- Design the backend service 

* Week 4 (Nov 12th - Nov 19th)   
- Implement the backend service 

* Week 5 (Nov 19th - Nov 26th)   
- Design the frontend service
 
* Week 6 (Nov 26th - Dec 3rd)    
- Implement the frontend service   
- Bug Fixes   
- Finish Documentation 



# Team Members
* Dominic Amaral
* Victor Lemus

# Comments
1. Write more details on the deliverables. What features will be delivered on the Front end/Back end
2. Think about extension of the game. Maybe having more than 2 people play the same game at the same time
