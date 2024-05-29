import pyautogui

last_mouse_position = None  # Define the variable outside the function

def is_mouse_moving():
    global last_mouse_position  # Declare the variable as global within the function
    current_mouse_position = pyautogui.position()
    
    if last_mouse_position is not None:
        if current_mouse_position != last_mouse_position:
            last_mouse_position = current_mouse_position  # Update the last mouse position
            return True
    
    last_mouse_position = current_mouse_position
    return False

def mouse_move():
    start_x, start_y = pyautogui.position()  # Current mouse position
    pyautogui.move(-20, 0, duration=0.1)  # Move mouse 20px left
    pyautogui.move(40, 0, duration=0.1)  # Move mouse 20px right
    pyautogui.moveTo(start_x, start_y, duration=0.1)  # Move to starting position
    
    # Simulate key presses
    pyautogui.keyDown('shift')
    pyautogui.keyUp('shift')
    
def mouse_click():
    pyautogui.click() # Click the mouse in its current location
    
def progress_percentage(current_time, total_time):
    percentage = ((total_time - current_time) / total_time)
    return percentage
    
    
""" if the name of the file is main.py, then run the code
in this case, it won't run because the file is functions.py 
"""
if __name__ == "__main__":
    mouse_move()
    # mouse_click()

    current_time = 1  # Assuming the current time is 5 seconds
    total_time = 10  # Total duration is 10 seconds
    
    percentage = progress_percentage(current_time, total_time)
    print("Percentage of completion:", percentage)