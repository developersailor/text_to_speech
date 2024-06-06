from gtts import gTTS

def convert_text_to_speech(text, language='tr', output_filename="speech.mp3", slow=True):
    """
    Converts text to speech and saves it as an audio file.

    Args:
            text: The text to convert to speech.
            language: The language of the text (default: Turkish).
            output_filename: The name of the output audio file (default: speech.mp3).
            slow: Whether to slow down the speech (default: False).

    Returns:
            None
    """
    tts = gTTS(text, lang=language, slow=slow)
    tts.save(output_filename)

# Example usage
text_to_convert = "Her ne kadar yapay zeka gelişse de, insan zekasının yerini tutamaz."
convert_text_to_speech(text_to_convert, slow=True)

output_filename = "speech.mp3"
print(f"Speech saved to: {output_filename}")
