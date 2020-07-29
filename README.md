# Mobile VR BOT
Goal of this bot is to establish a teleprescense in unacessable areas where a normal human can not go, but a small 

## Working
### The working if the bot has been divided into 3 parts
* ### 1. VR Stream
    - Here we were able to achieve a very low latency video stream in vr format to our phone from the bot's camera with a 480p resolution using WebRTC technology, this was achieved  by the UV4L Server from Linux Projects.
    - As for the VR format a custom frontend website that takes the streaming video and shows it in a VR format 
    - The VR stream can be viewed by any phone on the same network by going to the hosted website by the Rpi (Rpi_IP_adress:8080/)
    - The VR experience was achieved using a vr box and a phone as the display
* ### 2. Camera Control
    - The camera has 2 axis of freedom (ie X and Y axis) which was achieved by connecting the camera to a custom stand which is connected to 2 Servo motors
    - The camera moves according to your head movements which is detected by your smartphone's Gyroscope and Accelerometers Data.
    - The live streaming of the sensors data was achieved by using an app called WirelessIMU which connects to the custom port hosted by the Rpi in the network
    - The wireless IMU app works on a socket port connection with the Raspberry pi with Socket script written in python
    - Once the data is recieved in the Raspberry Pi to the program will calculate the servo angle from the data of the previous angles
    - Once the angle is calculated the Raspberry pi will move the servo to the specified angle by sending a PWM signal from the GPIO pins
* ### 3. Movement of the bot
    - The bot has a 4 wheel drive system where the bot is controlled 
