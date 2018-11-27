/**
* SpaceShip.java
* Author: @author Jesse Battalino
* Modified: @version 4/11/2016
* A simple program to manage a SpaceShipPanel object
*/

import javax.swing.*;
import java.awt.*;

public class SpaceShip 
{
	public static void main (String[] args) 
	{
		JFrame frame = new JFrame ("SpaceShip");
		frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
		
		frame.getContentPane().add(new SpaceShipPanel());
		
		frame.pack();
		frame.setVisible(true);
	}
}