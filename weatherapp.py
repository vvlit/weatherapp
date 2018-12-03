#!/usr/bin/python3

"""Weather app project.
"""

import html
from urllib.request import urlopen, Request



# Getting information from accuweather.com
ACCU_URL = "https://www.accuweather.com/uk/ua/dniprodzerzhynsk/322726/weather-forecast/322726"

# getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}
accu_request = Request(ACCU_URL, headers=headers)
accu_page = urlopen(accu_request).read()
accu_page = accu_page.decode('utf-8')

# Getting temperature from accuweather.com
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

# Getting weather condidtions from accuweather.com
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



# Getting information from rp5.ua
RP5_URL = ("http://rp5.ua/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9A%D0%B0%"
		   "D0%BC'%D1%8F%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D0%BC%D1%83_(%D0%94%D0%BD%D1%"
		   "96%D0%BF%D1%80%D0%BE%D0%B4%D0%B7%D0%B5%D1%80%D0%B6%D0%B8%D0%BD%D1%81%D1%"
		   "8C%D0%BA%D1%83)")

# getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}
rp5_request = Request(RP5_URL, headers=headers)
rp5_page = urlopen(rp5_request).read()
rp5_content = rp5_page.decode('utf-8')

# Getting temperature from rp5.ua
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

# Getting weather condidtions from rp5.ua
RP5_START_CONDITIONS_TAG = '<div class="ArchiveInfo"'
RP5_CONDITIONS_TAG = 'F</span>,'
rp5_conditions_tag_size = len(RP5_CONDITIONS_TAG)
rp5_conditions_tag_index = rp5_content.find(RP5_CONDITIONS_TAG, rp5_content.find(RP5_START_CONDITIONS_TAG))
rp5_conditions_tag_start = rp5_conditions_tag_index + rp5_conditions_tag_size
rp5_conditions_end_tag = '<'
rp5_conditions_end_tag_index = rp5_content.find(rp5_conditions_end_tag, rp5_conditions_tag_start)
rp5_conditions = rp5_content[rp5_conditions_tag_start:rp5_conditions_end_tag_index]

print(f'Weather condidtions: {rp5_conditions}\n')



# Getting information from sinoptik.ua
SINOPTIK_URL = ("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B0%D0%"
				"BC'%D1%8F%D0%BD%D1%81%D1%8C%D0%BA%D0%B5-303007130")

# getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}
sinoptik_request = Request(SINOPTIK_URL, headers=headers)
sinoptik_page = urlopen(sinoptik_request).read()
sinoptik_content = sinoptik_page.decode('utf-8')

# Getting temperature from sinoptik.ua
SINOPTIK_CONTAINER_TAG = ''
SINOPTIK_TEMP_TAG = '<p class="today-temp">'
sinoptik_temp_tag_index = sinoptik_content.find(SINOPTIK_TEMP_TAG)
sinoptik_temp_tag_size = len(SINOPTIK_TEMP_TAG)
sinoptik_temp_tag_start = sinoptik_temp_tag_index + sinoptik_temp_tag_size
sinoptik_temp_end_tag = '<'
sinoptik_temp_end_tag_index = sinoptik_content.find(sinoptik_temp_end_tag, sinoptik_temp_tag_start)
sinoptik_temp = sinoptik_content[sinoptik_temp_tag_start:sinoptik_temp_end_tag_index]

print('sinoptik.ua: \n')
print(f'Temperature: {html.unescape(sinoptik_temp)}\n')


def get_request_headers():
	"""
	"""
	return {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}


def get_page_source(url):
	"""
	"""

	request = Request(url, headers=get_request_headers())
	page_source = urlopen(request).read()
	return page_source.decode('utf-8')


def get_tag_content(page_content, tag):
	"""
	"""

	tag_index = page_content.find(tag)
	tag_size = len(tag)
	value_start = tag_index + tag_size

	content = ''
	for c in page_content[value_start:]:
		if c != '<':
			content += c
		else:
			break
	return content


def get_weather_info(page_content, tags):
	"""
	"""

	return tuple([get_tag_content(page_content, tag) for tag in tags])


def produce_output(provider_name, temp, condition):
	"""
	"""

	print(f'\n {provider_name}:')
	print(f'Temperature: {html.unescape(temp)}\n')
	print(f'Condition: {condition}\n')


def main():
	""" Main entry point.
	"""

	weather_sites = {"AccuWeather": (ACCU_URL, ACCU_TAGS),
	                 "RP5": (RP5_URL, RP5_TAGS)}
	for name in weather_sites:
		url, tags = weather_sites[name]
		content = get_page_source(url)
		temp, condition = get_weather_info(content, tags)
		produce_output(name, temp, condition)


if __name__ == '__main__':
	main()