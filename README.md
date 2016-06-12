#SHoW
This is a simple hot wire game made with the Raspberry Pi, used as a game for the "after defense" of a collegue.
For the development I used the RP2, but I guess it will be compatible with the models b+ as well. An important issue is that the RPi needs a very stable power source, otherwise it will fail apically (the time and detection of contact gets crazy).

The configuration can be found in the Main file. 
* if TEST is set true, it will show an extra panel to debug the program in order to simulate the touchs of ht users.
* PRI: defines if the game is used with the Raspberry Pi. If true, you can play with it.
* PUNISHMENT: defines the penalty in seconds that will be applied to the player
* TIME : defines the "safe time" after a touch during what other contacts will not be counted
* INPUTS and CTRLSP define the signal input for the players and end of the track.


```python
TEST = False
PRI = True  # defines if it is being used with the Raspberry pi or not

PUNISHMENT = 1
TIME = 0.5  # delay in seconds
INPUTS = [27, 17]
CTRLSP = [22, 10]
```

## hardware
* The wire itself needs to be conductive otherwise the game will not work (Physics 101).
* connect the track of every player to the input pins defined in INPUTS in order to be able to detect the contacts.
* At the end of the track using isolating tape and your imagination, connect a cable to the CTRLSP of each player.

The idea is that at the end of the race, wins the player with "less points" where the points are the number of seconds required for the race + the number of times that the player contacted the wire. For instance:  
* P1 = 25 segs required for the race and touched the wire 5 times,  
* P2 = 21 segs required for the race and touched the wire 10 times,  

finally    
P1 = 25+5  
p2 = 21+10  

and the winer is P1. The cryteria is to be fast an precise.
