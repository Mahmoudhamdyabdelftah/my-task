import random
word_list =[ "python","developer","programming","game","scramble" ]
original_word = random.choice(word_list)
letters =list(original_word)
random.shuffle(letters)
scrambled_word=''.join(letters)
attempts=5
print("welcome to the word scramble game ")
print(f"scrambled woed: {scrambled_word}")
while attempts>0:
   guess = input("What is the original word? ").strip().lower()
   if guess == "":
        print ("input is empty. please try again.")
        continue
   if guess ==original_word:
        print("congartulations! you gussed the word correctly")
        break
   else:
        attempts -=1
        if attempts > 0:
            print(f"incorrect guess.you have {attempts}attempts left.")
        else:
                     print(f"yot have run out of attempts. the original word was: {original_word}")

