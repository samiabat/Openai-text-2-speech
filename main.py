import os
from openai import OpenAI
api_key = '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'
os.environ['API-KEY'] = api_key

class TextToSpeech:
    """
    TextToSpeech class for converting text to speech using the OpenAI API.

    Parameters:
    - model (str): The model identifier for text-to-speech (default is 'tts-1').
    - voice (str): The voice identifier for text-to-speech (default is 'alloy').

    Attributes:
    - api_key (str): The API key for accessing the OpenAI API.
    - lan_type_mapping (dict): Mapping of language types to their corresponding names.
    - client (OpenAI): The OpenAI client for making API requests.
    - model (str): The specified model for text-to-speech.
    - voice (str): The specified voice for text-to-speech.

    Methods:
    - text_to_speech(text, lan_type, response_format='mp3'): Converts input text to speech
      and saves the audio file based on the specified language type and response format.

    Raises:
    - Exception: If an error occurs during the text-to-speech conversion.

    Note:
    - Requires an OpenAI API key set as an environment variable 'API-KEY'.
    """
    def __init__(self, model='tts-1', voice='alloy'):
        """
        Initializes a TextToSpeech instance.

        Parameters:
        - model (str): The model identifier for text-to-speech (default is 'tts-1').
        - voice (str): The voice identifier for text-to-speech (default is 'alloy').
        """
        self.api_key = os.environ.get('API-KEY')
        self.lan_type_mapping  ={0:'Japanese', 1:'English', 2:'Chinese'}
        self.client = OpenAI(api_key = self.api_key)
        self.model = model
        self.voice = voice
      


    def text_to_speech(self, text, lan_type, response_format='wav'):
        """
        Converts input text to speech and saves the audio file based on the specified language type and response format.

        Parameters:
        - text (str): The input text to be converted to speech.
        - lan_type (int): The language type identifier (0 for Japanese, 1 for English, 2 for Chinese).
        - response_format (str): The format of the audio response (default is 'mp3').

        Raises:
        - Exception: If an error occurs during the text-to-speech conversion.
        """
        try:
          response = self.client.audio.speech.create(
              model=self.model,
              voice=self.voice,
              input=text,
              speed=1
            )
          response.stream_to_file(f'{self.lan_type_mapping[lan_type]}_audio.{response_format}')
        except Exception as e:
          raise e

class Synthesizer:
    def __init__(self):
        japanese_text = 'こんにちは、私は日本語を話す言語モデルです。'#Japanese
        english_text = 'Hello, I am an English speaking language model.' #English
        chinese_text = '你好，我是一个说中文的语言模型。' #Chinnese

        model = 'tts-1' #@param ['tts-1', 'tts-1-hd'] {type:"string"}
        voice = 'nova' #@param ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'] {type:"string"}
        response_format = 'mp3' #@param ['mp3', 'opus', 'aac', 'and', 'flac'] {type:"string"}

        model = TextToSpeech(
            model=model, 
            voice = voice
            )
        model.text_to_speech(japanese_text, 0, response_format)
        model.text_to_speech(english_text, 1, response_format)
        model.text_to_speech(chinese_text, 2, response_format)
if __name__ == '__main__':
    synthesizer = Synthesizer()