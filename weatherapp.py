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


RP5_URL = ("http://rp5.ua/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9A%D0%B0%"
		   "D0%BC'%D1%8F%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D0%BC%D1%83_(%D0%94%D0%BD%D1%"
		   "96%D0%BF%D1%80%D0%BE%D0%B4%D0%B7%D0%B5%D1%80%D0%B6%D0%B8%D0%BD%D1%81%D1%"
		   "8C%D0%BA%D1%83)")

rp5_request = Request(RP5_URL, headers=headers)
rp5_page = urlopen(rp5_request).read()
rp5_content = rp5_page.decode('utf-8')

WINFO_CONTAINER_TAG = '<div id="ArchTemp">'
RP5_TEMP_TAG = '<span class="t_0" style="display: block;">'
rp5_temp_tag = rp5_content.find(RP5_TEMP_TAG, rp5_content.find(WINFO_CONTAINER_TAG))
rp5_temp_tag_size = len(RP5_TEMP_TAG)
rp5_temp_tag_start = rp5_temp_tag + rp5_temp_tag_size
rp5_temp = ''
for char in rp5_content[rp5_temp_tag_start:]:
	if char != '<':
		rp5_temp += char
	else:
		break

print('RP5.ua: \n')
print(f'Temperature: {html.unescape(rp5_temp)}\n')


RP5_START_CONDITIONS_TAG = '<div class="ArchiveInfo">'
RP5_CONDITIONS_TAG = 'F</span>,'
rp5_conditions_tag_size = len(RP5_CONDITIONS_TAG)
rp5_conditions_tag_index = rp5_content.find(RP5_CONDITIONS_TAG, rp5_content.find(RP5_START_CONDITIONS_TAG))
rp5_conditions_tag_start = rp5_conditions_tag_index + rp5_conditions_tag_size
rp5_conditions_end_tag = '<span'
rp5_conditions_end_tag_index = rp5_content.find(rp5_conditions_end_tag, rp5_conditions_tag_index)
rp5_conditions = rp5_content[rp5_conditions_tag_start:rp5_conditions_end_tag_index]

print(f'Weather condidtions: {rp5_conditions}\n')