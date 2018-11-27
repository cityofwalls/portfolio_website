/**
* Building.java
* Author: @author Jesse Battalino
* Modified: @version 2/19/2016
* A method that will provide the calls to create buildings when given a set of paramenters
*/

import java.awt.*;

public class Building 
{
	private int x, y, width, height;
	private Color color;
	
	/**
	* Constructor: Sets up a rectangular building filled with a given color
	* @param upperX  initalizes top left of building along the x-axis
	* @param upperY  initalizes top left of building along the y-axis
	* @param buildWidth  sets building's width from left to right along x-axis
	* @param buildHeight  sets building's height from left to right along y-axis
	* @param shade  sets color for building
	*/
	
	public Building (int upperX, int upperY, int buildWidth, int buildHeight, Color shade) 
	{
		x = upperX;
		y = upperY;
		width = buildWidth;
		height = buildHeight;
		color = shade;
	}
	
	/**
	* Width accessor
	* @return width  the current width of a building/window
	*/
	
	public int getWidth () 
	{
		return width;
	}
	
	/**
	* Height accessor
	* @return height  the current height of a building/window
	*/
	
	public int getHeight () 
	{
		return height;
	}
	
	/**
	* Width mutator
	* @param w  the requested width
	*/
	
	public void setWidth (int w) 
	{
		width = w;
	}
	
	/**
	* Height mutator
	* @param h  the requested height
	*/
	
	public void setHeight (int h) 
	{
		height = h;
	}
	
	/**
	* Color mutator
	* @param c  the requested color
	*/
	
	public void setColor (Color c)
	{
		color = c;
	}
	
	/**
	* Draws a building or window with the specified parameters
	*/
	
	public void draw (Graphics page) 
	{
		page.setColor (color);
		page.fillRect (x, y, width, height);
	}
}