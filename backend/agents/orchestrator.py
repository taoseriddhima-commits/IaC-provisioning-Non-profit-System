#  Orchestrator Class

import uuid
from backend.utils.preprocessor import preprocess_message
from backend.agents.classifier_agent import classify_message
from backend.agents.ner_agent import extract_entities
from backend.agents.response_agent import generate_response
from backend.vector_store import save_case


class TriageOrchestrator:
    def run(self, user_message: str):

        # Step 1: Preprocess
        cleaned = preprocess_message(user_message)

        # Step 2: Classification
        classification = classify_message(cleaned)

        # Step 3: Entity Extraction
        entities = extract_entities(cleaned)

        # Step 4: Response Generation
        response_text = generate_response(
            message=cleaned,
            classification=classification,
            entities=entities
        )

        # Step 5: Save to Vector Database
        case_id = str(uuid.uuid4())

        metadata = {
            "intent": classification.get("intent"),
            "urgency": classification.get("urgency"),
            "response_text": response_text
        }

        save_case(
            case_id=case_id,
            message=cleaned,
            metadata=metadata
        )

        # Final structured output
        final_output = {
            "case_id": case_id,
            "cleaned_message": cleaned,
            "classification": classification,
            "entities": entities,
            "response_text": response_text
        }

        return final_output
