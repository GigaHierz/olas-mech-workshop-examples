from typing import Any, Dict, Optional, Tuple


def run(**kwargs) -> Tuple[Optional[str], Optional[Dict[str, Any]], Any, Any]:
    """Run the task"""

    # Prepare your response
    prompt = kwargs.get("prompt", None)

    # Implement my tool's logic
    # here
    response = "Dummy response"

    # Optional returns
    transaction = None  # this tool does not generate transactions
    cost_object = None  # this tool does not calculate any costs

    return response, prompt, transaction, cost_object


if __name__ == "__main__":
    prompt = "Dummy prompt"
    response = run(prompt=prompt)
    print(response)