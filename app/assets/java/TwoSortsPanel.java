/**
* TwoSortsPanel.java
* Author: @author Jesse Battalino
* Modified: @version 4/30/2016
* A program to manage a visual display of two sorting algorithms inside a panel. 
* Each pass of the sort (selection and insertion) is managed with a JButton.
*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class TwoSortsPanel extends JPanel 
{
	Random gen = new Random();
	
	private final int SIZE = gen.nextInt(11) + 20;
	private int[] select = new int[SIZE];
	private int[] insert = new int[SIZE];
	private JButton sort;
	private int count = 0;
	private final int MID = 250;
	private int left = 10;
	private boolean sorted = false;
	
	/**
	* Constructor: Initializes 2 arrays of length [10-30] with random values placed into corresponding indecies. 
	* Sets up a panel with a control button and rectangle representations of the values within the arrays.
	*/
	public TwoSortsPanel() 
	{
		boolean repeat = false; //use to check if a random number has been picked already
		
		for (int i = 0; i < SIZE; i++) 
		{
			int temp = gen.nextInt(30) + 1; //pick a random number [1-30] to be placed in each sort array (select[] and insert[])
			
			//check the randomly generated number against all other generated numbers in the arrays, set flag to true if there are any matches
			for (int j = 0; j < SIZE; j++) 
			{
			    if (temp == select[j]) 
				    repeat = true;
			}
			
			//no matches? set to current index
			if (!repeat) 
			{
				select[i] = temp;
				insert[i] = temp;
				repeat = false; //reset flag for next pass
			}
			
			//there is a match? step back one in loop
			else 
			{
				i--;
				repeat = false; //reset flag for next pass
			}
		}
		
		// debug array values
		/*String test = new String();
		String test2 = new String();
		for (int j = 0; j < SIZE; j++) 
		{
			test += " " + select[j];
			test2 += " " + insert[j];
		}
		System.out.println(test);
		System.out.println(test2);*/
		
		sort = new JButton("Sort");
		sort.addActionListener(new ButtonListener());
		add(sort);
		
		setPreferredSize (new Dimension(500,500));
		setBackground (Color.cyan);
	}
	
	public void paintComponent (Graphics page) 
	{
		super.paintComponent (page);
		Font font = new Font ("Courier", Font.BOLD, 12);
		page.setFont (font);
		
		if (!sorted) 
			page.setColor (Color.red);
		else
			page.setColor (Color.darkGray);
		page.drawString ("Selection Sort", 10, 20);
		
		if (!sorted) 
			page.setColor (Color.blue);
		else
			page.setColor (Color.darkGray);
		page.drawString ("Insertion Sort", 390, 20);
		page.setColor (Color.magenta);
		page.drawString ("Sort Pass: " + count, 210, 45);
		
		if (sorted) 
		{
			page.setColor (new Color(0, gen.nextInt(129) + 82, 0));
			page.drawString ("Complete!", 220, 60);
		}
		
		
		//selection sort
		if (!sorted) 
		{
			int min = count;
			int temp = 0;
			
			for (int scan = min + 1; scan < SIZE; scan++) 
			{
				if (select[scan] < select[min]) 
					min = scan;
			}
				
		    temp = select[min];
			select[min] = select[count];
			select[count] = temp;
		}
		
		//insertion sort
		if (!sorted) 
		{
			int key;
			int position = count;
			if (count > SIZE) 
				key = insert[count + 1];
			else
				key = insert[count];
			
			
			while (position > 0 && key < insert[position - 1]) 
			{
				insert[position] = insert[position - 1];
				position--;
			}
			
			insert[position] = key;
		}
		
		if (!sorted) 
		{
		    display (page, select, Color.red, true);
		    display (page, insert, Color.blue, false);
		}
		else 
		{
			display (page, select, Color.darkGray, true);
			display (page, insert, Color.darkGray, false);
		}
	}
	
	/**
	* @param page  the panel object
	* @param a  an array to be displayed 
	* @param c  the color the chosen array will be displayed in
	* @param b  a switch to determine how the array will be displayed (either above the midpoint (MID)) - true - or below - false -
	*/
	public void display (Graphics page, int[] a, Color c, boolean b) 
	{
		left = 0;
		boolean whichList = b;
		int[] array = new int[SIZE];
		for (int i = 0; i < SIZE; i++) 
		{
			array[i] = a[i];
		}
		
		if (whichList) 
		{
			page.setColor (c);
		    for (int j = 0; j < SIZE; j++) 
		    {
			    left += 15;
			    page.fillRect (left, MID - array[j] - 1, 13, array[j]);
		    }
		}
		else 
		{
			page.setColor (c);
			for (int j = 0; j < SIZE; j++) 
			{
				left += 15;
				page.fillRect (left, MID + 1, 13, array[j]);
			}
		}
	}
	
	/**
	* Listener for button presses.
	*/
	public class ButtonListener implements ActionListener 
	{
		public void actionPerformed (ActionEvent e) 
		{
			if (!sorted) 
			{
				count++;
			    repaint();
				if (count == SIZE)
				{					
				    sorted = true;
					sort.setText ("Done");
				}
			}
		}
	}
}