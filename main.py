from tkinter import Tk

def on_drag_end(event):
    global prev_x, prev_y, drag_threshold_id, change_threshold_id

    # Check if x and y values have changed
    if prev_x != event.x or prev_y != event.y:
        # Update the x and y values
        prev_x = event.x
        prev_y = event.y
        # Cancel any existing threshold check
        if drag_threshold_id is not None:
            root.after_cancel(drag_threshold_id)
        # Schedule a new threshold check after 1 second
        drag_threshold_id = root.after(1000, on_drag_stopped)

        # Cancel any existing change threshold check
        if change_threshold_id is not None:
            root.after_cancel(change_threshold_id)
    else:
        # Cancel any existing change threshold check
        if change_threshold_id is not None:
            root.after_cancel(change_threshold_id)
        # Schedule a new change threshold check after 1 second
        change_threshold_id = root.after(1000, something_else_changed)

def on_drag_stopped():
    global drag_threshold_id
    drag_threshold_id = None  # Reset the threshold identifier
    print("Window dragging has stopped")
    # run some code here once the user stops dragging the window

def something_else_changed(): # This function is called when something else changes. I am not good at naming things alright :/
    global change_threshold_id
    change_threshold_id = None  # Reset the threshold identifier
    print("Something other than x and y values has changed")
    # run some code here once the user stops dragging the window but the x and y values have not changed

root = Tk()
root.geometry("400x100")

# Initialize the previous x and y values
prev_x = 0
prev_y = 0

# Store the ID of the threshold check
drag_threshold_id = None
change_threshold_id = None

# Bind the callback function to the <Configure> event
root.bind('<Configure>', on_drag_end)

root.mainloop()
