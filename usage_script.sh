#!/bin/bash
## run while loop to display date and hostname on screen ##
while [ : ]
do
    	clear
    	tput cup 5 5
    	date
    	tput cup 6 5
    	echo "Hostname : $(hostname)"
    	echo ""
	echo "System Temperatures"
	sensors
	echo "GPU Details"
	nvidia-smi
	sleep 5
	


done
