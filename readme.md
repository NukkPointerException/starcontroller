# Star Controller
This is a (very) simple Python server built using Flask that allows remote control of the Raspberry Pi Christmas Tree Star sold by The Pi Hut (https://thepihut.com/products/raspberry-pi-christmas-tree-star)

The aim of this project was to provide a simple web UI that allows control of the start without needing to SSH into your Christmas Tree (writing that sentence was weird).
Normally you would need to SSH into the Pi, and manually run the script that controls the star. This server runs those scripts for you when it receives requests on specific end points.

This was built very quickly to provide a handy way to remotely control the star. _You should not expose this server outside your network_.
  
# Use
Simply clone the repository onto the Pi that the star is plugged into, and run the _app.py_ script. 
This will start a server running on port 5000, which can then be accessed by any other device on the same network.
The interface was designed with phones in mind, so is quite simple with large buttons and bright colours 
(can also be used as an excellent distraction for the toddler in your life).

# Currently Supported Light Controls
- All On
- All Off
- Twinkle (my personal favourite)
- Pulse
- In/Out

# Extending
To enable a new style of lighting in the server, complete the following steps.
1. Add a new file to the starcode folder, following the style of the existing code that is in there.
2. Add a new endpoint to the server, by copying the _turn_on_ function and modifying the end point in the annotation, and the name of python script that is run when the end point is called.
3. Add a new button to the html page, following the style of the other buttons.
 
# FAQs
Q: What is this for again?  
A: It lets you remotely launch python scripts on a raspberry pi.

Q: Your implementation sucks.  
A: That's not a question.

Q: Merry/Happy Holidays/Christmas/\<Insert Festival Here>?  
A: Yes.  Merry/Happy Holidays/Christmas/\<Insert Festival Here>!