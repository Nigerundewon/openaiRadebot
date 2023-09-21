import openai;

text = "";
openai.api_key = "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";
mess = [
        {"role": "system", "content": "Tu es une assistant très utile qui va m'aider à réaliser la tâche que je t'assignerais"}
    ];


def generation(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        temperature=0.7
    )
    return response.choices[0]['message']['content'];

while True:
    text = input("Moicoubeh : ");
    user = {"role": "user", "content": text};
    mess.append(user);
    text = generation(mess);    
    print(f"Chat GPPute : {text}");
    assistant = {"role": "assistant", "content": text};
    mess.append(assistant);