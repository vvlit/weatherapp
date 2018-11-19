#!/usr/bin/python3

"""Weather app project.
"""

import html
from urllib.request import urlopen, Request

ACCU_URL = "https://www.accuweather.com/uk/ua/dniprodzerzhynsk/322726/weather-forecast/322726"

# getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}
accu_request = Request(ACCU_URL, headers=headers)
accu_page = urlopen(accu_request).read()
accu_page = accu_page.decode('utf-8')

ACCU_TEMP_TAG = '<span class="large-temp">'
accu_temp_tag_size = len(ACCU_TEMP_TAG)
accu_temp_tag_index = accu_page.find(ACCU_TEMP_TAG)
accu_temp_value_start = accu_temp_tag_index + accu_temp_tag_size
accu_temp = ''
for char in accu_page[accu_temp_value_start:]:
	if char != '<':
		accu_temp += char
	else:
		break

print('AccuWeather: \n')
print(f'Temperature: {html.unescape(accu_temp)}\n')

# Getting weather condidtions
accu_cond_tag = '<span class="cond">'
accu_cond_tag_size = len(accu_cond_tag)
accu_cond_tag_index = accu_page.find(accu_cond_tag)
accu_cond_value_start = accu_cond_tag_index + accu_cond_tag_size
accu_cond = ''
for char in accu_page[accu_cond_value_start:]:
	if char != '<':
		accu_cond += char
	else:
		break

print(f'Weather condidtions: {accu_cond}\n')