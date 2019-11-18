#Song chooser
import webbrowser #Used for opening website links

print("This is a program that will select a song depending on how you are feeling!")
print("How are you feeling?\na: Sad\nb: Really Sad\nc: Happy\nd: High on cocaine\ne: Saucy")

mood = str.lower(input())

while(mood != "a" 
and mood != "b" 
and mood != "c" 
and mood !="d" 
and mood != "e"):
    #If one of the options was not chosen then ask again
    print("Invalid selection\nPlease re-enter an option.")
    print("How are you feeling?\na: Sad\nb: Really Sad\nc: Happy\nd: High on cocaine\ne: Saucy")
    mood = str.lower(input())
    

if(mood == "a"):
    #Brokedown Palace - Grateful Dead
    webbrowser.open("https://www.youtube.com/watch?v=A9uyMjzmT3k")

elif(mood == "b"):
    #Black Muddy River - Grateful Dead RIP Jerry
    webbrowser.open("https://www.youtube.com/watch?v=6sFyRQPraJ8")

elif(mood == "c"):
    #Eyes of the World - Grateful Dead
    webbrowser.open("https://www.youtube.com/watch?v=kuSJ0djewQU")

elif(mood == "d"):
    #Casey Jones - Grateful Dead
    webbrowser.open("https://www.youtube.com/watch?v=_x2m6i4KFqg")

else:
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")   