# Default Settings

# External settings
usage_api = 'YANDEX'
method = 'JSON'

# ANKI
actions = {
    'addNote': ['create_one_note'],
    'modelFieldNames': ['get_front_and_back_field_names']
}


# Settings used by the script
class Settings:

    def __init__(self):
        # API settings
        self.usage_api = usage_api
        self.api_key = None
        self.method = method
        self.lang_from = None
        self.lang_to = None
        # Anki settings
        self.anki_model_name = None
        self.anki_deck_name = None
        self.anki_host = None
        self.anki_actions = actions
        self.user_action = None

    @property
    def user_action(self):
        return self.__user_action

    @user_action.setter
    def user_action(self, action: str):
        self.__user_action = action

    def get_anki_action_by_user_action(self, user_action) -> str:
        """
        Chose type Anki action
        :param user_action: Action from user
        :return: string Anki action
        """
        anki_action_by_user_action = None
        for key, value in self.anki_actions.items():
            if user_action in value:
                anki_action_by_user_action = key
                break
        if anki_action_by_user_action is None:
            raise Exception('Action not found')

        return anki_action_by_user_action
