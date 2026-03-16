# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.

   The games purpose is to pick a difficulty level and then proceed to try and guess a secret number in a certain amount of guesses, giving hints on whether your guess was higher or lower.

- [ ] Detail which bugs you found.

   The number range for two of the diffiulty levels were swapped.

   The hint messages were backwards, guessing higher returned the hint to guess higher and guessing lower returned the hint to guess lower.

   On even numbered attempts, the secret was cast to a string. When the guess and secret were then compared, it would return false because numerically that comparison is incorrect. This resulted in it being impossible to win on an even numbered attempt.

   Wrong guesses on even numbered attempts rewarded 5 points.

   The "Guess a number between" message used the hard coded values of 1 and 100 no matter the difficulty.

   New Game ignored the difficulty as well and was hard coded to always generate an number between 1 and 100.

   New Game didn't reset status or score.

   Attempt limit map values were swapped between easy and normal.

   The attempts counter started at 1.

   The info in the debug display was off.

- [ ] Explain what fixes you applied.

   For the bugs with swapped values, they were just switched to where they should be. 

   The attempt counter starting at one, I just had to change that one to a zero.

   The hard coded value bugs had their values replaced with the correct variables instead of their hard coded value.

   Removed the logic to reward points from the incorrect guess section.

   removed the string cast on secret number.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

   ![alt text](<Screenshot 2026-03-15 at 9.10.29 PM.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
