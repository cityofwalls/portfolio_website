/**
* TwoSorts.java
* Author: @author Jesse Battalino
* Modified: @version 4/28/2016
* A simple program to manage a TwoSortsPanel object
*/

import javax.swing.*;
import java.awt.*;

public class TwoSorts 
{
	public static void main (String[] args) 
	{
		JFrame frame = new JFrame ("TwoSorts");
		frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
		
		frame.getContentPane().add(new TwoSortsPanel());
		
		frame.pack();
		frame.setVisible(true);
	}
}