from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai

openai.api_key = 'your_key'


def chat_with_model(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=500,
        temperature=0.7,
        n=1,
        stop=None
    )

    reply = response.choices[0].text.strip()
    return reply


@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        response = chat_with_model(user_input)
        return render(request, 'chat.html', {'response': response})
    else:
        return render(request, 'chat.html')
