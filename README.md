# Text-to-Speech Synthesizer with OpenAI API

This project demonstrates text-to-speech synthesis using the OpenAI API. It utilizes the OpenAI GPT-3 language model to convert text into speech for Japanese, English, and Chinese languages.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Install dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set your OpenAI API key as an environment variable:

    ```bash
    export API_KEY="your-api-key"
    ```

2. Run the `main.py` script:

    ```bash
    python main.py
    ```

    The script will use the specified OpenAI GPT-3 model to generate speech for Japanese, English, and Chinese texts. The generated audio files will be saved in the project directory.

## Configuration

- `model`: Specify the GPT-3 model to use (default is 'tts-1').
- `voice`: Choose the voice for text-to-speech synthesis.
- `response_format`: Select the format of the audio response (mp3, opus, aac, and flac).

## Output

The generated audio files will be saved in the project directory with filenames corresponding to the language and response format. For example:

- `Japanese_audio.mp3`
- `English_audio.mp3`
- `Chinese_audio.mp3`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# Desktop-Openai-text-2-speech
