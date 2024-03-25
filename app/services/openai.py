from openai import OpenAI
import time
import json
from dotenv import load_dotenv
import os
from app.repository.thread_repository import ThreadRepository
from app.services.functions.ask_user_auth_information.ask_user_auth_information import ask_user_register_auth_function
from app.services.functions.ask_user_register_information.ask_user_register_information_description import \
    ask_user_register_information_function
from app.services.functions.authenticate_user.authenticate_user import authenticate_user
from app.services.functions.authenticate_user.authentificate_user_description import authenticate_user_function
from app.services.functions.create_workout.create_workout import create_workout
from app.services.functions.create_workout.create_workout_description import create_workout_function
from app.services.functions.get_exercises.get_exercises import get_exercises
from app.services.functions.get_exercises.get_exercises_description import get_exercises_function
from app.services.functions.get_user_info.get_user_info import get_user_info
from app.services.functions.get_user_info.get_user_info_description import get_user_infos_function
from app.services.functions.get_workouts.get_workouts import get_workouts
from app.services.functions.get_workouts.get_workouts_description import get_workouts_function
from app.services.functions.quizz.quizz import display_quiz
from app.services.functions.quizz.quizz_description import function_json
from app.services.functions.register_user.register_user import register_user
from app.services.functions.register_user.register_user_description import register_user_function

load_dotenv()

MATH_ASSISTANT_ID = os.environ.get("OPENAI_ASSISTANT_ID")
client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

assistant = client.beta.assistants.update(
    MATH_ASSISTANT_ID,
    tools=[
        {"type": "code_interpreter"},
        {"type": "retrieval"},
        {"type": "function", "function": function_json},
        {"type": "function", "function": register_user_function},
        {"type": "function", "function": get_exercises_function},
        {"type": "function", "function": authenticate_user_function},
        {"type": "function", "function": create_workout_function},
        {"type": "function", "function": get_workouts_function},
        {"type": "function", "function": get_user_infos_function},
        {"type": "function", "function": ask_user_register_information_function},
        {"type": "function", "function": ask_user_register_auth_function},
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


def create_thread_without_run():
    thread = client.beta.threads.create()
    with ThreadRepository() as repo:
        repo.create_thread(identifier=thread.id)

    return thread.id


def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)

        if run.status == "requires_action":
            tool_call = run.required_action.submit_tool_outputs.tool_calls[0]
            arguments = json.loads(tool_call.function.arguments)
            name = tool_call.function.name

            if name == "display_quiz":
                responses = display_quiz(arguments["title"], arguments["questions"])
                # print("Function Name:", name)
                # print("Function Arguments:", arguments)

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

            if name == 'register_user':
                arguments = json.loads(tool_call.function.arguments)
                responses = register_user(
                    username=arguments['username'],
                    email=arguments['email'],
                    password=arguments['password']
                )

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

            if name == 'get_exercises':
                arguments = json.loads(tool_call.function.arguments)
                responses = get_exercises()

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

            if name == 'get_workouts':
                arguments = json.loads(tool_call.function.arguments)
                responses = get_workouts(token=arguments['token'])

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

            if name == 'authenticate_user':
                arguments = json.loads(tool_call.function.arguments)
                responses = authenticate_user(
                    identifier=arguments['identifier'],
                    password=arguments['password']
                )

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

            if name == 'create_workout':
                arguments = json.loads(tool_call.function.arguments)
                responses = create_workout(
                    exercise=arguments['exercise'],
                    rep=arguments['rep'],
                    date=arguments['date'],
                    weight=arguments['weight'],
                    user_id=arguments['users_permissions_user'],
                    token=arguments['token'])

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

            if name == 'get_user_info':
                arguments = json.loads(tool_call.function.arguments)
                responses = get_user_info(arguments['token'])

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

            if name == 'ask_user_auth_information':
                run = client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread.id,
                    run_id=run.id,
                    tool_outputs=[
                        {
                            "tool_call_id": tool_call.id,
                            "output": json.dumps({"message": "Demande a l'utilisateur de renseigner sont email et mot "
                                                             "de passe avant continuer sont"
                                                             "authentification à l'application"})

                        }
                    ],
                )

            if name == 'ask_user_register_information':
                run = client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread.id,
                    run_id=run.id,
                    tool_outputs=[
                        {
                            "tool_call_id": tool_call.id,
                            "output": json.dumps({"message": "Demande a l'utilisateur de renseigner son username, "
                                                             "email et mot de passe avant la création de son"
                                                             "compte"})
                        }
                    ],
                )

    return run
