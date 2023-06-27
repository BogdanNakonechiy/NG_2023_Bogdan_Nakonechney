import tkinter as tk
import pyautogui
import win32clipboard
from io import BytesIO
from PIL import Image, ImageDraw, ImageTk, ImageGrab

def start_of_cut(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def change_tool(new_tool):
    global tool
    tool = new_tool

def edit_screenshot(event):
    match tool:
        case "Brush":
            x = event.x
            y = event.y
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")
        case "Cut":
            global end_cut_x, end_cut_y
            canvas.delete("highlight")
            end_cut_x = event.x
            end_cut_y = event.y
            canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="red" ,tags="highlight")

            canvas.bind("<ButtonRelease-1>", end_of_cut)
def end_of_cut(event):
    less_x = min(start_x, end_cut_x)
    less_y = min(start_y, end_cut_y)
    difference_x = abs(start_x - end_cut_x)
    difference_y = abs(start_y - end_cut_y)

    screenshot = take_screenshot().crop((less_x + 1, less_y + 1, less_x + difference_x - 1, less_y + difference_y - 1 ))
    root.destroy()
    new_screenshot(screenshot)

def take_screenshot():
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + screenshot.size[0]
    y1 = y + screenshot.size[1]

    return ImageGrab.grab().crop((x, y, x1, y1))

def save_screenshot():
    take_screenshot().save("new_screenshot.png")

def add_to_clipboard():
    image = take_screenshot()
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def new_screenshot(screenshot):
    # Variables
    global canvas, root, tool

    root = tk.Tk()

    root.title('Screenshot (╯°□°）╯︵ ┻━┻')
    root.geometry(f'{screenshot.size[0]}x{screenshot.size[1] + 30}')
    root.resizable(width=False, height=False)

    canvas = tk.Canvas(root, width=screenshot.size[0], height=screenshot.size[1])
    canvas.pack()

    screenshot = ImageTk.PhotoImage(screenshot)
    image_item = canvas.create_image(0, 0, anchor="nw", image=screenshot)

    # Mouse event
    canvas.bind("<ButtonPress-1>", start_of_cut)
    canvas.bind("<B1-Motion>", edit_screenshot)

    # Button
    btn_brush = tk.Button(root, text="Brush", command=lambda: change_tool("Brush"))
    btn_brush.pack(side='left')

    btn_cut = tk.Button(root, text="Cut", command=lambda: change_tool("Cut"))
    btn_cut.pack(side="left")

    btn_save = tk.Button(root, text="Save", command=save_screenshot)
    btn_save.pack(side='right')

    btn_clipboard = tk.Button(root, text="Add to clipboard", command=add_to_clipboard)
    btn_clipboard.pack(side="right")

    root.mainloop()

# Take screenshot
screenshot = pyautogui.screenshot()

tool = "Brush"

# Resize the screenshot
screenshot.thumbnail((screenshot.size[0] - 160, screenshot.size[1] - 90))

new_screenshot(screenshot)