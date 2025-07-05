# Gemini Chatbot with Streamlit

This is a simple chatbot application built using Streamlit and the Google Gemini API.

## Features

- Interactive chat interface.
- Uses the Gemini Pro model for generating responses.
- Maintains chat history within the session.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)

## Installation

1.  **Clone the repository (if applicable) or navigate to the project directory:**

    ```bash
    cd "D:/code/chat bot streamlit"
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## API Key Setup

This application uses the Google Gemini API. You need to provide your API key.

1.  **Get your API Key:**
    If you don't have one, you can obtain a Gemini API key from the Google AI Studio: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

2.  **Update `app.py`:**
    Open the `app.py` file and replace `"YOUR_GEMINI_API_KEY"` with your actual API key:

    ```python
    GEMINI_API_KEY = "AIzaSyB2_Agj5KlfFhVQCJSw9xT0soRltapmTP4" # Your actual API key
    ```

    *Note: For production applications, it is highly recommended to use Streamlit secrets or environment variables to manage your API key securely instead of hardcoding it.*

## Running the Application

To run the chatbot, execute the following command in your terminal from the project directory:

```bash
streamlit run app.py
```

This will open the Streamlit application in your web browser.