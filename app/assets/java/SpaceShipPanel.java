/**
* SpaceShipPanel.java
* Author: @author Jesse Battalino
* Modified: @version 4/13/2016
* Manages a simple SpaceShip "game" inside of a SpaceShip Panel
*/

import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SpaceShipPanel extends JPanel
{
	private ArrayList<Point> shotList; //holds point of each mouse click for laser beams
	private Building build1, build2, build3, build4, build5; //5 buildings for background
	private int colorChoose; //will hold random number for laser beam color switch statement
	private Color setter; //will hold randomly chosen color for laser beam
	private Point point, ship; //will hold (x,y) values of mouse click area or position in frame
	private JButton reset; //a button to reset "shots fired" counter
	
	Random gen = new Random(); //use to choose random number for color
	
	/**
	* Constructor: creates a panel 500 pixels by 500 pixels with buildings for the background. The cursor controls a small spaceship that fires
	* lasers of random colors at random areas of the panel.
	*/
	public SpaceShipPanel() 
	{
		shotList = new ArrayList<Point>();

		addMouseListener (new ShotListener());
		addMouseMotionListener (new ShotListener());

		reset = new JButton("Reset");
		reset.addActionListener(new ButtonListener());

		add(reset);

		build1 = new Building (0, 475, 499, 25, Color.blue);
		build2 = new Building (25, 200, 125, 300, Color.black);
		build3 = new Building (165, 250, 100, 250, Color.black);
		build4 = new Building (275, 350, 125, 150, Color.black);
		build5 = new Building (410, 100, 80, 400, Color.black);

		setPreferredSize (new Dimension(500,500));
		setBackground (Color.darkGray);
	}
	
	/**
	* Draws buildings and spaceship
	*/
	public void paintComponent (Graphics page) 
	{
		super.paintComponent (page);
		
		page.setColor (Color.red);
		page.drawString ("Attack the City!", 10, 20);
		page.drawString ("Shots Fired: " + shotList.size(), 400, 20);
		
		build1.draw (page);
		build2.draw (page);
		build3.draw (page);
		build4.draw (page);
		build5.draw (page);
		
		if (ship != null) 
		{
			page.setColor (Color.green);
			page.fillOval (ship.x + 10, ship.y, 15, 15);
			page.setColor (Color.lightGray);
			page.fillOval (ship.x + 5, ship.y + 5, 25, 10);
		}
		
		// Laser color ver. 1.0
		/*colorChoose = gen.nextInt(4);
		switch (colorChoose) 
		{
			case 0: setter = Color.red;
			break;
			case 1: setter = Color.orange;
			break;
			case 2: setter = Color.green;
			break;
			case 3: setter = Color.cyan;
			break;
		}*/
		
		// Laser color ver. 1.1
		setter = new Color(gen.nextInt(256), gen.nextInt(256), gen.nextInt(256));
		
		if (point != null) 
		{
		    page.setColor (setter);
		    page.drawLine (point.x + 10, point.y + 10, gen.nextInt(450) + 25, gen.nextInt(450) + 25);
	    }
	}
	
	/**
	* Listener for mouse events
	*/
	private class ShotListener /*extends JApplet*/ implements MouseListener, MouseMotionListener 
	{
		public void mousePressed (MouseEvent event) 
		{
			shotList.add(event.getPoint());
			point = event.getPoint();
			repaint();
			/*AudioClip laser = getAudioClip(getDocumentBase(), "LaserBeam.wav");
			laser.play();*/ //failed sound. please ignore
		}
		public void mouseClicked (MouseEvent event) {}
		public void mouseReleased (MouseEvent event) {}
		public void mouseEntered (MouseEvent event) {}
		public void mouseExited (MouseEvent event) {}
		public void mouseMoved (MouseEvent event) 
		{
			ship = event.getPoint();
			point = null;
			repaint();
		}
		public void mouseDragged (MouseEvent event) {}
	}
	
	public class ButtonListener implements ActionListener 
	{
		public void actionPerformed (ActionEvent event) 
		{
			shotList = new ArrayList<Point>();
			repaint();
		}
	}
}