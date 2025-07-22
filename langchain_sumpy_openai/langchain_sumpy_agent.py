from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import SecretStr
from sympy import symbols, diff, integrate, ln, limit, oo, log

openai_api_key = "your-openai-api-key"

# ------------------- Symbolic Tool -------------------
x = symbols('x')

@tool
def run_sympy(code: str) -> str:
    """
    Executes a single-line SymPy expression and returns the result.
    Supported expressions include differentiation, integration, and limits.
    """
    local_dict = {
        "x": x,
        "diff": diff,
        "integrate": integrate,
        "ln": ln,
        "log": log,
        "limit": limit,
        "oo": oo
    }
    try:
        sanitized_code = code.replace('```python', '').replace('```', '').strip()
        result = eval(sanitized_code, {}, local_dict)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# ------------------- LLM Setup -------------------
llm = ChatOpenAI(
    model="gpt-4-turbo",  # ✅ Use 'model' instead of 'model_name'
    temperature=0,
    api_key=SecretStr(openai_api_key)  # Optional, can rely on env var
)

prompt = ChatPromptTemplate.from_template("""
You are a SymPy expert.
Convert this math question into a SINGLE valid SymPy expression.
Do NOT add import statements, code blocks, or explanations.
Expression only.

Question: {question}
Answer:
""")

# ------------------- Helper Functions -------------------
def get_sympy_expression(user_question: str) -> str:
    chain = prompt | llm
    result = chain.invoke({"question": user_question})
    return result.content.strip()

def execute_sympy_expression(expression: str) -> str:
    return run_sympy.invoke({"code": expression})

# ------------------- Example Usage -------------------
def ask_math_question(user_question: str):
    print(f"\nUser Question: {user_question}")
    sympy_code = get_sympy_expression(user_question)
    print(f"[LLM-generated SymPy Code]: {sympy_code}")
    result = execute_sympy_expression(sympy_code)
    print(f"[Final Result]: {result}")

if __name__ == "__main__":
    questions = [
        "What is the derivative of ln(x**2 + 1)?",
        "What is the integral of 1 / (x**2 + 1)?",
        "What is the limit of (1 + 1/x)**x as x approaches infinity?"
    ]

    for q in questions:
        ask_math_question(q)