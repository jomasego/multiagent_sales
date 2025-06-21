import streamlit as st
import os
import pandas as pd
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain.tools import Tool

# Load environment variables from .env file
load_dotenv()

# --- LLM and Tool Definitions ---

# Initialize LLMs
# Sales Agent: High-capability, creative model for customer interaction
llm_sales = ChatGroq(temperature=0.8, model_name="llama3-70b-8192")
# Research Agent: Factual, concise model for technical lookups
llm_research = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1)
# Business Agent: Strategic, balanced model for inventory/pricing decisions
llm_business = ChatGroq(temperature=0.4, model_name="llama3-70b-8192")


# --- Tool Functions ---

@st.cache_data
def load_inventory():
    """Loads the vehicle inventory from the CSV file."""
    inventory_path = "data/vehicles.csv"
    if os.path.exists(inventory_path):
        return pd.read_csv(inventory_path)
    # Create a dummy dataframe if the file doesn't exist
    st.warning("Inventory file 'data/vehicles.csv' not found. Using empty inventory.")
    return pd.DataFrame(columns=['id', 'make', 'model', 'year', 'price', 'color'])

def search_inventory(query: str) -> str:
    """
    Searches the vehicle inventory based on a customer's query.
    The query should be a string containing keywords like make, model, color, etc.
    Returns a string representation of matching vehicles.
    """
    inventory = load_inventory()
    if inventory.empty:
        return "The vehicle inventory is currently empty."

    # A more robust search would involve better filtering or a database query.
    # For this demo, we'll do a simple case-insensitive search across all columns.
    try:
        # Create a boolean mask for rows that contain the query in any of their cells
        mask = inventory.apply(
            lambda row: row.astype(str).str.contains(query, case=False).any(),
            axis=1
        )
        results = inventory[mask]

        if results.empty:
            return f"No vehicles found matching your query: '{query}'. Try a broader search."
        return f"Found the following vehicles matching '{query}':\n{results.to_string()}"
    except Exception as e:
        return f"An error occurred while searching the inventory: {e}"


def get_technical_details(query: str) -> str:
    """
    Provides technical specifications or answers research questions about a vehicle.
    Use this when the customer asks for details not present in the main inventory,
    like safety features, engine specs, or comparisons.
    The query should be a clear, specific question about a vehicle.
    """
    prompt = f"""
    You are Dru, a vehicle research specialist. A customer has a question.
    Provide a concise, factual answer based on your knowledge.
    If you don't know the answer, say so. Do not invent information.

    Customer's question: "{query}"

    Your factual response:
    """
    response = llm_research.invoke(prompt)
    return response.content

def get_business_decision(query: str) -> str:
    """
    Consults the business coordinator for decisions on pricing, discounts, or inventory strategy.
    Use this when a customer wants to negotiate a price or asks about business policies.
    The query should be a clear question about a business matter.
    """
    prompt = f"""
    You are the Boss, the business coordinator. A sales agent needs a decision.
    Base your answer on standard business policies (e.g., firm but fair pricing, small discounts for serious buyers).

    Sales agent's query: "{query}"

    Your decision:
    """
    response = llm_business.invoke(prompt)
    return response.content


# --- Agent Setup ---

# Define the tools the sales agent can use
tools = [
    Tool(
        name="SearchInventory",
        func=search_inventory,
        description="Searches the vehicle inventory for cars matching a description (e.g., 'black sedan', '2022 Toyota')."
    ),
    Tool(
        name="GetTechnicalDetails",
        func=get_technical_details,
        description="Gets technical specifications or answers specific research questions about a vehicle (e.g., 'what are the safety features of the Honda Accord?')."
    ),
    Tool(
        name="GetBusinessDecision",
        func=get_business_decision,
        description="Consults the business coordinator for pricing, discounts, and negotiation strategies (e.g., 'can I offer a 5% discount on the Tesla Model 3?')."
    ),
]

# This is the core prompt that guides the agent's reasoning process.
# It uses the ReAct (Reasoning and Acting) framework.
agent_prompt_template = """
You are John, a friendly, professional, and highly capable AI car sales expert.
Your goal is to understand the customer's needs, provide them with the best options from our inventory,
and answer their questions accurately by collaborating with your specialized AI colleagues.

You have access to the following tools:
{tools}

To answer the customer's request, you MUST use the following format:

Thought: Do I need to use a tool? Yes. I need to understand what the user wants and then decide which tool is best to use. I will reason about this and then act.
Action: The action to take. It MUST be one of the following: {tool_names}.
Action Input: The input to the action.
Observation: The result of the action.

... (this Thought/Action/Action Input/Observation can repeat N times)

Thought: I have now gathered enough information and can construct a final answer for the user.
Final Answer: [A final, comprehensive, and friendly response to the user's original question. This is what the user will see. Do not just repeat the tool output; synthesize the information into a conversational response.]

---
Here are some rules to follow:
1.  Always start with a friendly greeting and aim to build rapport.
2.  First, use the `SearchInventory` tool to see if you can find what the customer is asking for.
3.  If the customer asks a technical question that the inventory search doesn't answer, use the `GetTechnicalDetails` tool.
4.  If the customer wants to negotiate or asks about pricing policies, use the `GetBusinessDecision` tool.
5.  Do not make up information. If you don't know something, use a tool to find out or say that you don't know.
6.  Your "Final Answer" should be a single, helpful, and conversational response directed to the customer. Do not include the "Thought:" process in the final answer.
---

Let's begin!

Human: {input}

{agent_scratchpad}
"""

# Create the agent
prompt = PromptTemplate.from_template(agent_prompt_template)
agent = create_react_agent(llm_sales, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors="Check your output and make sure it conforms to the format instructions.",
    max_iterations=10 # Give the agent more steps to think
)


# --- Streamlit UI ---

st.set_page_config(page_title="Multi-Agent Sales System", layout="wide")
st.title("🚗 Multi-Agent Sales System")
st.write("Powered by Groq, Gemini, and LangChain")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi, I'm John! How can I help you find the perfect car today?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What are you looking for?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = agent_executor.invoke({"input": prompt})
                st.markdown(response['output'])
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response['output']})
            except Exception as e:
                error_message = f"Sorry, I encountered an error: {e}. Please try rephrasing your question."
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})
