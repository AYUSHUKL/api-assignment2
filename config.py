# config.py

# API configurations
API_HOST = "127.0.0.1"
API_PORT = 8000
DEBUG_MODE = True

# Model configurations
SUMMARIZATION_MODEL = "t5-small"  # Model for text summarization
SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"  # Model for sentiment analysis
QA_MODEL = "distilbert-base-uncased-distilled-squad"  # Model for question answering
IMAGE_CLASSIFICATION_MODEL = "microsoft/resnet-50"  # Model for image classification
OCR_LANGUAGES = ['en']  # OCR language support

# Paths
FINE_TUNED_MODEL_PATH = "./model/fine_tuned_model/"  # Path for saving/loading fine-tuned model

# Metrics configurations
METRICS_ENABLED = True  # Toggle for enabling/disabling LLMOps metrics
METRIC_LATENCY_THRESHOLD = 0.5  # Example threshold for latency

# API keys (if using external services)
HUGGINGFACE_API_KEY = "your_huggingface_api_key"  # Add your API key if needed

# Dataset configurations
DATA_PATH = "./data/customer_data.csv"
IMAGE_DATA_PATH = "./data/product_images/"

# Other settings
MAX_TEXT_LENGTH = 512  # Maximum text length for models
