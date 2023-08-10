import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Indian Flag")
window.geometry("600x400")

# Create the canvas
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

# Draw the background color
canvas.create_rectangle(0, 0, 600, 400, fill="cyan")

# Draw the Ashoka Chakra (the blue circular emblem)
canvas.create_oval(250, 150, 350, 250, fill="navy", outline="navy")

# Draw 24 spokes of the Ashoka Chakra
for i in range(0, 360, 15):
    canvas.create_line(300, 200, 300 + 80 * (i % 30 < 15),
                       200 + 80 * (i % 30 < 15), width=1, fill="white")

# Draw the three stripes
canvas.create_rectangle(50, 100, 550, 200, fill="orange", outline="")
canvas.create_rectangle(50, 200, 550, 300, fill="white", outline="")
canvas.create_rectangle(50, 300, 550, 400, fill="green", outline="")

# Draw the topmost stripe (saffron) with rounded corners
canvas.create_arc(50, 100, 550, 200, start=180, extent=-180,
                  style=tk.ARC, width=0, fill="#FF9933")

# Draw the bottom stripe (green) with rounded corners
canvas.create_arc(50, 300, 550, 400, start=0, extent=180,
                  style=tk.ARC, width=0, fill="#138808")

# Start the main event loop
window.mainloop()
