import os
import json
import warnings
import logging
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from templates.prompt_template import (
    PROMPT_TEMPLATE_ANNOTATION,
    PROMPT_TEMPLATE_SYNONYM,
    PROMPT_TEMPLATE_CONCEPTS,
    PROMPT_TEMPLATE_ONTO
)

# Suppress warnings if necessary
warnings.filterwarnings("ignore")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load OpenAI API Key
try:
    with open('./credentials_private.json') as f:
        data = json.load(f)
    os.environ['OPENAI_API_KEY'] = data['api_key']
except FileNotFoundError:
    logger.error("Credential file not found. Please provide a valid 'credentials_private.json'.")
except json.JSONDecodeError:
    logger.error("Error decoding JSON from the credentials file.")
except Exception as e:
    logger.error(f"Unexpected error loading credentials: {e}")

class OpenAI:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens=200)

    def get_concept_LLM(self, text: str) -> list:
        try:
            prompt = PROMPT_TEMPLATE_CONCEPTS.format(class_name=text)
            messages = [HumanMessage(content=prompt)]
            response = self.llm(messages)
            logger.info(f"Concepts generated: {response.content}")
            return json.loads(response.content).get("concepts", [])
        except json.JSONDecodeError:
            logger.error("Error parsing JSON response from get_concept_LLM.")
            return []
        except Exception as e:
            logger.error(f"Error generating concepts: {e}")
            return []

    def get_unknown_concepts_LLM(self, text: str, known_concepts: list) -> list:
        try:
            final_concepts = []
            concepts = self.get_concept_LLM(text)

            # Filter out known concepts
            unknown_concepts = [concept for concept in concepts if concept not in known_concepts]

            for concept in unknown_concepts:
                final_concepts.append(self.create_answer(concept))

            return final_concepts
        except Exception as e:
            logger.error(f"Error identifying unknown concepts: {e}")
            return []

    def find_fitting_ontology(self, concept: str, definition: str) -> str:
        try:
            prompt = PROMPT_TEMPLATE_ONTO.format(class_name=concept, definition=definition)
            messages = [HumanMessage(content=prompt)]
            response = self.llm(messages)
            logger.info(f"Ontology found: {response.content}")
            return response.content
        except Exception as e:
            logger.error(f"Error finding fitting ontology: {e}")
            return ""

    def create_answer(self, concept: str) -> dict:
        try:
            llm_definition = self.generate_definition(concept)

            return {
                "originalLabel": concept,
                "synonym": self.generate_synonym(concept, llm_definition),
                "links": {
                    "ontology": self.find_fitting_ontology(concept, llm_definition),
                },
                "@id": '1234',
                "suggested_description": llm_definition,
            }
        except Exception as e:
            logger.error(f"Error creating answer for concept '{concept}': {e}")
            return {}

    def generate_definition(self, concept: str) -> str:
        try:
            prompt = PROMPT_TEMPLATE_ANNOTATION.format(class_name=concept)
            messages = [HumanMessage(content=prompt)]
            response = self.llm(messages)
            return response.content
        except Exception as e:
            logger.error(f"Error generating definition for concept '{concept}': {e}")
            return ""

    def generate_synonym(self, concept: str, definition: str) -> str:
        try:
            prompt = PROMPT_TEMPLATE_SYNONYM.format(class_name=concept, definition=definition)
            messages = [HumanMessage(content=prompt)]
            response = self.llm(messages)
            return response.content
        except Exception as e:
            logger.error(f"Error generating synonym for concept '{concept}': {e}")
            return ""
