import requests
from selectorlib import Extractor

class Temperature:
    """Temperature holds information of country and city and finds temperature
    using these parameters"""
    yaml_dir = 'calorie_back/temperature.yaml'
    temp_url = "https://www.timeanddate.com/weather/"

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def _build_url(self):
        return requests.get(self.temp_url + self.country + "/" + self.city)

    def get(self):
        """Method that gets temperature based on country and city"""
        weather_url = self._build_url()
        ext = Extractor.from_yaml_file(self.yaml_dir)
        page_info_text = weather_url.text
        temperature_info = ext.extract(page_info_text)
        temperature_num = float(temperature_info['temper'].replace("\xa0°C", ""))
        return temperature_num


