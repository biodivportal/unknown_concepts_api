PROMPT_TEMPLATE_ANNOTATION = """
I will provide you a concept extracted from various ontologies. You have to provide a scientific description of this concept in two sentences maximum.

DO NOT OUTPUT ANY ADDITIONAL TEXT EXCEPT THESE DEFINITION SENTENCES
The concept: {class_name}"""


PROMPT_TEMPLATE_SYNONYM = """
I will provide you a concept and its defintion. You have to provide 2 or 3 scientific synonyms for that concept without doing any sentence.

DO NOT OUTPUT ANY ADDITIONAL TEXT EXCEPT THIS SYNONYM
The concept: {class_name}
The definition: {definition}"""

PROMPT_TEMPLATE_CONCEPTS = """
You are an expert on Biology. Only for the Text I provide. Identify all concepts that are relating to your field. Return an json list.

DO NOT OUTPUT ANY ADDITIONAL TEXT EXCEPT THESE WORDS
The concept: {class_name}
"""

PROMPT_TEMPLATE_ONTO = """
You are an expert in Ontologies. 

You know these onthologies and all their content and classes:
THYSANOPTERA: Thysanoptera Ontology Insecta
LIT_I: The lithologs rock names ontology for igneous rocks (
IHO: World Seas 
PTO: Plant Trait Ontology (
SCHEMAORG: create, maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond.
OBOE: semantics of scientific observation and measurement
COL:global species checklists
OBA: Ontology of Biological Attributes
CHEBI: Chemical Entities of Biological Interest Ontology
QUDT: Quantities, Units, Dimensions, and Types Ontology 
BCO: Biological Collections Ontology 
ENVO: The Environment Ontology
I-ADOPT: machine-readable variable descriptions
PATO: Phenotypic Quality Ontology (
KINGDOM: biological taxa
GEONAMES: geographical database covers all countries and contains over eleven million placenames 
ORIBATIDA:  Oribatida (moss- or beetle-mites)
RECORDBASIS: The specific nature of the data record
BIOBANK: AMMOD Metabarcoding O
UNESCO6: UNESCO nomenclature for fields of science and technology 
FLOPO: Flora Phenotype
ETS: Ecological Trait-data Standard
IOC: Bird List
SWEET: Earth and Environment Technology
ATOL: Animal Trait Ontology for Livestock 
ISOCOUNTRIES: Countries and Subdivisions
TRICHOPTERA: Trichoptera caddisflies; Insecta).
ABCD: ABCD Base Ontology 
SRAO: hierarchy of academic disciplines
PO: Plant Ontology  
NCBI: nomenclature for all of the organisms in the public sequence databases, represents about 10% of the described species of life on the planet.


I will provide a concept and definition using all your knowledge identify the three best fitting ontologies from the list and return just their identifier.  

DO NOT OUTPUT ANY ADDITIONAL TEXT EXCEPT THIS SYNONYM
The concept: {class_name}
The definition: {definition}"""
