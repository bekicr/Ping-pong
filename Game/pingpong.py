import tkinter as tk
import random

class PingPongGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Ping Pong Game")
        self.master.wm_resizable(False, False)

        self.width = 600
        self.height = 400
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg='black')
        self.canvas.pack()


        self.canvas.create_text(300, 20, text="Ping Pong", fill="white", font=("Arial", 24))

 
        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill='yellow')
        self.paddle = self.canvas.create_rectangle(250, 370, 350, 380, fill='white')


        self.ball_dx = 3 * random.choice([1, -1])
        self.ball_dy = 3


        self.bounce_count = 0
        self.high_score = 0

    
        self.bounce_display = self.canvas.create_text(300, 50, text="Bounces: 0", fill="white", font=("Arial", 16))
        self.high_score_display = self.canvas.create_text(300, 80, text="High Score: 0", fill="white", font=("Arial", 14))

   
        self.canvas.bind("<B1-Motion>", self.move_paddle_with_mouse)

      
        self.try_again_button = tk.Button(self.master, text="Try Again", command=self.reset_game)
        self.try_again_button.pack(pady=10)
        self.try_again_button.place_forget() 

        self.update()

    def move_paddle_with_mouse(self, event):
        """Move paddle with mouse drag, restricting movement within the screen."""
        paddle_coords = self.canvas.coords(self.paddle)
        new_x = event.x

      
        if new_x < 0:
            new_x = 0
        elif new_x > self.width - (paddle_coords[2] - paddle_coords[0]):
            new_x = self.width - (paddle_coords[2] - paddle_coords[0])

 
        self.canvas.coords(self.paddle, new_x, paddle_coords[1], new_x + (paddle_coords[2] - paddle_coords[0]), paddle_coords[3])

    def update(self):
 
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_pos = self.canvas.coords(self.ball)
        paddle_pos = self.canvas.coords(self.paddle)

        if ball_pos[1] <= 0:
            self.ball_dy = -self.ball_dy

   
        if ball_pos[0] <= 0 or ball_pos[2] >= self.width:
            self.ball_dx = -self.ball_dx

      
        if (paddle_pos[0] <= ball_pos[2] <= paddle_pos[2] or paddle_pos[0] <= ball_pos[0] <= paddle_pos[2]) and ball_pos[3] >= paddle_pos[1]:
            self.ball_dy = -self.ball_dy
            self.bounce_count += 1

       
            self.ball_dx *= 1.05
            self.ball_dy *= 1.05

     
            self.canvas.itemconfig(self.bounce_display, text=f"Bounces: {self.bounce_count}")

       
            if self.bounce_count > self.high_score:
                self.high_score = self.bounce_count
                self.canvas.itemconfig(self.high_score_display, text=f"High Score: {self.high_score}")

   
        if ball_pos[3] >= self.height:
            self.show_try_again_button()
            return  

        self.master.after(20, self.update)

    def show_try_again_button(self):
     
        self.try_again_button.place(x=250, y=180)

    def reset_game(self):
       
        self.canvas.coords(self.ball, 290, 50, 310, 70)  
        self.ball_dx = 3 * random.choice([1, -1])
        self.ball_dy = 3
        self.bounce_count = 0  
        self.canvas.itemconfig(self.bounce_display, text=f"Bounces: {self.bounce_count}")
        self.try_again_button.place_forget() 
        self.update()

if __name__ == "__main__":
    root = tk.Tk()
    game = PingPongGame(root)
    root.mainloop()
