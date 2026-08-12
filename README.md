# End to end Medical Chatbot using Llama2

1. Run 'python -m venv mchatbot'. By running 'python -m venv env' the python version present in the base is already installed in the environment. Run 'pip list' to view the list of libraries present in the environment. OR 'py -3.11 -m venv mchatbot' to install python 3.11 as pinecone(library) does not support higher version
2. Run 'mchatbot\scripts\activate'
3. To install the local project package, create **setup.py** file and run 'pip install -e .'

## Running the project

1. Refer the instruction.text file in model folder to download the model. And save the downloaded model in model folder.
2. Create a folder named 'data' in the root and include the data file.
3. Create a .env file in the root folder and store the API key. For exmpale PINECONE_API_KEY = "xxxxxxxxxx"
4. Run 'python app.py'
