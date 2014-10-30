#!/usr/bin/python3
# -*- coding: utf8 -*-
# smssend - smssend is a program to send SMS messages class for python3/2.7.

# Copyright © 2009-2014 by Sergey Denisov aka 'LittleBuster', Denis Khabarov aka 'Saymon21'
# E-Mail: DenisovS21 at gmail dor com (DenisovS21@gmail.com)
# E-Mail: saymon at hub21 dot ru (saymon@hub21.ru)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3
# as published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import json
from os import getenv
from urllib import quote
from urllib2 import urlopen, URLError

__author__ = "Sergey 'LittleBuster' Denisov"
__copyright__ = "Copyright © 2014 Denis 'Saymon21' Khabarov, Sergey 'LittleBuster' Denisov"
__credits__ = []
__license__ = "GPLv3"
__version__ = "0.4.1"
__maintainer__ = "Sergey 'LittleBuster' Denisov"
__email__ = "DenisovS21@gmail.com"
__status__ = "Complete"


SMS_CODES = {
	100:"Сообщение принято к отправке.",
	200:"Неправильный api_id",
	201:"Не хватает средств на лицевом счету",
	202:"Неправильно указан получатель",
	203:"Нет текста сообщения",
	204:"Имя отправителя не согласовано с администрацией",
	205:"Сообщение слишком длинное (превышает 8 СМС)",
	206:"Будет превышен или уже превышен дневной лимит на отправку сообщений",
	207:"На этот номер (или один из номеров) нельзя отправлять сообщения, либо указано более 100 номеров в списке получателей",
	208:"Параметр time указан неправильно",
	209:"Вы добавили этот номер (или один из номеров) в стоп-лист",
	210:"Используется GET, где необходимо использовать POST",
	211:"Метод не найден",
	220:"Сервис временно недоступен, попробуйте чуть позже.",
	300:"Неправильный token (возможно истек срок действия, либо ваш IP изменился)",
	301:"Неправильный пароль, либо пользователь не найден",
	302:"Пользователь авторизован, но аккаунт не подтвержден (пользователь не ввел код, присланный в регистрационной смс)",
}

class SMSSender(object):
	"""
	Simple class for send SMS using sms.ru
	"""
	def send_from_cfg(self, text, config_file=None):
		"""
		Load sms configs from local config file in json format
		"""
		if config_file == None:
			config_file = "sms.cfg"

		f = open(config_file, "rt")
		cfg = json.load(f)
		f.close()

		self.url = "http://sms.ru/sms/send?api_id=%s&to=%s&text=%s" % (cfg["SMSSend"]["api_id"], 
																	   cfg["SMSSend"]["phone"],
																	   quote(text))
		if not cfg["SMSSend"]["from"] == "":
			selff.url += "&from=%s" % (cfg["SMSSend"]["from"])
		if cfg["SMSSend"]["translit"] == 1:
			self.url += "%&translit=1"
		self._send_sms(cfg["SMSSend"]["time_delay"])

	def send(self, api_id, to, text, from_m=None, translit=None, time_delay=None):
		"""
		Sending message using params
		"""
		self.url = "http://sms.ru/sms/send?api_id=%s&to=%s&text=%s" % (api_id, to, quote(text))

		if from_m:
			selff.url += "&from=%s" % (from_m)
		if translit == True:
			self.url += "%&translit=1"
		self._send_sms(time_delay)

	def _send_sms(self, time_delay):
		"""
		Connect to sms.ru web server
		"""
		try:
			if time_delay == None:
				time_delay = 10
			res = urlopen(self.url, timeout=time_delay)
		except URLError as errstr:
			return 2

		service_result=res.read().splitlines()
		if service_result is not None and int(service_result[0]) == 100:
			return 0
		if service_result is not None and int(service_result[0]) != 100:
			"""
			Result is fail, return error code
			"""
			return int(service_result[0])