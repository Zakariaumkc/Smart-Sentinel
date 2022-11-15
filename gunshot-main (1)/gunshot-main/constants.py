import pyaudio

AUDIO_FORMAT = pyaudio.paFloat32
AUDIO_RATE = 44100
NUMBER_OF_AUDIO_CHANNELS = 1
AUDIO_DEVICE_INDEX = 1
NUMBER_OF_FRAMES_PER_BUFFER = 88200


SAMPLE_DURATION = 2
AUDIO_VOLUME_THRESHOLD = 0.01
NOISE_REDUCTION_ENABLED = False
MODEL_CONFIDENCE_THRESHOLD = 0.5
MINIMUM_FREQUENCY = 20
MAXIMUM_FREQUENCY = AUDIO_RATE // 2
NUMBER_OF_MELS = 128
NUMBER_OF_FFTS = NUMBER_OF_MELS * 20