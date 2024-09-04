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


class UnknownConceptResponse(BaseModel):
    originalLabel: str
    synonym: str
    links: Dict[str, str]
    id: str = '@id'
    suggested_description: str


# Define the route to identify unknown concepts in the text
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
            unknown_concepts = llm.get_unknown_concepts_LLM(request.text, request.known_concepts)
            return {"unknownConcepts": unknown_concepts}
    except Exception as e:
        # Handle exceptions and return an HTTP error response
        raise HTTPException(status_code=500, detail=str(e))


# This block makes the script executable
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
