import emoji
from tensorflow.keras.preprocessing.sequence import pad_sequences


def preprocess_text(text, tokenizer, max_len):
    """
    Preprocess input text using the same pipeline
    used during model training.
    """

    # Remove emojis
    text = emoji.replace_emoji(text, replace='')

    # Convert characters to integer sequence
    sequence = tokenizer.texts_to_sequences([text])

    # Pad / truncate sequence
    padded_sequence = pad_sequences(
        sequence,
        maxlen=max_len,
        padding='post',
        truncating='post'
    )

    return padded_sequence