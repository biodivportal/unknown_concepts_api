# FastAPI Concept Identification API

This FastAPI application provides an API endpoint to identify unknown concepts in a given text, based on a list of known concepts. It integrates with the OpenAI API to analyze text and generate responses. A development mode is also available, which returns a static response for testing purposes.

## Features

- **Identify Unknown Concepts**: Extract unknown concepts from text by comparing them against a list of known concepts.
- **Development Mode**: Easily test the API with a static response by enabling development mode via a query parameter.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/biodivportal/unknown_concepts_api.git
   cd unknown_concepts_api
   
2. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt

3. **Set up the OpenAI API key**:

   Ensure you have a `credentials_private.json` file in the root directory with your OpenAI API key:

   ```json
   {
     "api_key": "your_openai_api_key"
   }

## Usage: Running the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

## API Endpoint

- **URL**: `/identify_unknown_concepts/`
- **Method**: `POST`
- **Request Body**: JSON object containing:
  - `text` (string): The input text to analyze.
  - `known_concepts` (list of strings): A list of known concepts to exclude.
- **Query Parameter**: `dev_mode` (boolean, optional): Set to `true` to enable development mode, which returns a static response.

## Example Request

Here is an example of how to make a request to the API:

```bash
curl -X POST "http://127.0.0.1:8001/identify_unknown_concepts/?dev_mode=true" \
-H "Content-Type: application/json" \
-d '{
  "text": "There is for example genetic variability, species diversity, ecosystem diversity and phylogenetic diversity. Diversity is not distributed evenly on Earth.",
  "known_concepts": ["concept1", "concept2"]
}'
```

### Development Mode
Enable development mode by setting the `dev_mode` query parameter to `true`. In this mode, the API returns a static response for testing purposes:

```bash
{
  "unknownConcepts": [
    {
      "originalLabel": "staticConcept",
      "synonym": "staticSynonym",
      "links": {
        "ontology": "staticOntologyLink"
      },
      "id": "1234",
      "suggested_description": "This is a static description for development mode."
    }
  ]
}
```


## Example Request

Here is an example of how to make a request to the API:

```bash
curl -X POST "http://127.0.0.1:8001/identify_unknown_concepts/?dev_mode=true" \
-H "Content-Type: application/json" \
-d '{
  "text": "This is an example text.",
  "known_concepts": ["concept1", "concept2"]
}'
```

## Docker Usage

You can also run this FastAPI application inside a Docker container.

### Building the Docker Image

1. Make sure you have Docker installed on your machine.

2. Build the Docker image using the following command:

```bash
   docker build -t fastapi-app .
```

### Running the Docker Container
```bash
   docker run -p 8001:8001 fastapi-app
```
This command starts the Docker container and maps port 8001 of the container to port 8000 on your local machine. You can then access the FastAPI application at http://localhost:8001.


