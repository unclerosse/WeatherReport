import requests 

def GetWeather(City):
	Answ = []

	__KEY = '1cbf87fcd8292f2f9a9f7ee9c0c1aeea'
	GeoUrl = 'http://api.openweathermap.org/geo/1.0/direct?q=+' + City +'&appid=' + __KEY
	Result = requests.get (GeoUrl)
	lt = str (Result.json () [0]['lat'])
	ln = str (Result.json () [0]['lon'])
	Answ.append (Result.json () [0]['local_names']['ru'])
	
	URL = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + lt + '&lon=' + ln + '&exclude=minutely,hourly,alerts&appid=' + __KEY + '&units=metric&lang=ru'
	Result = requests.get (URL)
	
	Answ.append (Result.json ())
	return Answ 