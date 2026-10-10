import tkinter
from main import get_weather_data

window = tkinter.Tk()
window.title("Weather Companion")
window.geometry("700x500")
window.config(bg="#F4F1EA")

title = tkinter.Label(
    window,
    text="Your Weather Companion",
    font=("Arial", 24, "bold"),
    fg="#1F2A44",
    bg="#F4F1EA"
)
title.grid(column=0, row=0, columnspan=3, pady=10)

subtitle = tkinter.Label(
    window,
    text="Check the weather before you workout!",
    font=("Arial", 18, "bold italic"),
    fg="#68645D",
    bg="#F4F1EA"
)
subtitle.grid(column=0, row=1, columnspan=3, pady=10)

check_button = tkinter.Label(
    window,
    text="Check Weather",
    fg="#F4F1EA",
    bg="#1F2A44",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    cursor="hand2"
)
check_button.grid(column=0, row=2, columnspan=3, pady=15)

weather_result = tkinter.Label(
    window,
    text="Your weather will appear here",
    font=("Arial", 15),
    fg="#1F2A44",
    bg="#F4F1EA"
)
weather_result.grid(column=0, row=3, columnspan=3, pady=10)

temperature_label = tkinter.Label(
    window,
    text="Temperature: -- °C",
    font=("Arial", 13),
    fg="#1F2A44",
    bg="#F4F1EA"
)
temperature_label.grid(column=0, row=4, padx=10, pady=10)

wind_label = tkinter.Label(
    window,
    text="Wind: -- km/h",
    font=("Arial", 13),
    fg="#1F2A44",
    bg="#F4F1EA"
)
wind_label.grid(column=1, row=4, padx=10, pady=10)

rain_label = tkinter.Label(
    window,
    text="Rain: -- %",
    font=("Arial", 13),
    fg="#1F2A44",
    bg="#F4F1EA"
)
rain_label.grid(column=2, row=4, padx=10, pady=10)

training_frame = tkinter.Frame(
    window,
    bg="#F4F1EA",
    highlightbackground="#4A8B62",
    highlightthickness=2,
    padx=20,
    pady=10
)
training_frame.grid(column=0, row=5, columnspan=3, pady=20)

check_label = tkinter.Label(
    training_frame,
    text="Check the weather first!",
    font=("Arial", 15, "bold"),
    fg="#1F2A44",
    bg="#F4F1EA"
)
check_label.grid(column=0, row=0)


def check_weather():
    temperature, wind, rain = get_weather_data()

    temperature_label.configure(text=f"Temperature: {temperature} °C")
    wind_label.configure(text=f"Wind: {wind} km/h")
    rain_label.configure(text=f"Rain: {rain} %")

    if temperature > 10 and wind < 30 and rain < 40:
        check_label.configure(text="Go training!")
        training_frame.configure(highlightbackground="#4A8B62")
    else:
        check_label.configure(text="No training today")
        training_frame.configure(highlightbackground="#C0392B")


check_button.bind("<Button-1>", lambda event: check_weather())

window.grid_columnconfigure(0, weight=1, uniform="weather")
window.grid_columnconfigure(1, weight=1, uniform="weather")
window.grid_columnconfigure(2, weight=1, uniform="weather")

window.mainloop()