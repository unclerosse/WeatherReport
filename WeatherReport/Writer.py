#скрипт, который будет записывать данные о погоде в weather_cache.txt

from os import curdir
from ApiParser import GetWeather 
from datetime import datetime

def MathRound (i):
    i = int (i + (0.5 if i > 0 else -0.5))
    return i    

def Sort (js):
	WR = js [0] + '\n\n'
	Current = js [1]['current']
	Time = datetime.utcfromtimestamp (Current ['dt']).strftime ('%d.%m.%Y %H:%M')
	Temp = 'Погода на ' + Time + '\nТемпература: ' + str (MathRound (Current ['temp'])) + '°C\n'
	Feels = 'По ощущениям: ' + str (MathRound (Current ['feels_like'])) + '°C\n'
	Water = 'Влажность: ' + str (Current ['humidity']) + '%\n'
	Wind = 'Скорость ветра: ' + str (MathRound (Current ['wind_speed'])) + ' м/c\n'
	Description = Current ['weather'][0]['description'] + '\n\n'
	WR += Temp + Feels + Water + Wind + Description.capitalize ()

	for i in range (8):
		Daily = js [1]['daily'][i]
		Time = datetime.utcfromtimestamp (Daily ['dt']).strftime ('%d.%m.%Y')
		Temp = 'Погода на ' + Time + '\nДнём: ' + str (MathRound (Daily ['temp']['day'])) + '°C\nНочью: ' + str (MathRound (Daily ['temp']['night'])) + '°C\n'
		Water = 'Влажность: ' + str (Daily ['humidity']) + '%\n'
		Wind = 'Скорость ветра: ' + str (MathRound (Daily ['wind_speed'])) + ' м/c\n'
		Description = Daily ['weather'][0]['description'] + '\n\n'
	
		WR += Temp + Water + Wind + Description.capitalize ()
	return WR

#основной алгоритм записи
def WriteOnFile (City):
	Cache = open (r"__pycache__/weather_cache.txt", "w") #открываем кэш-файл
	Cache.write (Sort (GetWeather (City)))

if __name__ == "__main__":
	WriteOnFile ("москва")
	print ('done.')
	input ()
