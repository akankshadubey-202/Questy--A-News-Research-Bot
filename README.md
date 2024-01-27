# Questy-A News Research Bot

Questy is a user-friendly news research bot designed for effortless information retrieval. Users can input article URLs and ask questions to receive relevant insights from the stock market and financial domain.
![image](https://github.com/akankshadubey-202/Questy--A-News-Research-Bot/assets/91489416/f2675a6b-2b84-4824-a84e-ab0f1bdc6ed7)

## Features of the bot

- Load URLs or upload text files containing URLs to fetch article content.
- Process article content through LangChain's UnstructuredURL Loader
- Construct an embedding vector using OpenAI's embeddings and leverage FAISS, a powerful similarity search library, to enable swift and effective retrieval of relevant information
- Interact with the LLM's (Chatgpt) by inputting queries and receiving answers along with source URLs.

## Project Structure

- main.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
- newstool: A folder that contains a pickle file to store the FAISS index.
- .env: Configuration file for storing your OpenAI API key.
- 
## To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the application using streamlit run main.py
4. Access the system by opening a web browser
