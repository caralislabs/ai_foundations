# 🧮 LangChain + OpenAI + SymPy Math Assistant

A practical example of combining **LLMs** with **symbolic computation** using **LangChain**, **OpenAI's GPT**, and **SymPy**.

This project demonstrates how to build a simple math assistant that:
- Understands natural language math queries
- Converts them into executable SymPy expressions
- Safely evaluates them and returns results  

## 🚀 Features
- ✅ LLM-assisted SymPy expression generation  
- ✅ Safe evaluation of symbolic expressions (derivatives, integrals, limits)  
- ✅ LangChain chaining pattern with latest API  
- ✅ OpenAI GPT-4-turbo integration  

## 🛠️ Technologies Used
- [LangChain](https://python.langchain.com/)  
- [OpenAI API](https://platform.openai.com/)  
- [SymPy](https://www.sympy.org/)  

## 📜 Example Usage  

```bash
$ python langchain_sumpy_agent.py
```

Example output:
```
User Question: What is the derivative of ln(x**2 + 1)?
[LLM-generated SymPy Code]: diff(ln(x**2 + 1), x)
[Final Result]: 2*x/(x**2 + 1)
```

## 📦 Installation

```bash
pip install langchain langchain-openai langchain-community sympy
```

Set your OpenAI API key:

- in the code
```
    openai_api_key = "your-openai-api-key"
```

- or, with minimal code changes

```bash
export OPENAI_API_KEY=your-key-here
```

## 🔗 Related Articles
- [Technical Deep Dive on Combining LLMs with Symbolic Engines](https://medium.com/@ncaraliceanews/how-to-build-a-symbolic-math-assistant-with-openai-langchain-and-sympy-bd320f19b33b)  

## 📝 License
MIT License
