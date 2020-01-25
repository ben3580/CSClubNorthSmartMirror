import requests, json

class GetWeather:

    def __init__(self, city):
        self.city = city

    def get_info(self, city):
        # API key
        self.api_key = "611454210432c7064822cbcbe7dc14d7"
  
        # base_url variable to store url 
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
          
        # complete_url variable to store complete url address 
        self.complete_url = self.base_url + "appid=" + self.api_key + "&q=" +\
                            self.city 
          
        # get method of requests module return response object 
        self.response = requests.get(self.complete_url) 
          
        # json method of response object. Convert json format data into 
        # python format data 
        self.x = self.response.json()


        if self.x["cod"] != "404": # If the website does not give a 404 error
            # The website returns all the information in one big list, which
            # contains many smaller lists
            # I extract all the  wanted information from the list and return it
            # as a list
            
            # Extracts the "description" information from the "weather" list
            self.weather_list = self.x["weather"]
            self.weather_index_0 = self.weather_list[0]
            self.description = self.weather_index_0["description"]
            
            # Extracts the "temperature" and "feels_like"
            # information from the "main" list
            self.main_list = self.x["main"]
            self.temperature_k = self.main_list["temp"]
            self.feels_like_k = self.main_list["feels_like"]
            # Converts temperature from Kelvin to Fahrenheit
            self.temperature_f = round(1.8 * (self.temperature_k - 273) + 32)
            self.feels_like_f = round(1.8 * (self.feels_like_k - 273) + 32)
            
            # Extracts the "speed" information from the "wind" list
            self.wind_list = self.x["wind"]
            self.wind_speed_m = self.wind_list["speed"]
            # Converts wind speed from m/s to mph
            self.wind_speed_mi = round(self.wind_speed_m * 2.23693629)
            # Returns only the information we want
            return self.description, self.temperature_f, self.feels_like_f,\
                   self.wind_speed_mi
        else: 
            return "City Not Found"

# What you'll have to write in the main program
city_name = input("Enter city name : ")

get_weather = GetWeather(city_name) # Instantiate GetWeather object

info_we_want = get_weather.get_info(city_name) # Get the information

print(info_we_want)

