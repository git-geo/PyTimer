import tkinter as tk
from time import sleep

win = tk.Tk()

win.geometry("350x300")
win.title("Timer")
win['bg'] = "black"
win.wm_attributes("-alpha", 0.9)
win.resizable(height=False, width=False)
def timer():
    try:
        seconds = int(sec.get())
        minutes = int(min.get())

        min_label.destroy()
        min.destroy()
        sec_label.destroy()
        sec.destroy()
        start_button.destroy()

        time_left_label = tk.Label(win, text="Time left:", fg="lime", bg="black", font="Consolas 20")
        time_left_label.place(x=100, y=50)

        time_left = tk.Label(win, text="", fg="lime", bg="black", font="Consolas 60")
        time_left.place(x=60, y=100)


        seconds = minutes * 60 + seconds

        for i in range(seconds):
            ftime = [str(x) for x in divmod(seconds, 60)]
            rmtime = "0"+ftime[0] if int(ftime[0]) < 10 else ftime[0]
            rstime = "0"+ftime[1] if int(ftime[1]) < 10 else ftime[1]
            rtime = f"{rmtime}:{rstime}"

            time_left.config(text=rtime)
            seconds -= 1
            win.update()
            sleep(1)

        time_left.config(text="00:00", fg="red")
        time_left.place(x=60, y=100)

        time_left_label.config(text="Time has gone!", fg="red")
        time_left_label.place(x=70, y=50)

        win.wm_attributes("-topmost", True)
        print("\a")

    except ValueError:
        pass


min_label = tk.Label(win, text="Minutes: ", font="Consolas 20", fg="lime", bg="black")
min_label.grid(row=0, column=0, padx=50, pady=30)

min = tk.Entry(win, width=5, font="Monospace 15", fg="red")
min.grid(row=0, column=1)

sec_label = tk.Label(win, text="Seconds: ", font="Consolas 20", fg="lime", bg="black")
sec_label.grid(row=1, column=0, padx=50, pady=1)

sec = tk.Entry(win, width=5, font="Monospace 15", fg="red")
sec.grid(row=1, column=1)


start_button = tk.Button(win, text="Start timer", width=12, height=1, font="Consolas 15", bg="white", command=timer)
start_button.place(x=105, y=200)


win.mainloop()
