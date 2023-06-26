import tkinter as tk
import pyautogui
import win32clipboard
from io import BytesIO
from PIL import Image, ImageDraw, ImageTk, ImageGrab

def start_drawing(event):
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

def take_screenshot():
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas_width
    y1 = y + canvas_height

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

def main():
    # Take screenshot
    screenshot = pyautogui.screenshot()

    # Variables
    tool = "Brush"
    canvas_width = screenshot.size[0] - 160
    canvas_height = screenshot.size[1] - 90

    # Resize the screenshot
    screenshot.thumbnail((canvas_width, canvas_height))

    # -loop-
    root = tk.Tk()

    root.title('Screenshot (╯°□°）╯︵ ┻━┻')
    root.geometry(f'{canvas_width + 5}x{canvas_height + 30}')
    root.resizable(width=False, height=False)

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height,)
    canvas.pack()

    screenshot = ImageTk.PhotoImage(screenshot)
    image_item = canvas.create_image(0, 0, anchor="nw", image=screenshot)


    # Button
    btn_brush = tk.Button(root, text="Brush", command=lambda : change_tool("Brush"))
    btn_brush.pack(side='left')

    btn_cut = tk.Button(root, text="Cut", command=lambda : change_tool("Cut"))
    btn_cut.pack(side="left")

    btn_save = tk.Button(root, text="Save", command=save_screenshot)
    btn_save.pack(side='right')

    btn_clipboard = tk.Button(root, text="Add to clipboard", command=add_to_clipboard)
    btn_clipboard.pack(side="right")

    # Mouse move event
    canvas.bind("<Button-1>", start_drawing)
    canvas.bind("<B1-Motion>", edit_screenshot)

    root.mainloop()

main()