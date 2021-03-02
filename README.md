#Welcome to AutoMic
Auto Mic is a open source project used to automatically use Push to Talk in games that require push to talk. You set a 
key to press once the volume of a microphone reaches a certain threshold. Both are selected in the 
<br>
<br>
Auto Mic is licensed under the GNU General Public License v3.0. More information on the GNU v3 license is 
below<br>
[LICENSE.md](./LICENSE.md)
<br>
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
