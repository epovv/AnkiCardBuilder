from anki.anki_interact import AnkiApiCenter
from anki_card_template.create_templates_center import CreateTemplateCenter
from settings.settings import Settings
from translator.yandex_translator import YandexTranslator


class MainDispatcher:

    def __init__(self, setting: Settings):
        self.settings = setting
        self.anki_api_center = AnkiApiCenter(settings=settings)
        self.template_center = CreateTemplateCenter(settings=settings)

    def dispatch(self, text_to_translate: str):
        """
        Main point
        :param text_to_translate: text for sending to translate
        """
        template = self.create_template(text_to_translate)
        response_from_anki = self.anki_api_center.anki_action(user_action=settings.user_action, template=template)

        self.response_message(response_from_anki)

    def create_template(self, text_to_translate: str) -> dict:
        """
        Chose template creator by usage api
        :param text_to_translate: text for sending to translate
        :return: template dict
        """
        if self.settings.usage_api == 'YANDEX':
            response_from_api = YandexTranslator(self.settings).get_response(text_to_translate)
            template = self.template_center.yandex_make_template(response_from_api)
        else:
            template = None
        return template

    @staticmethod
    def response_message(response_from_anki):
        """
        Write message to console according to response from Anki server
        :param response_from_anki: response from Anki server
        """
        if response_from_anki is not None:
            result = response_from_anki.get('result')
            error = response_from_anki.get('error')

            if result is not None:
                print(f'Card {result} was created')
            else:
                print(f'An error occurred: {error}')
        else:
            print('Bad response')


if __name__ == '__main__':

    settings = Settings()
    with open('config.txt', 'r') as f:
        for line in f:
            new_line = line.strip().split('=')
            if new_line[0] == 'api_key':
                settings.api_key = new_line[1]
            elif new_line[0] == 'lang_from':
                settings.lang_from = new_line[1]
            elif new_line[0] == 'lang_to':
                settings.lang_to = new_line[1]
            elif new_line[0] == 'anki_model_name':
                settings.anki_model_name = new_line[1]
            elif new_line[0] == 'anki_deck_name':
                settings.anki_deck_name = new_line[1]
            elif new_line[0] == 'anki_host':
                settings.anki_host = new_line[1]

    while True:
        try:
            text_to_translate = input('Input word to translate: ')
            user_action = 'create_one_note'

            settings.user_action = user_action
            MainDispatcher(settings).dispatch(text_to_translate)
        except Exception as e:
            print(e)
            pass
