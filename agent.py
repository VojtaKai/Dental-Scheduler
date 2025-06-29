from typing import List, Dict, Any
import json
from openai import Client

class ReactAgent:
    """A ReAct (Reason and Act) agent that handles multiple tool calls."""
    
    def __init__(self, client: Client, model: str = "gpt-4o", available_functions: dict = {}, tools: List[Dict[str, Any]] = [], max_iterations: int = 10):
        self.client = client
        self.model = model
        self.available_functions = available_functions
        self.tools = tools
        self.max_iterations = max_iterations  # Prevent infinite loops
        
    def run(self, messages: List[Dict[str, Any]]) -> str:
        """
        Run the ReAct loop until we get a final answer.
        
        The agent will:
        1. Call the LLM
        2. If tool calls are returned, execute them
        3. Add results to conversation and repeat
        4. Continue until LLM returns only text (no tool calls)
        """
        iteration = 0
        
        while iteration < self.max_iterations:
            iteration += 1
            print(f"\n--- Iteration {iteration} ---")
            
            # Call the LLM
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.tools,
                tool_choice="auto",
                parallel_tool_calls=False
            )
            
            response_message = response.choices[0].message
            print(f"LLM Response: {response_message}")
            
            # Check if there are tool calls
            if response_message.tool_calls:
                # Add the assistant's message with tool calls to history
                messages.append(response_message)
                
                # Process ALL tool calls (not just the first one)
                for tool_call in response_message.tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    tool_id = tool_call.id
                    
                    print(f"Executing tool: {function_name}({function_args})")
                    
                    # Call the function
                    function_to_call = self.available_functions[function_name]
                    function_response = function_to_call(**function_args)
                    
                    print(f"Tool result: {function_response}")
                    
                    # Add tool response to messages
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_id,
                        "content": json.dumps(function_response),
                    })
                
                # Continue the loop to get the next response
                continue
                
            else:
                # No tool calls - we have our final answer
                final_content = response_message.content
                
                # Add the final assistant message to history
                messages.append({
                    "role": "assistant",
                    "content": final_content
                })
                
                print(f"\nFinal answer: {final_content}")
                return final_content
        
        # If we hit max iterations, return an error
        return "Error: Maximum iterations reached without getting a final answer."