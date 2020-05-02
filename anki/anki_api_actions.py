from anki.anki_api_actions_abstract import AnkiApiAbstract


class AnkiApiCommonActions(AnkiApiAbstract):
    """
    Class with common API actions including "modelFieldNames"
    """
    def choice_method(self, user_action: str, template: dict = None) -> dict:
        """
        Select method by user_action
        :param user_action: Action from user
        :param template: template to send to Anki
        :return: response from Anki
        """
        if user_action == 'get_front_and_back_field_names':
            response = self.get_front_and_back_field_names()
        else:
            response = None
        return response

    def get_front_and_back_field_names(self) -> dict:
        """
        Get front and back fields from model Anki
        :return: dict with {front, back}
        """
        data_to_add = {
            'modelName': self.anki_center.settings.anki_model_name
        }
        response = self.sender.request(action='modelFieldNames', params=data_to_add)

        result = response.get('result')
        if result is not None:
            model_field_names = {
                'front': result[0],
                'back': result[1],
            }
        else:
            raise Exception('Cant parse result with model fields name')
        return model_field_names


class AnkiApiAddNote(AnkiApiAbstract):
    """
    Class to process "addNote" API actions
    """

    def choice_method(self, user_action: str, template: dict = None) -> dict:
        """
        Select method by user_action
        :param user_action: Action from user
        :param template: template to send to Anki
        :return: response from Anki
        """
        if user_action == 'create_one_note':
            response = self.create_one_note(template)
        else:
            response = None
        return response

    def create_one_note(self, template: dict) -> dict:
        """
        Create new one note
        :param template: template from response
        :return: response from Anki
        """
        model_fields = self.anki_center.anki_action(user_action='get_front_and_back_field_names')

        data_to_add = {
            'note': {
                'deckName': self.anki_center.settings.anki_deck_name,
                'modelName': self.anki_center.settings.anki_model_name,
                'fields': {
                    model_fields.get('front'): template.get('front'),
                    model_fields.get('back'): template.get('back')
                },
                'options': {
                    'allowDuplicate': False
                },
                'tags': []
            }
        }

        response = self.sender.request(action='addNote', params=data_to_add)
        return response
