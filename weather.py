import tkinter as tk
import requests
import time



userUnitPreference = str(input("Do you prefer Imperial or Metric? "))



def getWeatherMetric(canvas):


    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city + "&units=Metric&APPID=3cc7707b3b9fea8605f38b46a28e6ee5"
    json_data = requests.get(api).json()

    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']) 
    min_temp = int(json_data['main']['temp_min']) 
    max_temp = int(json_data['main']['temp_max']) 
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']

    wind = json_data['wind']['speed']

    # sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    # sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "mb" + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Wind Speed: " + str(wind) + "mph" + "\n"

    label1.config(text = final_info)
    label2.config(text = final_data)




def getWeatherImperial(canvas):


    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&units=Imperial&APPID=3cc7707b3b9fea8605f38b46a28e6ee5"
    json_data = requests.get(api).json()

    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']) 
    min_temp = int(json_data['main']['temp_min']) 
    max_temp = int(json_data['main']['temp_max']) 
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']

    wind = json_data['wind']['speed']

    # sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    # sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + "\n" + str(temp) + "°F"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "°F" + "\n" + "Min Temp: " + str(min_temp) + "°F" + "\n" + "Pressure: " + str(pressure) + "mb" + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Wind Speed: " + str(wind) + "kmph" + "\n"

    label1.config(text = final_info)
    label2.config(text = final_data)
    


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Beginner Weather Application")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
# Allow the user to type the city name directly without moving the cursor:
textfield.focus()
# Create 2 labels to show the physical data:
if userUnitPreference == "Imperial":
    textfield.bind('<Return>', getWeatherImperial)
elif userUnitPreference == "Metric":
    textfield.bind('<Return>', getWeatherMetric)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()


