# Streamlit Chatbot with OpenAI, FAISS, & Langchain 🦜️🔗

This repository contains a Streamlit application for a chatbot that utilizes OpenAI's language model, FAISS for document retrieval, and Langchain for managing conversation chains. The chatbot engages in conversations and retrieves relevant documents based on the user's input.


## Features

- **OpenAI Language Model:** Provides natural language understanding and generation.
- **FAISS for Document Retrieval:** Efficiently retrieves relevant documents based on user queries.
- **Langchain for Conversation Management:** Manages conversation chains with memory capabilities.
- **Conversation History:** Maintains conversation history within the session.
- **Customizable UI:** Includes custom CSS for enhanced user experience.

## Setup

### Prerequisites

>- Python 3.11+
>- Streamlit
>- OpenAI API key
>- LangChain
>- FAISS library

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/arnabsaha7/Chatbot-with-LLM_RAG.git
    cd Chatbot-with-LLM_RAG
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your OpenAI API key:**

    Replace the placeholder API key in the code with your actual OpenAI API key.

    ```python
    os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
    ```

4. **Prepare the FAISS index and documents:**

    Ensure you have the FAISS index (`faiss_index_1`) and documents file (`documents.json`) in the project directory.

## Running the Application

1. **Start the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2. **Open your browser:**

    The application will be available at `http://localhost:8501`.

## Usage

- `Welcome Screen:` The app starts with a welcome screen. You can begin interacting with the chatbot by typing your message in the input box.

- `Conversation History:` The conversation history is displayed on the screen. User messages are shown in one style, while the bot's responses are shown in another.

- `Document Retrieval:` When you send a message, the chatbot retrieves relevant documents from the FAISS index and uses them to provide a more informed response.

- `Reset Conversation:` Use the "Reset Conversation" button to clear the conversation history and start a new session.

## File Structure

- `Chatbot.py` -->   The main Streamlit application file.
- `requirements.txt` -->   Lists all Python dependencies.
- `faiss_index_1` -->   The FAISS index file.
- `documents.json` -->   JSON file containing documents with metadata.
- `styles.css` -->   Custom CSS for styling the app.

## Acknowledgements

- [OpenAI](https://www.openai.com/)
- [FAISS](https://github.com/facebookresearch/faiss.git)
- [Streamlit](https://www.streamlit.io/)
- [Langchain](https://github.com/langchain-ai/langchain.git)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or inquiries, please contact [your-email@example.com].

