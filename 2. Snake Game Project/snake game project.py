import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Game settings
SNAKE_SIZE = 20
SNAKE_SPEED_OPTIONS = {
    "Easy": 50,
    "Medium": 100,
    "Hard": 200
}

class BoxSnakeGame:
    def __init__(self, root, speed, app):
        self.root = root
        self.app = app
        self.root.title("Smooth Snake Game")

        # Get screen dimensions
        self.game_width = root.winfo_screenwidth() - 100  # Leave some space from the edges
        self.game_height = root.winfo_screenheight() - 150  # Leave some space from the edges

        # Create a frame to act as a border
        self.border_frame = tk.Frame(root, bd=10, bg='brown')
        self.border_frame.pack(padx=20, pady=20)  # Add padding around the border

        # Create the canvas inside the border frame
        self.canvas = tk.Canvas(self.border_frame, width=self.game_width, height=self.game_height, bg='black')
        self.canvas.pack()

        # Initialize the snake body
        self.snake = [(100, 100), (100 - SNAKE_SIZE, 100), (100 - 2 * SNAKE_SIZE, 100)]
        self.direction = 'Right'
        self.running = True
        self.score = 0  # Initialize score
        self.high_score = 0  # Initialize high score
        self.paused = False  # Initialize paused state

        # Draw snake body
        self.draw_snake()

        # Create initial food
        self.food = None
        self.create_food()

        # Display the score and high score
        self.score_label = self.canvas.create_text(10, 10, anchor='nw', fill='white', font=("Arial", 14), text=f"Score: {self.score}")

        # Bind keys for movement and pause
        root.bind("<KeyPress>", self.change_direction)
        root.bind("<space>", self.toggle_pause)  # Space bar to toggle pause

        # Set the snake speed
        self.speed = speed

        # Start the game loop
        self.move_snake()

    def draw_snake(self):
        # Clear the existing snake body on the canvas
        self.canvas.delete("snake")
        # Draw body segments as overlapping ovals for a smooth look
        for x, y in self.snake:
            self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='green', tags="snake")

    def create_food(self):
        # Randomly position the food
        while True:
            x = random.randint(0, (self.game_width // SNAKE_SIZE) - 1) * SNAKE_SIZE
            y = random.randint(0, (self.game_height // SNAKE_SIZE) - 1) * SNAKE_SIZE
            if (x, y) not in self.snake:  # Ensure food doesn't spawn on the snake
                break
        self.food = self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='red')

    def change_direction(self, event):
        # Update direction based on arrow key pressed
        if event.keysym == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif event.keysym == 'Down' and self.direction != 'Up':
            self.direction = 'Down'
        elif event.keysym == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif event.keysym == 'Right' and self.direction != 'Left':
            self.direction = 'Right'

    def move_snake(self):
        if not self.running or self.paused:
            return

        # Get the current head position
        head_x, head_y = self.snake[0]

        # Calculate the new position of the head
        if self.direction == 'Right':
            head_x += SNAKE_SIZE
        elif self.direction == 'Left':
            head_x -= SNAKE_SIZE
        elif self.direction == 'Up':
            head_y -= SNAKE_SIZE
        elif self.direction == 'Down':
            head_y += SNAKE_SIZE

        new_head = (head_x, head_y)

        # Check for collisions with walls or self
        if (
            head_x < 0 or head_x >= self.game_width or 
            head_y < 0 or head_y >= self.game_height or
            new_head in self.snake
        ):
            self.game_over()
            return

        # Move the snake by adding the new head
        self.snake.insert(0, new_head)

        # Check if the snake eats the food
        if self.canvas.coords(self.food) == [head_x, head_y, head_x + SNAKE_SIZE, head_y + SNAKE_SIZE]:
            # Food eaten; create new food and increase score
            self.canvas.delete(self.food)
            self.create_food()
            self.score += 5  # Increment score by 5
            self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}")  # Update score display
            # Update high score
            if self.score > self.high_score:
                self.high_score = self.score
        else:
            # Remove the tail segment
            self.snake.pop()

        # Redraw the snake
        self.draw_snake()

        # Continue moving
        if  not self.paused:
            self.root.after(self.speed, self.move_snake)
            return
        
    def game_over(self):
        self.running = False
        result = messagebox.askquestion("Game Over", f"Your Score: {self.score}\nHigh Score: {self.high_score}\nWould you like to Replay?")

        if result == 'yes':
            self.restart_game()
        else:
            self.app.close_game(self)  # Close the current game frame and return to game selection

    def toggle_pause(self, event):
        # Toggle the paused state
        self.paused = not self.paused
        if self.paused:
            # Show paused text when the game is paused
            self.canvas.create_text(self.game_width // 2, self.game_height // 2, 
                                    text="PAUSED", fill="yellow", font=("Arial", 24), tags="paused")
        else:
            # Remove the paused text when resuming
            self.canvas.delete("paused")
            self.move_snake()  # Resume the game loop when unpaused

    def restart_game(self):
        """Reset the game state."""
        self.score = 0  # Reset score
        self.canvas.delete("all")  # Clear the canvas
        self.snake = [(100, 100), (100 - SNAKE_SIZE, 100), (100 - 2 * SNAKE_SIZE, 100)]  # Reset snake
        self.direction = 'Right'  # Reset direction
        self.running = True  # Set running to True
        self.paused = False  # Reset paused state

        self.draw_snake()  # Draw snake again
        self.create_food()  # Create new food

        # Recreate the score label
        self.score_label = self.canvas.create_text(10, 10, anchor='nw', fill='white', font=("Arial", 14), text=f"Score: {self.score}")  # Reset score display

        self.move_snake()  # Start the game loop again

# Constants for game dimensions and snake size
GAME_WIDTH = 1510
GAME_HEIGHT = 770

class ClassicalSnakeGame:
    def __init__(self, root, speed, app):
        self.root = root
        self.app = app
        self.root.title("Classical Snake Game")

        # Create the canvas inside the window
        self.canvas = tk.Canvas(self.root, width=GAME_WIDTH, height=GAME_HEIGHT, bg='black')
        self.canvas.pack()

        # Initialize the snake body
        self.snake = [(100, 100), (100 - SNAKE_SIZE, 100), (100 - 2 * SNAKE_SIZE, 100)]
        self.direction = 'Right'
        self.running = True
        self.score = 0
        self.high_score = 0
        self.paused = False

        # Draw snake body
        self.draw_snake()

        # Set the snake speed
        self.speed = speed

        # Create initial food
        self.food = None
        self.create_food()

        # Display the score
        self.score_label = self.canvas.create_text(10, 10, anchor='nw', fill='white', font=("Arial", 14), text=f"Score: {self.score}")

        # Bind keys for movement and pause
        root.bind("<KeyPress>", self.change_direction)
        root.bind("<space>", self.toggle_pause)

        # Start the game loop
        self.move_snake()

    def draw_snake(self):
        """Draw the snake on the canvas."""
        self.canvas.delete("snake")  # Clear existing snake
        for x, y in self.snake:
            self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='green', tags="snake")

    def create_food(self):
        """Randomly place food on the canvas."""
        while True:
            x = random.randint(0, (GAME_WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE
            if (x, y) not in self.snake:  # Ensure food doesn't spawn on the snake
                break
        self.food = self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='red')

    def change_direction(self, event):
        """Change the direction of the snake based on arrow key pressed."""
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            opposite_directions = {
                'Up': 'Down',
                'Down': 'Up',
                'Left': 'Right',
                'Right': 'Left'
            }
            if self.direction != opposite_directions[event.keysym]:
                self.direction = event.keysym

    def move_snake(self):
        """Move the snake in the current direction."""
        if not self.running:
            return

        # Get the current head position
        head_x, head_y = self.snake[0]

        # Calculate the new position of the head based on direction
        if self.direction == 'Right':
            head_x += SNAKE_SIZE
        elif self.direction == 'Left':
            head_x -= SNAKE_SIZE
        elif self.direction == 'Up':
            head_y -= SNAKE_SIZE
        elif self.direction == 'Down':
            head_y += SNAKE_SIZE

        # Wrap-around logic for continuous movement
        head_x %= GAME_WIDTH
        head_y %= GAME_HEIGHT

        new_head = (head_x, head_y)

        # Check if the snake collides with itself
        if new_head in self.snake:
            self.game_over()
            return

        # Check if the snake eats the food (consider wrap-around logic)
        if self.check_food_collision(new_head):
            # Food eaten; create new food
            self.canvas.delete(self.food)
            self.create_food()
            self.score += 5  # Increment score
            self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}")  # Update score display
            # Update high score
            if self.score > self.high_score:
                self.high_score = self.score
        else:
            # Remove the tail segment if no food was eaten
            self.snake.pop()

        # Move the snake by adding the new head
        self.snake.insert(0, new_head)

        # Redraw the snake
        self.draw_snake()

        # Continue moving if not paused
        if not self.paused:
            self.root.after(self.speed, self.move_snake)

    def check_food_collision(self, head):
        """Check if the snake's head is colliding with the food, including wrapped positions."""
        food_coords = self.canvas.coords(self.food)

        # Get the food's actual position
        food_x = food_coords[0]
        food_y = food_coords[1]

        # Check direct collision
        if (head[0] == food_x and head[1] == food_y):
            return True

        # Check wrapped positions
        wrapped_food_x = food_x + GAME_WIDTH
        wrapped_food_y = food_y + GAME_HEIGHT

        # Check if the snake's head matches any of the wrapped positions
        if (head[0] in [food_x, food_x + GAME_WIDTH] and head[1] in [food_y, food_y + GAME_HEIGHT]):
            return True

        # Check for negative wrap-around positions
        if (head[0] in [food_x - GAME_WIDTH, food_x] and head[1] in [food_y - GAME_HEIGHT, food_y]):
            return True

        return False

    def game_over(self):
        """Handle game over logic."""
        self.running = False
        result = messagebox.askquestion("Game Over", f"Your Score: {self.score}\nHigh Score: {self.high_score}\nWould you like to Replay?")

        if result == 'yes':
            self.restart_game()
        else:
            self.app.close_game(self)  # Close the current game frame and return to game selection  # Close the current game frame and return to game selection

    def toggle_pause(self, event):
        """Toggle the paused state."""
        self.paused = not self.paused
        if self.paused:
            self.canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2, text="PAUSED", fill="yellow", font=("Arial", 24), tags="paused")
        else:
            self.canvas.delete("paused")
            self.move_snake()  # Resume the game loop when unpaused

    def restart_game(self):
        """Reset the game state."""
        self.score = 0  # Reset score
        self.canvas.delete("all")  # Clear the canvas
        self.snake = [(100, 100), (100 - SNAKE_SIZE, 100), (100 - 2 * SNAKE_SIZE, 100)]  # Reset snake
        self.direction = 'Right'  # Reset direction
        self.running = True  # Set running to True
        self.paused = False  # Reset paused state

        self.draw_snake()  # Draw snake again
        self.create_food()  # Create new food

        # Recreate the score label
        self.score_label = self.canvas.create_text(10, 10, anchor='nw', fill='white', font=("Arial", 14), text=f"Score: {self.score}")

        self.move_snake()  # Start the game loop again
        
BAR_MIN_SIZE = 40  # Minimum bar size (applies to height for vertical bars and width for horizontal bars)
BAR_MAX_SIZE = 100  # Maximum bar size (applies to height for vertical bars and width for horizontal bars)
NUM_BARS = 20  # Number of bars to place in the game area

class BoxBarSnakeGame:
    def __init__(self, root, speed, app):
        self.root = root
        self.app = app
        self.root.title("Box Snake Game with Vertical and Horizontal Bars")

        # Get screen dimensions
        self.game_width = root.winfo_screenwidth() - 100
        self.game_height = root.winfo_screenheight() - 150

        # Create a frame to act as a border
        self.border_frame = tk.Frame(root, bd=10, bg='brown')
        self.border_frame.pack(padx=20, pady=20)

        # Create the canvas inside the border frame
        self.canvas = tk.Canvas(self.border_frame, width=self.game_width, height=self.game_height, bg='black')
        self.canvas.pack()

        # Initialize the snake body
        self.snake = [(100, 100), (100 - SNAKE_SIZE, 100), (100 - 2 * SNAKE_SIZE, 100)]
        self.direction = 'Right'
        self.running = True
        self.score = 0
        self.high_score = 0
        self.paused = False

        # Draw snake body
        self.draw_snake()

        # Create initial food
        self.food = None
        self.create_food()

        # Draw bars
        self.bars = self.create_bars()

        # Display the score and high score
        self.score_label = self.canvas.create_text(10, 10, anchor='nw', fill='white', font=("Arial", 14), text=f"Score: {self.score}")

        # Bind keys for movement and pause
        root.bind("<KeyPress>", self.change_direction)
        root.bind("<space>", self.toggle_pause)

        # Set the snake speed
        self.speed = speed

        # Start the game loop
        self.move_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='green', tags="snake")

    def create_food(self):
        while True:
            x = random.randint(0, (self.game_width // SNAKE_SIZE) - 1) * SNAKE_SIZE
            y = random.randint(0, (self.game_height // SNAKE_SIZE) - 1) * SNAKE_SIZE
            if (x, y) not in self.snake:
                break
        self.food = self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='red')

    def create_bars(self):
        bars = []
        for _ in range(NUM_BARS):
            while True:
                x = random.randint(0, (self.game_width // SNAKE_SIZE) - 1) * SNAKE_SIZE
                y = random.randint(0, (self.game_height // SNAKE_SIZE) - 1) * SNAKE_SIZE

                # Randomly decide if the bar is vertical or horizontal
                orientation = random.choice(["vertical", "horizontal"])

                if orientation == "vertical":
                    # Randomly choose the height for the vertical bar
                    height = random.randint(BAR_MIN_SIZE // SNAKE_SIZE, BAR_MAX_SIZE // SNAKE_SIZE) * SNAKE_SIZE
                    if (x, y) not in self.snake and (x, y) != self.food:
                        bars.append((x, y, BAR_MIN_SIZE, height, orientation))
                        self.canvas.create_rectangle(x, y, x + BAR_MIN_SIZE, y + height, fill='brown', outline='brown')
                        break
                else:
                    # Randomly choose the width for the horizontal bar
                    width = random.randint(BAR_MIN_SIZE // SNAKE_SIZE, BAR_MAX_SIZE // SNAKE_SIZE) * SNAKE_SIZE
                    if (x, y) not in self.snake and (x, y) != self.food:
                        bars.append((x, y, width, BAR_MIN_SIZE, orientation))
                        self.canvas.create_rectangle(x, y, x + width, y + BAR_MIN_SIZE, fill='brown', outline='brown')
                        break
        return bars

    def change_direction(self, event):
        if event.keysym == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif event.keysym == 'Down' and self.direction != 'Up':
            self.direction = 'Down'
        elif event.keysym == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif event.keysym == 'Right' and self.direction != 'Left':
            self.direction = 'Right'

    def move_snake(self):
        if not self.running or self.paused:
            return

        # Get the current head position
        head_x, head_y = self.snake[0]

        # Calculate the new position of the head
        if self.direction == 'Right':
            head_x += SNAKE_SIZE
        elif self.direction == 'Left':
            head_x -= SNAKE_SIZE
        elif self.direction == 'Up':
            head_y -= SNAKE_SIZE
        elif self.direction == 'Down':
            head_y += SNAKE_SIZE

        new_head = (head_x, head_y)

        # Check for collisions with the game borders
        if head_x < 0 or head_x >= self.game_width or head_y < 0 or head_y >= self.game_height:
            self.game_over()
            return

        # Check for collisions with the bars
        for (bar_x, bar_y, bar_width, bar_height, orientation) in self.bars:
            if (new_head[0] >= bar_x and new_head[0] < bar_x + bar_width and
                new_head[1] >= bar_y and new_head[1] < bar_y + bar_height):
                self.game_over()
                return

        # Check for self-collision
        if new_head in self.snake:
            self.game_over()
            return

        # Move the snake by adding the new head
        self.snake.insert(0, new_head)

        # Check if the snake eats the food
        if self.canvas.coords(self.food) == [head_x, head_y, head_x + SNAKE_SIZE, head_y + SNAKE_SIZE]:
            self.canvas.delete(self.food)
            self.create_food()
            self.score += 5
            self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}")
            if self.score > self.high_score:
                self.high_score = self.score
        else:
            self.snake.pop()

        # Redraw the snake
        self.draw_snake()

        # Continue moving
        if not self.paused:
            self.root.after(self.speed, self.move_snake)

    def game_over(self):
        self.running = False
        result = messagebox.askquestion("Game Over", f"Your Score: {self.score}\nHigh Score: {self.high_score}\nWould you like to Replay?")

        if result == 'yes':
            self.restart_game()
        elif result == 'No':
            self.app.close_game(self)
        else:
            self.app.close_game(self)
            
    def toggle_pause(self, event):
        self.paused = not self.paused
        if self.paused:
            self.canvas.create_text(self.game_width // 2, self.game_height // 2, 
                                    text="PAUSED", fill="yellow", font=("Arial", 24), tags="paused")
        else:
            self.canvas.delete("paused")
            self.move_snake()

    def restart_game(self):
        self.score = 0
        self.canvas.delete("all")
        self.snake = [(100, 100), (100 - SNAKE_SIZE, 100), (100 - 2 * SNAKE_SIZE, 100)]
        self.direction = 'Right'
        self.running = True
        self.paused = False

        self.draw_snake()
        self.create_food()
        self.bars = self.create_bars()  # Create new bars

        self.score_label = self.canvas.create_text(10, 10, anchor='nw', fill='white', font=("Arial", 14), text=f"Score: {self.score}")

        self.move_snake()

class TunnelSnakeGame:
    def __init__(self, root, speed, app):
        self.root = root
        self.app = app
        self.root.title("Classical Snake Game")

        # Create the canvas inside the window
        self.canvas = tk.Canvas(self.root, width=GAME_WIDTH, height=GAME_HEIGHT, bg='black')
        self.canvas.pack()

        # Initialize the snake body
        self.snake = [(100, 100), (100 - SNAKE_SIZE, 100), (100 - 2 * SNAKE_SIZE, 100)]
        self.direction = 'Right'
        self.running = True
        self.score = 0
        self.high_score = 0
        self.paused = False

        # Define barriers (x1, y1, x2, y2)
        self.barriers = self.create_barriers()

        # Draw snake body and barriers
        self.draw_snake()
        self.draw_barriers()

        # Set the snake speed
        self.speed = speed

        # Create initial food
        self.food = None
        self.create_food()
        
        # Display the score and high score
        self.score_label = self.canvas.create_text(10, 10, anchor='nw', fill='white', font=("Arial", 14), text=f"Score: {self.score}")

        # Bind keys for movement
        root.bind("<KeyPress>", self.change_direction)
        root.bind("<space>", self.toggle_pause)
        root.bind("<Escape>", self.exit_game)

        # Start the game loop
        self.move_snake()

    def create_barriers(self):
        # Define and return the barriers in the game
        return [
           #(100, 50, 150, 70),     # Barrier 1
           # (400, 100, 50, 120),  # Barrier 2
           (400, 100, 900, 130),  # Barrier 4
           #(850, 200, 950, 220),   # Barrier 5
            #(1100, 100, 1200, 120), # Barrier 6
            (50, 400, 150, 420),    # Barrier 7
            #(200, 300, 300, 320),    # Barrier 8
            (400, 350, 900, 380),    # Barrier 9
            #(800, 300, 900, 320),     # Barrier 10
            (1200, 400, 1300, 420),   # Barrier 11
            (1200, 600, 1300, 620),    # Barrier 12
            #(1400, 600, 1450, 620),     # Barrier 13
            (0, 0, 20, 100),           # Left vertical barrier (top-left L)
            (0, 0, 100, 20),           # Top horizontal barrier (top-left L)
            (GAME_WIDTH - 20, 0, GAME_WIDTH, 100),  # Right vertical barrier (top-right L)
            (GAME_WIDTH - 100, 0, GAME_WIDTH, 20),   # Top horizontal barrier (top-right L)
            (0, GAME_HEIGHT - 20, 100, GAME_HEIGHT), # Left vertical barrier (bottom-left L)
            (0, GAME_HEIGHT - 100, 20, GAME_HEIGHT),  # Bottom horizontal barrier (bottom-left L)
            (GAME_WIDTH - 20, GAME_HEIGHT - 100, GAME_WIDTH, GAME_HEIGHT),  # Right vertical barrier (bottom-right L)
            (GAME_WIDTH - 100, GAME_HEIGHT - 20, GAME_WIDTH, GAME_HEIGHT)   # Bottom horizontal barrier (bottom-right L)
        ]

    def draw_snake(self):
        # Clear the existing snake body on the canvas
        self.canvas.delete("snake")
        # Draw body segments as overlapping ovals for a smooth look
        for x, y in self.snake:
            self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='green', tags="snake")

    def draw_barriers(self):
        # Draw barriers on the canvas
        for x1, y1, x2, y2 in self.barriers:
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='blue', tags="barrier")

    def create_food(self):
        # Randomly position the food
        while True:
            x = random.randint(0, (GAME_WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE

            # Check if the food spawns on the snake or barriers
            if (x, y) not in self.snake and not self.check_collision_with_barriers((x, y)):
                break

        self.food = self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='red')

    def change_direction(self, event):
        # Update direction based on arrow key pressed
        if event.keysym == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif event.keysym == 'Down' and self.direction != 'Up':
            self.direction = 'Down'
        elif event.keysym == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif event.keysym == 'Right' and self.direction != 'Left':
            self.direction = 'Right'

    def move_snake(self):
        if not self.running:
            return

        # Get the current head position
        head_x, head_y = self.snake[0]

        # Calculate the new position of the head
        if self.direction == 'Right':
            head_x += SNAKE_SIZE
        elif self.direction == 'Left':
            head_x -= SNAKE_SIZE
        elif self.direction == 'Up':
            head_y -= SNAKE_SIZE
        elif self.direction == 'Down':
            head_y += SNAKE_SIZE

        # Wrap around the snake when it goes beyond the window boundary
        if head_x >= GAME_WIDTH:
            head_x = 0  # Reappear from the left side
        elif head_x < 0:
            head_x = GAME_WIDTH - SNAKE_SIZE  # Reappear from the right side
        if head_y >= GAME_HEIGHT:
            head_y = 0  # Reappear from the top side
        elif head_y < 0:
            head_y = GAME_HEIGHT - SNAKE_SIZE  # Reappear from the bottom side

        new_head = (head_x, head_y)

        # Check if the snake collides with itself or the barriers
        if new_head in self.snake or self.check_collision_with_barriers(new_head):
            self.game_over()
            return

        # Move the snake by adding the new head
        self.snake.insert(0, new_head)

        # Check if the snake eats the food
        if self.canvas.coords(self.food) == [head_x, head_y, head_x + SNAKE_SIZE, head_y + SNAKE_SIZE]:
            # Food eaten; create new food
            self.canvas.delete(self.food)
            self.create_food()
            self.score += 5  # Increment score by 5
            self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}")  # Update score display
            # Update high score
            if self.score > self.high_score:
                self.high_score = self.score
        else:
            # Remove the tail segment
            self.snake.pop()

        # Redraw the snake
        self.draw_snake()

        # Continue moving if not paused
        if not self.paused:
            self.root.after(self.speed, self.move_snake)

    def check_collision_with_barriers(self, new_head):
        head_x, head_y = new_head
        for x1, y1, x2, y2 in self.barriers:
            if x1 <= head_x < x2 and y1 <= head_y < y2:
                return True
        return False

    def exit_game(self, event):
        """Exit the game and close the application."""
        result = messagebox.askquestion("Exit", "Are you sure you want to exit the game?")
        if result == 'yes':
            self.root.destroy()  # Close the application if 'Yes' is selected

    def game_over(self):
        result = messagebox.askquestion("Game Over", "Do you want to play again?")
        if result == 'yes':
            self.restart_game()
        elif result == 'No':
            self.app.close_game(self)
        else:
            self.app.close_game(self)
            
    def toggle_pause(self, event):
        # Toggle the paused state
        self.paused = not self.paused
        if self.paused:
            # Show paused text when the game is paused
            self.canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2, 
                                    text="PAUSED", fill="yellow", font=("Arial", 24), tags="paused")
        else:
            # Remove the paused text when resuming
            self.canvas.delete("paused")
            self.move_snake()  # Resume the game loop when unpaused

    def restart_game(self):
        """Reset the game state."""
        self.score = 0  # Reset score
        self.canvas.delete("all")  # Clear the canvas
        self.snake = [(100, 100), (100 - SNAKE_SIZE, 100), (100 - 2 * SNAKE_SIZE, 100)]  # Reset snake
        self.direction = 'Right'  # Reset direction
        self.running = True  # Set running to True
        self.paused = False  # Reset paused state

        self.draw_snake()  # Draw snake again
        self.draw_barriers()  # Draw barriers again
        self.create_food()  # Create new food

        # Recreate the score label
        self.score_label = self.canvas.create_text(10, 10, anchor='nw', fill='white', font=("Arial", 14), text=f"Score: {self.score}")  # Reset score display

        self.move_snake()  # Start the game loop again

class SnakeGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game Menu")

        # Get the screen width and height
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # Set the window size to match the screen size
        root.geometry(f"{self.screen_width}x{self.screen_height}")

        # Load the background image using Pillow
        background_image = Image.open("C:/Users/udayk/Downloads/snake game background image.jpg")
        background_image = background_image.resize((self.screen_width, self.screen_height), Image.Resampling.LANCZOS)  # Resize to fit the screen
        self.bg_image_tk = ImageTk.PhotoImage(background_image)

        # Create a Label widget for the background and place it
        background_label = tk.Label(root, image=self.bg_image_tk)
        background_label.place(x=0, y=0, width=self.screen_width, height=self.screen_height)

        # Create the menu bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # Create a File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Help", command=self.help_file, font=("Arial", 15))
        self.file_menu.add_command(label="About", command=self.about_file, font=("Arial", 15))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app, font=("Arial", 15))

        # Add the File menu to the menu bar
        self.menu_bar.add_cascade(label="Menu", menu=self.file_menu,font=("Arial", 15))

        # Create a frame for game types
        self.game_type_frame = tk.Frame(root, bg='#FF8040')
        self.game_type_frame.pack(pady=20)

        # Create buttons for different snake game types
        self.classic_button = tk.Button(self.game_type_frame, text="Classical Snake Game",width=18,
                                         command=lambda: self.start_game("Classical"), font=("Arial", 24), bg="#FD1C03")
        self.classic_button.pack(pady=10)

        self.box_button = tk.Button(self.game_type_frame, text="Box Snake Game",width=18,
                                     command=lambda: self.start_game("Box"), font=("Arial", 24), bg="#FFDF00")
        self.box_button.pack(pady=10)

        self.bar_button = tk.Button(self.game_type_frame, text="Bar Snake Game",width=18,
                                     command=lambda: self.start_game("Bar"), font=("Arial", 24), bg="#59E817")
        self.bar_button.pack(pady=10)

        self.tunnel_button = tk.Button(self.game_type_frame, text="Tunnel Snake Game",width=18,
                                        command=lambda: self.start_game("Tunnel"), font=("Arial", 24), bg="#01F9C6")
        self.tunnel_button.pack(pady=10)

    def help_file(self):
        messagebox.showinfo("Help","Add Soon!")

    def about_file(self):
        messagebox.showinfo("About", "Add Soon!")

    def exit_app(self):
        # Ask the user if they want to exit the application
        result = messagebox.askquestion("Exit", "Are you sure you want to exit the game?")
        if result == 'yes':
            self.root.destroy()  # Close the application if 'Yes' is selected

    def start_game(self, game_type):
        # Hide game type buttons and show difficulty buttons
        self.game_type_frame.pack_forget()
        
        # Create difficulty buttons
        self.easy_button = tk.Button(self.root, text="Easy", command=lambda: self.launch_game(game_type, "Hard"), width=6,font=("Arial", 18,"bold"), bg="#FD1C03")
        self.easy_button.pack(pady=20)

        self.medium_button = tk.Button(self.root, text="Medium", command=lambda: self.launch_game(game_type, "Medium"), width=6, font=("Arial", 18,"bold"), bg="#FFDF00")
        self.medium_button.pack(pady=20)

        self.hard_button = tk.Button(self.root, text="Hard", command=lambda: self.launch_game(game_type, "Easy"), font=("Arial", 18,"bold"), width=6, bg="#59E817")
        self.hard_button.pack(pady=20)

        # Add Back button
        self.back_button = tk.Button(self.root, text="Back", command=self.go_back, font=("Arial", 18,"bold"), width=6, bg='#FF8040')
        self.back_button.pack(pady=20)

    def go_back(self):
        # Hide difficulty buttons and Back button
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.back_button.pack_forget()

        # Show game type buttons again
        self.game_type_frame.pack(pady=20)

    def launch_game(self, game_type, difficulty):
        # Start the selected game type with the specified difficulty
        speed = SNAKE_SPEED_OPTIONS[difficulty]
        if game_type == "Box":
            self.new_game = BoxSnakeGame(self.root, speed, self)
        elif game_type == "Classical":
            self.new_game = ClassicalSnakeGame(self.root, speed, self)
        elif game_type == "Bar":
            self.new_game = BoxBarSnakeGame(self.root, speed, self)
        elif game_type == "Tunnel":
            self.new_game = TunnelSnakeGame(self.root, speed, self)

        # Hide difficulty buttons
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.back_button.pack_forget()

    def close_game(self, game):
        # Close the current game frame
        game.canvas.pack_forget()# Clear the game canvas
        game.canvas.delete("all")
        if hasattr(game, 'border_frame'):
            game.border_frame.destroy()  # Remove the border frame
        self.game_type_frame.pack()  # Show game type buttons again     

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeGameApp(root)
    root.mainloop()
