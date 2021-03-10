from django.core.management import BaseCommand

from forecast.models import Forecasts

import requests
import json

from datetime import datetime, date
import pytz

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "My test command"

    # A command must define handle()
    def handle(self, *args, **options):

        headers = {
	        'X-AjaxPro-Method': 'GetCurrentOne',
	    }
        payload = {
	        "cityId":"77107",
	    }
        url = 'http://weather.news24.com/ajaxpro/Weather.Code.Ajax,Weather.ashx'
	
        response = requests.post(url, headers=headers,
		                 data=json.dumps(payload))
        response.raise_for_status()
	    #date , min temp , max temp , wind and rain

        resp = response.json()

        date_resp_arr = resp["value"]["LocalUpdateTime"].split(' ')
        date_resp_arr = date_resp_arr[:len(date_resp_arr)-1]
        date_resp_arr_str = ' '.join(date_resp_arr)

        timezone = pytz.timezone("Africa/Johannesburg")

	    #Thu, 07 Jun 2018 20:42:09 SAST
        datetime_object = datetime.strptime(date_resp_arr_str, '%a, %d %b %Y %H:%M:%S')
        datetime_object_aware = timezone.localize(datetime_object)

        
        temp_low = int(resp["value"]["Forecast"]["LowTemp"])
        temp_high = int(resp["value"]["Forecast"]["HighTemp"])
        precipitationProbability = int(resp["value"]["Forecast"]["PrecipitationProbability"])
        windSpeed = int(resp["value"]["Forecast"]["WindSpeed"])
        
        findObj = Forecasts.objects.filter(date=datetime_object_aware, min_temp=temp_low,max_temp=temp_high,wind_speed=windSpeed, rain_probability=precipitationProbability ).exists()

        if (not findObj):
            p = Forecasts(date=datetime_object_aware, min_temp=temp_low,max_temp=temp_high,wind_speed=windSpeed, rain_probability=precipitationProbability )
            p.save()
        else:
            self.stdout.write("got that data!")

        self.stdout.write("successful?")












