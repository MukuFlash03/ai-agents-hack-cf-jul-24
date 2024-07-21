from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY)
MODEL = 'llama3-70b-8192'


def get_response(question):
    return json.dumps({"question": question})

def mutual_fund(fund_name):
    if "growth" in fund_name.lower():
        return json.dumps({"fund_name": "Growth Fund", "nav": 150.75, "1_year_return": "12.5%"})
    elif "income" in fund_name.lower():
        return json.dumps({"fund_name": "Income Fund", "nav": 102.50, "1_year_return": "8.4%"})
    else:
        return json.dumps({"fund_name": fund_name, "details": "unknown"})

def upi(transaction_id):
    if transaction_id == "TX123":
        return json.dumps({"transaction_id": "TX123", "status": "Success", "amount": 1500})
    else:
        return json.dumps({"transaction_id": transaction_id, "status": "Pending"})

def health_insurance(policy_number):
    if policy_number == "HP001":
        return json.dumps({"policy_number": "HP001", "coverage": "500000", "premium": "12000", "status": "Active"})
    else:
        return json.dumps({"policy_number": policy_number, "details": "unknown"})

def cash_loan(loan_id):
    if loan_id == "LN123":
        return json.dumps({"loan_id": "LN123", "amount": "20000", "interest_rate": "12%", "status": "Approved"})
    else:
        return json.dumps({"loan_id": loan_id, "details": "unknown"})


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
    {
        "type": "function",
        "function": {
            "name": "mutual_fund",
            "description": "Get the details of a mutual fund",
            "parameters": {
                "type": "object",
                "properties": {
                    "fund_name": {
                        "type": "string",
                        "description": "The name of the mutual fund (e.g. 'Growth Fund')",
                    }
                },
                "required": ["fund_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "upi",
            "description": "Get the status of a UPI transaction",
            "parameters": {
                "type": "object",
                "properties": {
                    "transaction_id": {
                        "type": "string",
                        "description": "The ID of the UPI transaction (e.g. 'TX123')",
                    }
                },
                "required": ["transaction_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "health_insurance",
            "description": "Get the details of a health insurance policy",
            "parameters": {
                "type": "object",
                "properties": {
                    "policy_number": {
                        "type": "string",
                        "description": "The policy number of the health insurance (e.g. 'HP001')",
                    }
                },
                "required": ["policy_number"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "cash_loan",
            "description": "Get the details of a cash loan",
            "parameters": {
                "type": "object",
                "properties": {
                    "loan_id": {
                        "type": "string",
                        "description": "The ID of the cash loan (e.g. 'LN123')",
                    }
                },
                "required": ["loan_id"],
            },
        },
    }
]

def run_conversation(user_prompt):
    messages = [
        {
            "role": "system",
            "content": "You are a function calling LLM that uses the data extracted from the functions to answer questions around mutual funds, UPI transactions, health insurance policies, and cash loans."
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
        max_tokens=4096
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        available_functions = {
            "get_response": get_response,
            "mutual_fund": mutual_fund,
            "upi": upi,
            "health_insurance": health_insurance,
            "cash_loan": cash_loan,
        }
        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(**function_args)
            
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

if __name__ == "__main__":
    user_prompt = "Tell me about the Growth Mutual Fund"
    print(run_conversation(user_prompt))

    user_prompt = "It's pretty late now, past midnight here. What should I do to fall asleep early?"
    print(run_conversation(user_prompt))