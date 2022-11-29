# docker-monitor
This Python application utilizes the **docker-py** library to implement basic functions equivalent to common Docker CLI commands such as:
- monitoring that a given container is running  
- keep such container running if its status is not equal to running 

Program stops executing by manual intervention only, otherwise it will continue to run.


## Implementation 
This script bootstraps an Ubuntu-based CLI bash window and keeps it open in its Docker image.

- If the script finds any Docker containers in running state in the local system, they will be stopped before running the intended Ubuntu **/bin/bash** container.
- If this Ubuntu container gets killed by user, the script will bootstrap a brand new one.
- If this Ubuntu container gets paused by user, the script will unpause and resume its execution.
