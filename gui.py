import customtkinter as ct
import datetime as time
import pyautogui
from PIL import Image
import function

ct.set_appearance_mode("dark")

# Window Class
class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("The Jiggler")
        self.geometry("300x350")

        # Create a grid layout with a single column and row
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.emblem = ct.CTkImage(light_image=Image.open("images/Mouse_emblem.png"),
                                  dark_image=Image.open("images/Mouse_emblem.png"),
                                  size=(240, 64))
        self.banner_img = ct.CTkLabel(self, text="", image=self.emblem)
        self.banner_img.grid(row=0, column=0, padx=1, pady=5)

        self.countdown_timer = CountdownTimer(self)
        self.countdown_timer.grid(row=1, column=0, padx=10, pady=5)

        self.mode_select = ct.CTkComboBox(self, values=["Move", "Click"], 
                                          border_color="#3B8ED0", button_color="#3B8ED0", 
                                          fg_color="#1F6AA5", dropdown_fg_color="#1F6AA5", 
                                          dropdown_hover_color="#3B8ED0")
        self.mode_select.grid(row=2, column=0, padx=1, pady=10)

        self.start_button = ct.CTkButton(self, text="Start")
        self.start_button.configure(command=self.countdown_timer.start_timer)
        self.start_button.grid(row=3, column=0, padx=20, pady=5)

        self.stop_button = ct.CTkButton(self, text="Stop")
        self.stop_button.configure(command=self.countdown_timer.stop_timer)
        self.stop_button.grid(row=4, column=0, padx=20, pady=10)
        print(self.stop_button.cget("fg_color"))

# The Framed Timer Widget
class CountdownTimer(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)        
        self.configure(corner_radius=5, border_color="gray25", border_width=1)

        self.duration_entry = ct.CTkComboBox(self, values=["10 sec", "30 sec", "1 min", "5 min"])
        self.duration_entry.pack(padx=55, pady=10)

        self.remaining_time = time.timedelta(seconds=0)  # Initialize with 0 seconds

        self.timer_label = ct.CTkLabel(self, text=str(self.remaining_time))
        self.timer_label.pack(padx=10, pady=10)
        
        self.timer_bar = ct.CTkProgressBar(self, orientation="horizontal")
        self.timer_bar.pack(padx=10, pady=10)
        self.timer_bar.set(0)

        self.timer_running = False
        self.timer_id = None
        self.last_mouse_position = None
        self.duration_sec = 0

    def start_timer(self):
        print("Started Timer")
        if not self.timer_running:
            duration_text = self.duration_entry.get()
            self.duration_sec = self.parse_duration(duration_text)
            self.remaining_time = time.timedelta(seconds=self.duration_sec)
            self.timer_label.configure(text=str(self.remaining_time))
            self.timer_running = True
            self.update_timer()
            
    def parse_duration(self, duration_text):
        if duration_text == "10 sec":
            return 10
        elif duration_text == "30 sec":
            return 30
        elif duration_text == "1 min":
            return 60
        elif duration_text == "5 min":
            return 300
        else:
            return 0

    def stop_timer(self):
        print("Stopped Timer")
        if self.timer_running:
            self.timer_running = False
            if self.timer_id is not None:
                self.after_cancel(self.timer_id)

    def update_timer(self):
        if self.timer_running:
            if self.remaining_time.total_seconds() > 0:
                mouse_moved = function.is_mouse_moving()
                if mouse_moved:
                    self.remaining_time = time.timedelta(seconds=self.duration_sec)
                
                self.mouse_moving = mouse_moved  # Update the flag based on mouse movement
                
                self.remaining_time -= time.timedelta(seconds=1)
                self.timer_label.configure(text=str(self.remaining_time))
                
                current_time = self.remaining_time.total_seconds()  # Extract total seconds
                total_time = self.duration_sec  # Assuming duration_sec is the total duration

                percentage = function.progress_percentage(current_time, total_time)
                self.timer_bar.set(percentage)
                
                self.timer_id = self.after(1000, self.update_timer)
            else:
                self.timer_running = False
                mode_choice = app.mode_select.get()
                if mode_choice == "Move":
                    function.mouse_move()
                if mode_choice == "Click":
                    function.mouse_click()
                
                self.start_timer()

app = App()

# pywinstyles.apply_style(app, "acrylic")
app.mainloop()