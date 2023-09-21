import openai;
import json;

text = "";
openai.api_key = "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";
mess = [
        {"role": "system", "content": "Radebot est une reproduction artificielle de son créateur"}
    ];


def generation(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        temperature=0.7
    )
    return response.choices[0]['message']['content'];

def chatbot():
    text = input("Moicoubeh : ");
    user = {"role": "user", "content": text};
    mess.append(user);
    text = generation(mess);    
    print(f"Chat GPPute : {text}");
    assistant = {"role": "assistant", "content": text};
    mess.append(assistant);

def fineTune(questionFile, writeFile):
    writefile = open(writeFile, 'w')
    file =  open(questionFile,'r')
    questions = file.readlines()
    for line in questions:
        answer = input(f"{line}\n")
        finetuningLine = {"messages": [{"role": "system", "content": "Radebot est une reproduction artificielle de son créateur"}, {"role": "user", "content": f"{line.strip()}"}, {"role": "assistant", "content": f"{answer}"}]}
        writefile.writelines(json.dumps(finetuningLine) + "\n")
        print(finetuningLine)

def createFineTuned():
    #f = openai.File.create(
     #  file=open('C:/Users/radew/Bureau/openai/openaiRadebot/finetuning.jsonl'),
      # purpose='fine-tune',
    #)
    f2 = openai.FineTuningJob.create(training_file="file-FYPII6bJeBhuCfHpro1aQIla", model="gpt-3.5-turbo")
    print(f2)
    #response = openai.FineTuningJob.retrieve("ftjob-7YQOSUNGh80E39rR70KpV96O")

#print(response)

#fineTune("C:/Users/radew/Bureau/openai/openaiRadebot/iaFineTuningQuestions.txt","C:/Users/radew/Bureau/openai/openaiRadebot/finetuning.jsonl")

createFineTuned()