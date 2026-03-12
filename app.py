import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

DOCUMENT_PROMPTS = {
    "employment_contract": """Generate a professional Employment Contract with the following details:
- Employer: {employer_name}
- Employee: {employee_name}
- Position/Job Title: {position}
- Start Date: {start_date}
- Salary/Compensation: {salary}
- Work Location: {work_location}
- Additional Terms: {additional_terms}

Create a complete, legally-structured employment contract with all standard clauses including duties and responsibilities, compensation, working hours, confidentiality, termination conditions, and governing law. Format it professionally with clear section headings.""",

    "nda": """Generate a professional Non-Disclosure Agreement (NDA) with the following details:
- Disclosing Party: {party_one}
- Receiving Party: {party_two}
- Effective Date: {start_date}
- Purpose of Disclosure: {purpose}
- Confidentiality Period: {duration}
- Additional Terms: {additional_terms}

Create a complete, legally-structured NDA with all standard clauses including definition of confidential information, obligations, exclusions, term and termination, remedies, and governing law. Format it professionally with clear section headings.""",

    "lease_agreement": """Generate a professional Residential Lease Agreement with the following details:
- Landlord: {party_one}
- Tenant: {party_two}
- Property Address: {property_address}
- Lease Start Date: {start_date}
- Lease Duration: {duration}
- Monthly Rent: {salary}
- Security Deposit: {security_deposit}
- Additional Terms: {additional_terms}

Create a complete, legally-structured lease agreement with all standard clauses including property description, rent payment, security deposit, maintenance responsibilities, restrictions, entry rights, and termination. Format it professionally with clear section headings.""",

    "service_agreement": """Generate a professional Service Agreement with the following details:
- Service Provider: {party_one}
- Client: {party_two}
- Service Description: {purpose}
- Start Date: {start_date}
- Duration: {duration}
- Compensation: {salary}
- Additional Terms: {additional_terms}

Create a complete, legally-structured service agreement with all standard clauses including scope of services, payment terms, intellectual property, confidentiality, liability limitation, and termination. Format it professionally with clear section headings.""",

    "partnership_agreement": """Generate a professional Partnership Agreement with the following details:
- Partner 1: {party_one}
- Partner 2: {party_two}
- Business Name: {employer_name}
- Business Purpose: {purpose}
- Start Date: {start_date}
- Profit/Loss Split: {salary}
- Additional Terms: {additional_terms}

Create a complete, legally-structured partnership agreement with all standard clauses including capital contributions, profit/loss allocation, management responsibilities, decision-making, dissolution, and governing law. Format it professionally with clear section headings.""",
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "No data provided."}), 400

        doc_type = data.get("doc_type", "").strip()
        if not doc_type or doc_type not in DOCUMENT_PROMPTS:
            return jsonify({"success": False, "error": "Invalid document type selected."}), 400

        prompt_template = DOCUMENT_PROMPTS[doc_type]

        fields = {
            "employer_name": data.get("employer_name", "N/A"),
            "employee_name": data.get("employee_name", "N/A"),
            "party_one": data.get("party_one", data.get("employer_name", "N/A")),
            "party_two": data.get("party_two", data.get("employee_name", "N/A")),
            "position": data.get("position", "N/A"),
            "start_date": data.get("start_date", "N/A"),
            "salary": data.get("salary", "N/A"),
            "work_location": data.get("work_location", "N/A"),
            "duration": data.get("duration", "N/A"),
            "purpose": data.get("purpose", "N/A"),
            "property_address": data.get("property_address", "N/A"),
            "security_deposit": data.get("security_deposit", "N/A"),
            "additional_terms": data.get("additional_terms", "None specified"),
        }

        prompt = prompt_template.format(**fields)
        prompt += "\n\nIMPORTANT: Add a disclaimer at the end stating this is AI-generated and should be reviewed by a qualified attorney before use."

        response = model.generate_content(prompt)
        document_text = response.text

        return jsonify({"success": True, "document": document_text, "doc_type": doc_type})

    except Exception as e:
        return jsonify({"success": False, "error": f"Generation failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)