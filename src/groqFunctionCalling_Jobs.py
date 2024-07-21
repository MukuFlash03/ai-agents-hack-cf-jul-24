from groq import Groq
import os
import json
from dotenv import load_dotenv
from easyApplAI import easyApplAIEntrypoint

load_dotenv()

GROQ_API_KEY=os.getenv('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY)
MODEL = 'llama3-70b-8192'


def get_response(question):
    return json.dumps({"question": question})

# def calculate(expression):
#     """Evaluate a mathematical expression"""
#     try:
#         result = eval(expression)
#         return json.dumps({"result": result})
#     except:
#         return json.dumps({"error": "Invalid expression"})

def initiate_jobs_apply(task):
    taskComplete = easyApplAIEntrypoint()
    return json.dumps({"taskComplete": taskComplete})

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_response",
            "description": "Responding a casual chat",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "Responding a casual chat",
                    }
                },
                "required": ["question"],
            },
        },
    },
    # {
    #     "type": "function",
    #     "function": {
    #         "name": "calculate",
    #         "description": "Evaluate a mathematical expression",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "expression": {
    #                     "type": "string",
    #                     "description": "The mathematical expression to evaluate",
    #                 }
    #             },
    #             "required": ["expression"],
    #         },
    #     },
    # },
    {
        "type": "function",
        "function": {
            "name": "initiate_jobs_apply",
            "description": "Apply to Saved Jobs from LinkedIn",
            "parameters": {
                "type": "object",
                "properties": {
                    "task": {
                        "type": "string",
                        "description": "The task to apply to saved jobs from LinkedIn",
                    }
                },
                "required": ["task"],
            },
        },
    }
]

def run_conversation(user_prompt):
    # You are a function calling LLM that calls functions and executes the tasks in them, OR you can use the data extracted from the functions to answer questions around general queries.
    # You are a function calling LLM that calls functions and executes the tasks in them, OR you can use the data extracted from the functions to answer questions around general queries. Also please keep the final output response from the function calls to just 1-2 lines so it is concise and brief.
    messages = [
        {
            "role": "system",
            "content": """
                    You are a function calling LLM that calls functions and executes the tasks in them, OR you can use the data extracted from the functions to answer questions around general queries. Also please keep the final output response from the function calls to just 2-3 lines so it is concise and brief.
                """
        },
        {
            "role": "user",
            "content": user_prompt,
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        # tool_choice="required",
        max_tokens=4096
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        available_functions = {
            "get_response": get_response,
            "initiate_jobs_apply": initiate_jobs_apply
        }
        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(**function_args)
            # function_response = function_to_call(
            #     task=function_args.get("task")
            # )
            
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            })

        second_response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )
        final_response = second_response.choices[0].message.content
    else:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=4096
        )
        messages.append(response_message)
        final_response = response.choices[0].message.content

    return final_response

def run_tests_e2e(text):
    # user_prompt = "Can you please apply to my saved jobs from LinkedIn?"
    # print(run_conversation(user_prompt))
    # user_prompt = "It's pretty late now, past midnight here. What should I do to fall asleep early?"
    user_prompt = text
    # print(run_conversation(user_prompt))
    final_response = run_conversation(user_prompt)
    return final_response

if __name__ == "__main__":
    # user_prompt = "Can you please apply to my saved jobs from LinkedIn?"
    # print(run_conversation(user_prompt))
    user_prompt = "It's pretty late now, past midnight here. What should I do to fall asleep early?"
    print(run_conversation(user_prompt))