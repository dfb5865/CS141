"""
   Use turtle graphics to draw a simple face.

   file: smiling_faces.py
   author: James Heliotis
   author: Ben K Steele
   created: August 2010
   revised: August 2011
"""

import turtle

def initialize():
    """Initialize the turtle so that it is facing North with the pen up."""
    turtle.up()
    turtle.left( 90 )

def drawBorder():
    """Draw a circle for the outline of the face."""
    turtle.right( 90 )
    turtle.down()
    turtle.circle( 100 )
    turtle.up()
    turtle.left( 90 )

def drawMouth():
    """Draw a smiling mouth 60 points wide (30 units per side), 
       40 points above the bottom of the face.
    """
    turtle.forward( 40 )
    turtle.left( 65 )
    turtle.forward( 30 )
    turtle.left( 180 )
    turtle.down()
    turtle.forward( 30 )
    turtle.left( 50 )
    turtle.forward( 30 )
    turtle.left( 180 )
    turtle.up()
    turtle.forward( 30 )
    turtle.left( 65 )
    turtle.forward( 40 )
    turtle.left( 180 )

def drawNose():
    """Draw a nose as an equilateral triangle with sides of 30,
       70 points above the bottom of the face.
    """
    turtle.forward( 70 )
    turtle.left( 90 )
    turtle.down()
    turtle.forward( 15 )
    turtle.right( 120 )
    turtle.forward( 30 )
    turtle.right( 120 )
    turtle.forward( 30 )
    turtle.right( 120 )
    turtle.forward( 15 )
    turtle.up()
    turtle.left( 90 )
    turtle.forward( 70 )
    turtle.left( 180 )

def drawEyes():
    """Draw both eyes as circles of radius 15, 100 points above the bottom
       of the face, and with centers 100 points apart.
    """
    turtle.forward( 100 )
    turtle.left( 90 )
    turtle.forward( 50 )
    turtle.right( 180 )
    drawEye()
    turtle.forward( 100 )
    drawEye()
    turtle.right( 180 )
    turtle.forward( 50 )
    turtle.left( 90 )
    turtle.forward( 100 )
    turtle.left( 180 )

def drawEye():
    """Draw a single eye as a 15-point-radius circle.
       Assume the turtle is facing right at the bottom of where the
       eye will be. Leave the turtle in that same state.
    """
    turtle.down()
    turtle.circle( 15 )
    turtle.up()

def drawFace():
    """Draw a smiling face."""
    drawBorder()
    drawMouth()
    drawNose()
    drawEyes()

def main():
    """The program creates a picture canvas, draws a smiling face and
       waits for the user to respond before terminating.
    """
    initialize()
    drawFace()
    input( "Hit ENTER to continue the program." )
    turtle.left( 180 )
    drawFace()
    input( "Hit ENTER to finish the program." )
    turtle.bye()
	
# now call the main function to run the code

main()
