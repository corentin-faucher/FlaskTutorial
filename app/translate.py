import json
import requests
from flask_babel import _
from app import theapp


def translate(text, source_language, dest_language):
	if 'MS_TRANSLATOR_KEY' not in theapp.config or \
		not theapp.config['MS_TRANSLATOR_KEY']:
		return _('Error: the translator service is not configured.')
	auth = {'Ocp-Apim-Subscription-Key': theapp.config['MS_TRANSLATOR_KEY'] }
	r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
			'/Translate?text={}&from={}&to={}'.format(text, source_language, dest_language), 
			headers=auth)
	if r.status_code != 200:
		return _('Error: the translation service failed.')
	return json.loads(r.content.decode('utf-8-sig'))
