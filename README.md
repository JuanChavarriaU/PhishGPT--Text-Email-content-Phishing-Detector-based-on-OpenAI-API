# Project Name

PhishGPT: Text Email/content Phishing Detector based on OpenAI API

## Overview

The goal of this project is to show the capabilities of the gpt-3.5-turbo model to analyze and detect Phishing content. Given the current problems caused by this type of attack
this is the first approch to a future embeded tool for companies. Also, This is a capstone project for Wizeline Developers Sprint.

## Files Overview

## app.py

This file contains the main Flask application responsible for handling user requests, interacting with the data processing module (`data.py`), and querying the OpenAI GPT-3.5 model through the `chat.py` module.

### Purpose

`app.py` serves as the entry point for the Flask web application. It handles incoming HTTP requests, processes user input, interacts with the `data` module for text handling, and utilizes the `chat` module to obtain AI-driven responses based on user input prompts.

### Dependencies

This file depends on:
- `Flask`: Used for creating the web application and handling routes.
- `data`: Module containing functions for text processing and API handling.
- `chat`: Module responsible for interacting with the OpenAI GPT-3.5 model.

### Functions and Routes

#### `index()`

##### Route: `'/'`

- Renders the `index.html` template when the user accesses the root URL.

#### `text_input()`

##### Route: `'/text'` (with method POST)

- Handles POST requests sent to `/text`.
- Processes user input obtained from a form submission.
- Constructs a prompt based on the user's input.
- Queries the GPT-3.5 model using the `query()` function from the `chat` module.
- Prints the classification and likelihood obtained from the model.
- Renders the `results.html` template with relevant information obtained from the model for display to the user.


## chat.py

This file contains the functionalities related to interacting with the OpenAI API for conducting conversations and processing the responses.

### Purpose

`chat.py` serves as a module responsible for communication with the OpenAI API using the OpenAI Python library. It is primarily used to generate AI-driven responses based on given prompts.

### Dependencies

This file depends on:
- `openai` library: Used to interact with OpenAI's GPT models.
- `os` module: Utilized for accessing environment variables.

### Functions

#### `query(prompt)`

This function sends a prompt to the OpenAI GPT-3.5 model and processes the generated response.

##### Parameters
- `prompt`: The text prompt sent to the GPT-3.5 model for generating a response.

##### Steps
1. **Environment Setup:** Retrieves the OpenAI API key from environment variables.
2. **OpenAI API Interaction:** Utilizes the OpenAI Python library to create a chat completion by sending a prompt to the GPT-3.5 model.
3. **Response Processing:** Extracts the response from the model dump, sends it to the `apiHandler` function in the `data.py` file for further processing.
4. **Return Values:**
    - `queryResponse`: The processed response obtained from `apiHandler`.
    - `likelihood`: Likelihood score related to the response (from `apiHandler`).
    - `classification`: Classification of the response (from `apiHandler`).


## data.py

This file contains functions responsible for handling text manipulation and processing the API response obtained from the OpenAI GPT-3.5 model.

### Purpose

`data.py` serves as a module primarily focused on text handling and processing API responses to extract relevant information such as classification, likelihood scores, and details.

### Functions

#### `textHandler(text)`

- This function processes the input text by converting it to lowercase and removing extra whitespace using regular expressions.

##### Parameters
- `text`: The input text to be processed.

##### Steps
1. **Text Processing:** Converts the input text to lowercase and removes excess whitespace using regular expressions (`re.sub()`).
2. **Return Value:** Returns the processed text.

#### `apiHandler(gpt_response)`

- This function extracts classification, likelihood, and details from the GPT-3.5 model's response.

##### Parameters
- `gpt_response`: The response obtained from the GPT-3.5 model.

##### Steps
1. **Response Parsing:** Splits the response into parts based on whitespace.
2. **Initialization:** Initializes variables to store classification, likelihood, and details.
3. **Iteration:** Iterates through the response parts to identify and extract specific information such as classification, likelihood, and details based on predefined markers ("Classification:", "Likelihood:", "Details:").
4. **Return Values:**
    - `details`: Extracted details from the response.
    - `likelihood`: Likelihood score extracted from the response.
    - `classification`: Classification extracted from the response.
      
## Dependencies

All the dependencies required to run the project.

- Flask==1.1.4
- openai==0.10.2

## Installation and Setup

- Cloning the repository
- Installing dependencies (`pip install -r requirements.txt`)
- Environment setup: install anaconda, create an env (use the name you like). 

## Usage

- Once you setup and installed everything, you can go to your terminal, beware of the env, it must be activated, then you can type this -> (`python app.py`) and press enter.
- if any error is prompted, you should see an ip address something like this: `Running on http://127.0.0.1:5000` you press CTRL+click on this address and it will open your default browser with the app running.
- Now you have to press the button to access the text area; furthermore you can paste any phishing related text and press the Submit button. and the results.html page will show with the results.

## Additional Information (if needed)

- this is a capstone project, in the future will be updated with more functionalities and better UI/IX. 
