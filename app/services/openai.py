from openai import OpenAI
import time
import json
from dotenv import load_dotenv
import os
from app.repository.thread_repository import ThreadRepository
from app.services.functions.quizz.quizz import display_quiz
from app.services.functions.quizz.quizz_interface import function_json

load_dotenv()


def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()


MATH_ASSISTANT_ID = os.environ.get("OPENAI_ASSISTANT_ID")
client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

assistant = client.beta.assistants.update(
    MATH_ASSISTANT_ID,
    tools=[
        {"type": "code_interpreter"},
        {"type": "retrieval"},
        {"type": "function", "function": function_json},
    ],
)


def submit_message(assistant_id, thread, user_message, use_custom_function=False):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )


def get_messages(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")


def create_thread_and_run(user_input, thread=None):
    if thread is None:
        thread = client.beta.threads.create()
        with ThreadRepository() as repo:
            repo.create_thread(identifier=thread.id)
    run = submit_message(MATH_ASSISTANT_ID, thread, user_input)
    return thread, run


def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
        if run.status == "requires_action":
            print('requires_action statement')
            tool_call = run.required_action.submit_tool_outputs.tool_calls[0]
            arguments = json.loads(tool_call.function.arguments)
            name = tool_call.function.name
            responses = display_quiz(arguments["title"], arguments["questions"])

            print("Function Name:", name)
            print("Function Arguments:", arguments)

            run = client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=[
                    {
                        "tool_call_id": tool_call.id,
                        "output": json.dumps(responses),
                    }
                ],
            )
    return run
