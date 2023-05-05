import openai 
import pyytsx3 #convert text to speak 
import speech_recognition as sr # transcribe audio to text

#set your openAI API key
openai.api_key = "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"

#initialize the test-to-speech engine
engine=pyytsx3.init()
#func to convert audio to text for python code to understand 
def transcribe_audio_to_text(filename):
     recongnizer =sr.Recognixer() #perfrom speech recognition 
     with sr.AudioFile(filename) as source:
          audio=recongnizer.record(source)
     try:
          return recongnizer.recognize_google(audio)
     except:
          print("skipping unknown error")
          
def generate_response(prompt):
     response= openai.completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokend=4000,
          n=1,
          stop=None,
          temperature=0.5,
     )
     return response["choices"][0]["text"]

def speak_text(text):
     engine.say(text)
     engine.runAndWait()

def main():
     while True:
          #wait for user to say "genius"
            print("say 'genius' to start recording your question...")
            with sr.Microphone() as source:
               recognizer = sr.Recognizer()
               audio= recognizer.listen(source)
            try:
                    transcription =recognizer.reconize_google(audio)
                    if transcription.lower()=="genius":
                    # record audio
                       filename="input.wav"
                       print("say your question...")
                       with sr.Microphone() as source:
                         recognizer=sr.Recognizer()
                         source.pause_threshold =1
                         audio =recognizer.listen(source, phase_time_limit=None,timeout=None)
                         with open(filename,"wb") as f:
                              f.wrute(audio.get_wav_data())
                         
                         # transcribe audio to text


                              text = transcribe_audio_to_text(filename)
                              if text:
                                  print(f"you said:{text}")

                                  #generate response using GPT-3
                                  response = generate_response(text)
                                  print(f"GPT-3 says :{response}")
                              
                                 # read response using text-to-speech
                                  speak_text(response)
                                  
            except Exception as e:
                   print("An error : {}".format{e})
            
                                    

                    
if __name__=="__main__":
      main()