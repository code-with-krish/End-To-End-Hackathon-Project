from flask import Flask, render_template, request, jsonify
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from vectorstore_loader import load_vector_store, extract_amount_rupee

app = Flask(__name__)
db = load_vector_store()

def get_relevant_clauses(query):
    results = db.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in results])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]

        response_schemas = [
            ResponseSchema(name="decision", description="approved or rejected"),
            ResponseSchema(name="amount", description="₹ amount to be paid or null"),
            ResponseSchema(name="justification", description="reason based on policy clause")
        ]
        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        prompt_template = PromptTemplate(
            input_variables=["query", "context", "format_instructions"],
            template="""
You are a highly reliable insurance claim assistant.

Given the user query and the provided policy clauses, determine whether the claim is approved or rejected.

⛔ Do not assume anything beyond the context.  
✅ Use only the information given in the context.

Respond in the following JSON format only:
{format_instructions}

Rules:
1. "decision" must be either "approved" or "rejected" — never null.
2. "amount" must be in INR format with ₹ sign (e.g., "₹50000") if an amount is clearly mentioned in the context.
3. If no amount is found in the context, return "amount": null
4. "justification" must clearly explain the reason and quote clause if possible.
5. Do not add anything outside the JSON.

---

User Query:
{query}

Relevant Policy Clauses:
{context}
"""
        )

        llm = Ollama(model="mistral")
        chain = prompt_template | llm | output_parser

        context = get_relevant_clauses(query)
        response = chain.invoke({
            "query": query,
            "context": context,
            "format_instructions": format_instructions
        })

        # Inject ₹ amount manually if model missed it
        if not response.get("amount") or response["amount"] in ["null", "NULL", None]:
            response["amount"] = extract_amount_rupee(context)

        return jsonify(response)

    return render_template("index.html")

# ✅ এই অংশটা সবচেয়ে গুরুত্বপূর্ণ
if __name__ == "__main__":
    print("🚀 Flask app running on http://127.0.0.1:5000")
    app.run(debug=True)
