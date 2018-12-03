#!/usr/bin/python3
"""Weather app project.
"""

import html
from urllib.request import urlopen, Request

ACCU_URL = ("https://www.accuweather.com/uk/ua/dniprodzerzhynsk/322726/weather-"
           "forecast/322726")

RP5_URL = ("http://rp5.ua/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9A%D"
	       "0%B0%D0%BC'%D1%8F%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D0%BC%D1%83_(%D0%94"
	       "%D0%BD%D1%96%D0%BF%D1%80%D0%BE%D0%B4%D0%B7%D0%B5%D1%80%D0%B6%D0%B8%"
	       "D0%BD%D1%81%D1%8C%D0%BA%D1%83)")

SINOPTIK_URL = ("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%"
	            "D0%BA%D0%B0%D0%BC'%D1%8F%D0%BD%D1%81%D1%8C%D0%BA%D0%B5"
	            "-303007130")


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