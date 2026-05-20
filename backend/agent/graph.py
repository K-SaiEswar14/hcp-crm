from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated
import operator
import os
from dotenv import load_dotenv
from agent.tools import (log_interaction, edit_interaction,
                          search_hcp_history, suggest_followup, analyze_sentiment)

load_dotenv()

tools = [log_interaction, edit_interaction, search_hcp_history,
         suggest_followup, analyze_sentiment]

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, api_key=os.getenv("GROQ_API_KEY")).bind_tools(tools)

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

def call_model(state):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

def should_continue(state):
    last = state["messages"][-1]
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tools"
    return END

workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode(tools))
workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge("tools", "agent")
graph = workflow.compile()