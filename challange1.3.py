from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession

model = ChatModel("chat-bison")
response = model.chat([
  ChatSession(
    context="You are philosophy bot.",
    examples=[
      ChatExample(
        input=ChatMessage(content="1 + 1"),
        output=ChatMessage(content="2")
      )
    ],
    messages=[
      ChatMessage(author="USER", content="How much wood can a woodchuck chuck?"),
    ],
  )
], temperature=0.2)

print(response.responses[0].candidates[0].message.content)
