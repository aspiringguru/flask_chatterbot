from chatterbot import ChatBot
import time

'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

chatbot = ChatBot(
    'Export Example Bot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# First, lets train our bot with some data
print("starting training")
start = time.time()
chatbot.train('chatterbot.corpus.english')
end = time.time()
print("time to train on chatterbot.corpus.english: "+str(end - start))

# Now we can export the data to a file
chatbot.trainer.export_for_training('./my_export_chatterbot.corpus.english.json')
