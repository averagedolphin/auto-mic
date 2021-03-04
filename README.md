# Welcome to AutoMic
Please note that AutoMic is not finished yet.
<br>
Auto Mic is a open source project used to automatically use push to talk in games or chats that require push to talk. You set a 
key to be held when the volume of a microphone reaches a certain threshold. Both volume threshold, and key pressed can be customized via the root window.
<br>
<br>
Auto Mic is licensed under the GNU General Public License v3.0. More information on the GNU v3 license is 
below<br>
[LICENSE.txt](./LICENSE.txt)
<br>

## A Thank You to these contributors!
Creator:
@averagedolphin 
www.averagedolphin.tk

## So, how do I play around with it?

Well its relatively simple.
<br>
Auto Mic contains 5 Python Files. Each one is has its own purpose <br> 
<br>
`./main.py` - Main file that initialises driver.py <br>
`./src/driver.py` - Driver code that directs and '_drives_' everything. <br>
`./src/keyo.py` - Keyboard output functions to press keys via the pynput module. <br>
`./src/gui.py` - Gui Code for AutoMic, uses the tkinter module. <br>
`./src/microphoneio.py` - Input and Output microphone functions

## main.py functions
Main.py calls the `initAutoMic()` function which calls the initialize function in driver.py

