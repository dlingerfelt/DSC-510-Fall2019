# File : DSC510_Safari_WeatherReporter.py
# Name: Edris Safari
# Date:11/06/2019
# Course: DSC510 - Introduction To Programming
# Desc:
# This program uses web services to obtain current weather information from https://api.openweathermap.org
# The key 'f985b93ed77c52ad1dc90147bb8aa29e' was obtained from open weather map to facilitate the communication.
# This program implements a REST get from the open weather web service API. It then parses weather information from
# the reply. The program presents a GUI from which the user enters city name, city name and a country separated by
# comma(i.e Paris, Fr.) or a zip code. A button named 'search' is provided to allow the user to submit the query.
# Invalid zip codes or cities will result in "City not found" reply which is an acutal reply from the API. Any error
# code returned by open weather API will be displayed. If the entry is valid, the current temperature, Current
# condition,current pressure, humidity and min/max temperature will be displayed. An icon showing the weather condition
# is displayed. The icons were uploaded from the open weather map API 'https://openweathermap.org/img/w/'. There are 9
# icons for day and 9 icons for night. Each icon represents conditions such as partly cloudy with drizzle, with a cloud
# and droplets of rain underneath, sunny with a orange sun, etc. If time of day is after dark, the night icons are
# displayed and the day icons otherwise.
#
# NOTE:
# Please make sure python and all modules used in this program are installed and supporting software for running
# python programs are properly installed and functional.
#
# Usage:
# Execute this program from the command line by entering 'py DSC510_Safari_WeatherReporter.py'

import tkinter as tk
import requests
from PIL import Image, ImageTk
import zipcodes

HEIGHT = 500
WIDTH = 600
open_weather_url = "https://api.openweathermap.org/data/2.5/weather"


class MainApplication(tk.Frame):
    # The main class contains the attributes and methods needed to run the weather report.

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        parent.title("Get Current Weather information for any city or zip code")

        def is_valid_zip_code(zip_code):
            # This function validates the the zip code. The The module 'zipcodes' returns a structure for the zip
            # code given. If the zip code is valid the structure is as shown below:
            # <class 'list'>: [{'zip_code': '78133', 'zip_code_type': 'STANDARD', 'city': 'CANYON LAKE', 'state': 'TX',
            # 'lat': 29.87, 'long': -98.26, 'world_region': 'NA', 'country': 'US', 'active': True}]
            # The structure is an empty list if the zip code is invalid.
            # NOTE: zipcodes module ignores the 4-digit zip code extension
            # Example of valid patterns : 78133, 78133-3212
            # If user enters invalid zipcode or a city name, this function returns False
            result = False
            try:
                result = zipcodes.matching(zip_code)
                if result.__len__() > 0:
                    result = True
                else:
                    result = False  # zip code entered is invalid(e.g. 123456789) or is not in the US
            except:
                print("Error matching zip code.")  # user has entered alphanumeric value

            return result

        def format_weather_report(weather_report_json):
            # This function extracts the data from weather report sent back from open weather and constructs the report
            # in an organized fashion. It returns final_str which contains the weather report with line separated items.
            # This function is called by 'get_a_report'
            try:
                city = weather_report_json['name']
                country = weather_report_json['sys']['country']
                current_condition = weather_report_json['weather'][0]['description']
                current_temperature = weather_report_json['main']['temp']
                pressure = weather_report_json['main']['pressure']
                humidity = weather_report_json['main']['humidity']
                temp_min = weather_report_json['main']['temp_min']
                temp_max = weather_report_json['main']['temp_max']
                final_str = 'Weather in  %s, %s' % (city, country)
                final_str += '\n\n'
                final_str += '\nCurrent temperature: %s °F' % current_temperature
                final_str += '\nCurrent conditions: %s' % current_condition
                final_str += '\nPressure: %s hpa' % pressure
                final_str += '\nHumidity: %s %%' % humidity
                final_str += '\nMin temp: %s °F' % temp_min
                final_str += '\nMax temp: %s °F' % temp_max
            except IOError:
                final_str = 'There was a problem retrieving weather information.'
            return final_str

        def get_a_report(zip_code_or_city):
            # This function connects to the open weather API and executes its get method.
            # The weather_report is converted to JSON and the values listed in method 'format_weather_report'
            # are retrieved.This function is called by main.
            try:
                # In the conditions below, if zip code is deemed invalid or not found, we will use the city API
                # which may still return valid reply for even the zip code.
                # For example zip code 9000 is found invalid by zipcodes module, but the city API
                # returned Mullhouse, FR
                if is_valid_zip_code(zip_code_or_city):
                    querystring = {"zip": zip_code_or_city.split('-')[0], "APPID": "f985b93ed77c52ad1dc90147bb8aa29e",
                                   'units': 'imperial'}
                else:
                    querystring = {"q": zip_code_or_city, "APPID": "f985b93ed77c52ad1dc90147bb8aa29e",
                                   'units': 'imperial'}

                headers = {'cache-control': 'no-cache'}
                weather_report = requests.get(open_weather_url, headers=headers, params=querystring)
                if weather_report.status_code != 200:
                    weather_icon.delete("all")
                    results['text'] = 'Error ' + str(weather_report.json()['cod']) + '\n' + \
                                      weather_report.json()['message']
                else:
                    results['text'] = format_weather_report(weather_report.json())
                    icon_name = weather_report.json()['weather'][0]['icon']
                    # the icon name refers to a png file that has been uploaded from open_weather
                    display_condition_icon(icon_name)
            except EnvironmentError:
                results['text'] = 'Exception connecting to open_weather_url API!!'

        def display_condition_icon(icon):
            # This function places the given icon in the text box where the weather information is displayed.
            # The corresponding icon shows the weather condition and is pasted on the top-right corner of the text box.
            # The weather_icn widget is the container of this icon.
            # This function is called by get_a_report
            size = int(lower_frame.winfo_height() * 0.25)
            # load the icon file from img folder
            img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
            # delete any existing icons(from previous report)
            weather_icon.delete("all")
            # create the image
            weather_icon.create_image(0, 0, anchor='nw', image=img)
            # display it
            weather_icon.image = img

        # Create the canvas on the frame of the GUI
        canvas = tk.Canvas(parent, height=HEIGHT, width=WIDTH, bg='yellow')
        canvas.pack()
        # Create a text widget on the canvas.
        # The text widget will contain instruction for the user.
        canvas_id = canvas.create_text(80, 20, fill="darkblue", font="Times 15 italic bold", anchor="nw")
        canvas.itemconfig(canvas_id, text="Enter city name or a 5-digit zip code")
        canvas.insert(canvas_id, 12, "")

        # Create and place a frame for the user data entry area
        get_report_frame = tk.Frame(parent, bg='#42c2f4', bd=5)
        get_report_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        # Create and lace a text box for user to enter city or zip
        get_report_textbox = tk.Entry(get_report_frame, font=40)
        get_report_textbox.place(relwidth=0.65, relheight=1)

        # Create a button to click when user wants to see weather report and entering zip or city
        # When user clicks this button the content of the text box are retrieved by get_report_textbox.get().
        # The method get_a_report takes the value obtained and processes it.
        get_report_button = tk.Button(get_report_frame, text='Search',
                                      font=20, command=lambda: get_a_report(get_report_textbox.get()))
        get_report_button.place(relx=0.7, relheight=1, relwidth=0.3)

        # Create a frame for the the results section
        lower_frame = tk.Frame(parent, bg='#42c2f4', bd=10)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
        results.config(font=40, bg='white')
        results.place(relwidth=1, relheight=1)

        weather_icon = tk.Canvas(results, bg='white', bd=0, highlightthickness=0)
        weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)


def main():
    # Create window
    window = tk.Tk()
    # Instantiating the class MainApplication with the windows will display the main gui and provide
    # the application functions
    MainApplication(window).pack(side="top", fill="both", expand=True)
    # The loop keeps the window up until explicitly exited
    window.mainloop()


if __name__ == "__main__":
    main()
else:
    print("This Module's name is :" + __name__)
