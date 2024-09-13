from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn

from models.openai_prediction import OpenAI

# Create an instance of the FastAPI class
app = FastAPI()


# Define a Pydantic model to validate and document the input data
class EntityIdentifyRequest(BaseModel):
    text: str
    known_concepts: List[str]

class ListInputRequest(BaseModel):
    concepts: List[str]

class CombinedUnknownConceptResponse(BaseModel):
    originalLabel: str
    synonym: str
    links: Dict[str, str]
    id: str = '@id'
    suggested_description: str

class UnknownConceptResponse(BaseModel):
    originalLabel: str

class SynonymsResponse(BaseModel):
    originalLabel: str
    synonym: str

class DescriptionResponse(BaseModel):
    originalLabel: str
    suggested_description: str

class OntologyResponse(BaseModel):
    originalLabel: str
    links: Dict[str, str]

# Define the route to identify unknown concepts in the text
@app.post("/identify_unknown_concepts_synonyms_definition_ontology/")
async def identify_unknown_concepts_synonyms_definition_ontology(
        request: EntityIdentifyRequest,
        dev_mode: Optional[bool] = False  # Query parameter to enable/disable dev mode
) -> Dict[str, List[CombinedUnknownConceptResponse]]:
    """
    Identify unknown concepts in the given text based on known concepts.

    Args:
    - request: An instance of EntityIdentifyRequest containing the 'text' and 'known_concepts' list.
    - dev_mode: A boolean query parameter to enable/disable development mode.

    Returns:
    A dictionary with a list of unknown concepts identified in the text.
    """
    try:
        # Check if in development mode
        if dev_mode:
            # Return a static response for development mode
            static_response = [
                CombinedUnknownConceptResponse(
                    originalLabel="staticConcept",
                    synonym="staticSynonym",
                    links={"ontology": "staticOntologyLink"},
                    id="1234",
                    suggested_description="This is a static description for development mode."
                )
            ]
            return {"unknownConcepts": static_response}
        else:
            # Initialize the OpenAI model
            llm = OpenAI()
            # Get unknown concepts using the OpenAI model
            unknown_concepts = llm.get_unknown_concepts_LLM_definition_synonym_ontologies(request.text, request.known_concepts)
            return {"unknownConcepts": unknown_concepts}
    except Exception as e:
        # Handle exceptions and return an HTTP error response
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/identify_unknown_concepts/")
async def identify_unknown_concepts(
        request: EntityIdentifyRequest,
        dev_mode: Optional[bool] = False  # Query parameter to enable/disable dev mode
) -> Dict[str, List[UnknownConceptResponse]]:
    """
    Identify unknown concepts in the given text based on known concepts.

    Args:
    - request: An instance of EntityIdentifyRequest containing the 'text' and 'known_concepts' list.
    - dev_mode: A boolean query parameter to enable/disable development mode.

    Returns:
    A dictionary with a list of unknown concepts identified in the text.
    """
    try:
        # Check if in development mode
        if dev_mode:
            # Return a static response for development mode
            static_response = [
                UnknownConceptResponse(
                    originalLabel="staticConcept",
                )
            ]
            return {"unknownConcepts": static_response}
        else:
            # Initialize the OpenAI model
            llm = OpenAI()

            indentified_concepts = []
            for concept in llm.get_unknown_concepts_LLM(request.text, request.known_concepts):
                indentified_concepts.append({
                    'originalLabel': concept,
                })
            # Get unknown concepts using the OpenAI model
            #unknown_concepts = llm.get_unknown_concepts_LLM(request.text, request.known_concepts)
            return {"unknownConcepts": indentified_concepts}
    except Exception as e:
        # Handle exceptions and return an HTTP error response
        raise HTTPException(status_code=500, detail=str(e))


# Define the route to identify unknown concepts in the text
@app.post("/create_synonyms/")
async def create_synonyms(
        request: ListInputRequest,
        dev_mode: Optional[bool] = False  # Query parameter to enable/disable dev mode
) -> Dict[str, List[SynonymsResponse]]:
    """
    Identify unknown concepts in the given text based on known concepts.

    Args:
    - request: An instance of EntityIdentifyRequest containing the 'text' and 'known_concepts' list.
    - dev_mode: A boolean query parameter to enable/disable development mode.

    Returns:
    A dictionary with a list of unknown concepts identified in the text.
    """
    try:
        # Check if in development mode
        if dev_mode:
            # Return a static response for development mode
            static_response = [
                SynonymsResponse(
                    originalLabel="staticConcept",
                    synonym="staticSynonym"
                )
            ]
            return {"synonyms": static_response}
        else:
            # Initialize the OpenAI model
            llm = OpenAI()
            # Get unknown concepts using the OpenAI model
            synonyms = []
            for concept in request.concepts:
                synonyms.append({
                    'originalLabel': concept,
                    'synonym': llm.generate_synonym(concept)
                })

            return {"synonyms": synonyms}
    except Exception as e:
        # Handle exceptions and return an HTTP error response
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/create_description/")
async def create_description(
        request: ListInputRequest,
        dev_mode: Optional[bool] = False  # Query parameter to enable/disable dev mode
) -> Dict[str, List[DescriptionResponse]]:
    """
    Identify unknown concepts in the given text based on known concepts.

    Args:
    - request: An instance of EntityIdentifyRequest containing the 'text' and 'known_concepts' list.
    - dev_mode: A boolean query parameter to enable/disable development mode.

    Returns:
    A dictionary with a list of unknown concepts identified in the text.
    """
    try:
        # Check if in development mode
        if dev_mode:
            # Return a static response for development mode
            static_response = [
                DescriptionResponse(
                    originalLabel="staticConcept",
                    suggested_description="This is a static description for development mode."
                )
            ]
            return {"suggested_description": static_response}
        else:
            # Initialize the OpenAI model
            llm = OpenAI()
            # Get unknown concepts using the OpenAI model
            suggested_description = []
            for concept in request.concepts:
                suggested_description.append({
                    'originalLabel': concept,
                    'suggested_description': llm.generate_definition(concept)
                })

            return {"suggested_description": suggested_description}
    except Exception as e:
        # Handle exceptions and return an HTTP error response
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/get_ontology/")
async def get_ontology(
        request: ListInputRequest,
        dev_mode: Optional[bool] = False  # Query parameter to enable/disable dev mode
) -> Dict[str, List[OntologyResponse]]:
    """
    Identify unknown concepts in the given text based on known concepts.

    Args:
    - request: An instance of EntityIdentifyRequest containing the 'text' and 'known_concepts' list.
    - dev_mode: A boolean query parameter to enable/disable development mode.

    Returns:
    A dictionary with a list of unknown concepts identified in the text.
    """
    try:
        # Check if in development mode
        if dev_mode:
            # Return a static response for development mode
            static_response = [
                OntologyResponse(
                    originalLabel="staticConcept",
                    links={"ontology": "staticOntologyLink"},
                )
            ]
            return {"suggested_description": static_response}
        else:
            # Initialize the OpenAI model
            llm = OpenAI()
            # Get unknown concepts using the OpenAI model
            ontologies = []
            for concept in request.concepts:
                ontologies.append({
                    'originalLabel': concept,
                    'links': {"ontology": llm.find_fitting_ontology(concept)}
                })

            return {"ontologies": ontologies}
    except Exception as e:
        # Handle exceptions and return an HTTP error response
        raise HTTPException(status_code=500, detail=str(e))


# This block makes the script executable
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
