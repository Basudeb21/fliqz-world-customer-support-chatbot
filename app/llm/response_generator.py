# # app/llm/response_generator.py

# from app.prompts.reply_prompt import (
#     build_prompt
# )

# from app.llm.model import generate

# from app.rag.retriever import (
#     retrieve_context
# )


# def generate_reply(
#     question: str,
#     history: str
# ):

#     context = retrieve_context(
#         question
#     )

#     prompt = build_prompt(
#         context=context,
#         history=history,
#         question=question
#     )

#     response = generate(
#         prompt
#     )

#     return response


from app.prompts.reply_prompt import (
    build_prompt
)

from app.llm.model import generate


def generate_reply(
    question: str,
    history: str,
    context: str
):

    prompt = build_prompt(
        context=context,
        history=history,
        question=question
    )

    print("\n========== PROMPT ==========")
    print(prompt)
    print("============================\n")

    return generate(prompt)