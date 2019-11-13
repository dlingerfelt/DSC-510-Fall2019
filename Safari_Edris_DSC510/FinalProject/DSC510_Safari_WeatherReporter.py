import tkinter as tk
import requests
from PIL import Image, ImageTk
import zipcodes

HEIGHT = 500
WIDTH = 600


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        parent.title("Get Current Weather information for any city or zip code")

        def is_valid_zip_code(zip_code):
            # This function validates the pattern of the zip code. The regular expression below
            # returns valid for five digit value as well as five digits with hyphen followed by four or 5 digits.:
            # Example of valid patterns : 78133, 78133-3212
            # Example pf invalid patterns: Los Angels, 8976541,87676-123456
            result = False
            try:
                result = zipcodes.matching(zip_code.split('-')[0])
                if result.__len__() > 0:
                    result = True
                else:
                    result = False
            except:
                print("Error matching zip code.")

            return result

        def format_weather_report(weather_report_json):
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
            # The weather_report is converted to JSON and the following values are retrieved
            # This function is called by main.
            open_weather_url = "https://api.openweathermap.org/data/2.5/weather"
            try:
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
                    results['text'] = weather_report.json()['message'] + '\\n' + \
                                      str(weather_report.status_code) + '\\n' + ': Error connecting to API'
                else:
                    results['text'] = format_weather_report(weather_report.json())
                    icon_name = weather_report.json()['weather'][0]['icon']
                    # the icon name refers to a png file that has been uploaded from open_weather
                    display_condition_icon(icon_name)
            except EnvironmentError:
                results['text'] = 'Exception connecting to open_weather_url API!!'

        def display_condition_icon(icon):
            size = int(lower_frame.winfo_height() * 0.25)
            # load the icon file from img folder
            img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
            # delete any existing icons(from previous report)
            weather_icon.delete("all")
            # create the image
            weather_icon.create_image(0, 0, anchor='nw', image=img)
            # display it
            weather_icon.image = img

        canvas = tk.Canvas(parent, height=HEIGHT, width=WIDTH, bg='yellow')
        canvas.pack()
        canvas_id = canvas.create_text(80, 20, fill="darkblue", font="Times 15 italic bold", anchor="nw")
        canvas.itemconfig(canvas_id, text="Enter city name or a 5-digit zip code")
        canvas.insert(canvas_id, 12, "")

        get_report_frame = tk.Frame(parent, bg='#42c2f4', bd=5)
        get_report_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        get_report_textbox = tk.Entry(get_report_frame, font=40)
        get_report_textbox.place(relwidth=0.65, relheight=1)

        get_report_button = tk.Button(get_report_frame, text='Search',
                                      font=20, command=lambda: get_a_report(get_report_textbox.get()))
        get_report_button.place(relx=0.7, relheight=1, relwidth=0.3)

        lower_frame = tk.Frame(parent, bg='#42c2f4', bd=10)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        bg_color = 'white'
        results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
        results.config(font=40, bg=bg_color)
        results.place(relwidth=1, relheight=1)

        weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
        weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)


if __name__ == "__main__":
    window = tk.Tk()
    MainApplication(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
