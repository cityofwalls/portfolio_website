import random
import simplegui

width, height = 800, 800
grid_size = 49
display_centering_offset = 8

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
        #			  Top, Right, Bottom, Left
        self.sides = [True, True, True, True]
        self.neighbors = []
        self.visited = False
        self.previous = None
        
class Grid:
    def __init__(self, number_of_rows, number_of_columns):
        self.cell_width = width // number_of_columns
        self.cell_height = height // number_of_rows
        self.grid = []
        for i in range(number_of_rows):
            self.grid.append([])
            for j in range(number_of_columns):
                new_cell = Cell(i * self.cell_width + display_centering_offset, 
                                j * self.cell_height + display_centering_offset)
                if j > 0:
                    new_cell.neighbors.append(self.grid[i][j - 1])
                    random.shuffle(new_cell.neighbors)
                    self.grid[i][j - 1].neighbors.append(new_cell)
                    random.shuffle(self.grid[i][j - 1].neighbors)
                if i > 0:
                    new_cell.neighbors.append(self.grid[i - 1][j])
                    random.shuffle(new_cell.neighbors)
                    self.grid[i - 1][j].neighbors.append(new_cell)
                    random.shuffle(self.grid[i - 1][j].neighbors)
                self.grid[i].append(new_cell)
                
    def draw_grid(self, c):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                current_cell = self.grid[i][j]
                top, right = current_cell.sides[0], current_cell.sides[1]
                bottom, left = current_cell.sides[2], current_cell.sides[3]
                
                if top:
                    c.draw_line([current_cell.x, current_cell.y], 
                                [current_cell.x + self.cell_width, current_cell.y], 
                                1, "White")
                if right:
                    c.draw_line([current_cell.x + self.cell_width, current_cell.y], 
                                [current_cell.x + self.cell_width, current_cell.y + self.cell_height], 
                                1, "White")
                if bottom:
                    c.draw_line([current_cell.x, current_cell.y + self.cell_height], 
                                [current_cell.x + self.cell_width, current_cell.y + self.cell_height], 
                                1, "White")
                if left:
                    c.draw_line([current_cell.x, current_cell.y], 
                                [current_cell.x, current_cell.y + self.cell_height], 
                                1, "White")
                    
    def draw_path(self, path, c):
        x_offset, y_offset = self.cell_width // 2, self.cell_height // 2
        points = []
        for cell in path:
            points.append((cell.x + x_offset, cell.y + y_offset))
            
        points.insert(0, (points[0][0] - self.cell_width, points[0][1]))
        points.append((points[-1][0] + self.cell_width, points[-1][1]))
            
        c.draw_polyline(points, 2, "Red")

class MazeBuilder:
    def __init__(self, grid):
        self.maze = grid
        self.current = self.maze.grid[0][0]
        self.current.visited = True
        
    def _remove_walls(self, current, neighbor):
        if current.x > neighbor.x:
            current.sides[3] = False
            neighbor.sides[1] = False
        elif current.x < neighbor.x:
            current.sides[1] = False
            neighbor.sides[3] = False
        elif current.y > neighbor.y:
            current.sides[0] = False
            neighbor.sides[2] = False
        elif current.y < neighbor.y:
            current.sides[2] = False
            neighbor.sides[0] = False
    
    def _depth_first_search(self, current):
        for neighbor in current.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                self._remove_walls(current, neighbor)
                self._depth_first_search(neighbor)
    
    def create_maze(self):
        self._depth_first_search(self.current)
        
class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        for row in self.maze.grid:
            for cell in row:
                cell.visited = False
                
    def _no_wall_between(self, current_cell, neighbor_cell):
        dx = current_cell.x - neighbor_cell.x
        dy = current_cell.y - neighbor_cell.y
        
        if dx > 0 and not current_cell.sides[3]:
            return True
        if dx < 0 and not current_cell.sides[1]:
            return True
        if dy > 0 and not current_cell.sides[0]:
            return True
        if dy < 0 and not current_cell.sides[2]:
            return True
        
        return False
    
    def _construct_path_to(self, ending_cell):
        result = [ending_cell]
        while not result[0].previous is None:
            result.insert(0, result[0].previous)
            
        return result
    
    def _find_shortest_path(self, q, ending_cell):
        while not len(q) is 0:
            current_cell = q.pop(0)
            if current_cell is ending_cell:
                return self._construct_path_to(current_cell)
            for neighbor_cell in current_cell.neighbors:
                if not neighbor_cell.visited and self._no_wall_between(current_cell, neighbor_cell):
                    neighbor_cell.previous = current_cell
                    neighbor_cell.visited = True
                    q.append(neighbor_cell)
    
    def solve_maze(self):
        starting_cell = self.maze.grid[0][0]
        ending_cell = self.maze.grid[-1][-1]
        
        starting_cell.sides[3] = False
        ending_cell.sides[1] = False
        
        starting_cell.visited = True
        q = [starting_cell]
        shortest_path = self._find_shortest_path(q, ending_cell)
        
        return shortest_path
                    
                    
def setup():
    global maze, shortest_path
    maze = Grid(grid_size, grid_size)
    
    maze_builder = MazeBuilder(maze)
    maze_builder.create_maze()
    
    maze_solver = MazeSolver(maze)
    shortest_path = maze_solver.solve_maze()

def draw(canvas):
    maze.draw_grid(canvas)
    maze.draw_path(shortest_path, canvas)

f = simplegui.create_frame("Maze Generator", width, height)
f.set_draw_handler(draw)

setup()
f.start()