# Mobile VR BOT
Ever want to travel to a remote area because it looks cool and exciting but unfortunately is either not accessible or its dangerous to be there? If yes then virtual reality is exactly the domain we should look for. We had the same thought of traveling virtually from comfort of our our house and thus virtual bot was made. The bot has two main concepts. First is the bot itself that is on the remote place and second is the human side of technology, i.e., the vr headset and a controller. The human side gives the instructions to the bots for the movements and have a view of what bot can see using a rpi camera mounted on the bot itself. Since one might want to see what goes around and not just one fixed position we have servo motors connected to the camera which moves it according to the head tilt of the person using the headset. This in total gives a real time virtual experience with full comfort of your living room.
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
    - Currently the bot is controlled with a python script that takes inout from the wireless keyboard, but will soon be upgraded to a controller over the internet
