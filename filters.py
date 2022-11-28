def get_recent_repeated_responses(chatbot, conversation, sample=10, threshold=3, quantity=3):
    from collections import Counter
    conversation_statements = list(chatbot.storage.filter(
        conversation=conversation,
        order_by=['id']
    ))[sample * -1:]

    text_of_recent_responses = [
        statement.text for statement in conversation_statements
    ]

    counter = Counter(text_of_recent_responses)

    most_common = counter.most_common(quantity)

    return [
        counted[0] for counted in most_common
        if counted[1] >= threshold
    ]