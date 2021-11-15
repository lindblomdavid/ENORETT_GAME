from kivy import *
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
import random

enWordsLevel1 = ["bil", "kotte", "cykel", "gitarr", "TV"]

ettWordsLevel1 = ["hus", "ljus", "skepp", "bord", "TV-spel", "Träd"]
myGuessedEnWords = []
difficultWords = []
correctWords = []

class EnEttQuiz(Screen):
    def on_pre_enter(self, *args):
        self.getFirstWord()
        

    
    label_start_one = StringProperty(' ') # needed for first word
    

    def getFirstWord(self):

        
        if random.randint(0,1) == 0:
          pickWord = random.choice(enWordsLevel1)
                

        else: 
          pickWord = random.choice(ettWordsLevel1)
  
        self.label_start_one = (pickWord) #word most be within parenthesis
        
    def enClick(self):
      
      #add word to guessed words
      myGuessedEnWords.append(self.ids.word.text)
      #Checks previous word and matches the answer
      if self.ids.word.text in enWordsLevel1:
        self.ids.answer.text = "Correct, Way to go!"
        correctWords.append(self.ids.word.text)
        #remove word from en-list
        enWordsLevel1.remove(self.ids.word.text)
      else:
        self.ids.answer.text = "Sorry that is incorrect"
        #add word to difficult words
        difficultWords.append(self.ids.word.text)
        #remove word from ett-list
        ettWordsLevel1.remove(self.ids.word.text)
             
      #generate new word
      if len(ettWordsLevel1) > 0 and len(enWordsLevel1) > 0:
        enellerett = random.randint(0,1)
        if enellerett == 0:
          self.ids.word.text = random.choice(enWordsLevel1)
        elif enellerett == 1:
          self.ids.word.text = random.choice(ettWordsLevel1)
      else:
        self.ids.Enbutton.disabled = True
        self.ids.Ettbutton.disabled = True
        totalGuesses = len(correctWords) + len(difficultWords)
        self.ids.answer.text = "Game finnished, Well done! Your score was " + str(len(correctWords)) + " out of " + str(totalGuesses)
    
        

      print(myGuessedEnWords)




    #see enbutton
    def ettClick(self):
      myGuessedEnWords.append(self.ids.word.text)

      if self.ids.word.text in ettWordsLevel1:
        self.ids.answer.text = "Correct Way to go!"
        ettWordsLevel1.remove(self.ids.word.text)
        correctWords.append(self.ids.word.text)
        
      else:
        self.ids.answer.text = "Sorry that is incorrect"
        difficultWords.append(self.ids.word.text)
        enWordsLevel1.remove(self.ids.word.text)

      if len(ettWordsLevel1) > 0 and len(enWordsLevel1) > 0:
        enellerett = random.randint(0,1)
        if enellerett == 0:
          self.ids.word.text = random.choice(enWordsLevel1)
        elif enellerett == 1:
          self.ids.word.text = random.choice(ettWordsLevel1)
      else:
        self.ids.Enbutton.disabled = True
        self.ids.Ettbutton.disabled = True
        totalGuesses = len(correctWords) + len(difficultWords)
        self.ids.answer.text = "Game finnished, Well done! Your score was " + str(len(correctWords)) + " out of " + str(totalGuesses)
    

    
       
            


class ScreenManage(ScreenManager):
    pass


kv = Builder.load_file('my.kv')


class MyApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()