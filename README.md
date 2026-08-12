# End to end Medical Chatbot using Llama2

1. Run 'python -m venv mchatbot'. By running 'python -m venv env' the python version present in the base is already installed in the environment. Run 'pip list' to view the list of libraries present in the environment. OR 'py -3.11 -m venv mchatbot' to install python 3.11 as pinecone(library) does not support higher version
2. Run 'mchatbot\scripts\activate'
8. To install the local project package, create **setup.py** file and run 'pip install -e .'

## Running the project

- Refer the instruction.text file in model folder to download the model. And save the downloaded model in model folder.
- Create a .env file in the root folder and store the API key. For exmpale PINECONE_API_KEY = "xxxxxxxxxx"
- Run 'python app.py'
