# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  The first time I ran it, the game looked like a simple number guessing game with a dev section that provides the correct answer. One bug I noticed was the hints being swapped. It should say higher when the number is lower and lower when the guess is higher. But they are backwards, so it says lower when a low guess is made and higher when a high guess is made. Another bug I noticed is when a guess is entered after an incorrect guess, clicking submit removes the hint message and counts the attempt, however, the value isn't actually registered. So even if you guess the correct value, it quietly counts as another incorrect attempt.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used claude for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  I came under the assumption that the secret number would change after every button press. I asked AI why that might be. It came back with the response that there is already a guard against that. I verified it by going back and actually testing out the different buttons and something I thought was a bug turned out to be fine. The number only changed when new game was pressed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I asked AI to help me fix the hint logic and it made the fix correctly. But the fix was only for half of it. It completly missed the other spot that needed the fix just a few lines down. I had to go back and ask it again to fix that spot.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I made a unit test and if that passed, I checked it manually.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  One of the tests I ran was the pre-implemented test_winning_guess. It actually failed and I learned that the outcome it's testing for is part of a tuple and it was failing because it was expecting a normal variable.

- Did AI help you design or understand any tests? How?

  It helped me do both. It helped me understand by showing me why the pre-implemented tests were failing. It helped me design by helping me implement the tests needed for the bugs that were found.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  I am assuming that at one point there was no guard because I never ran into this issue. The guard against reruns was already in place, so the only time the secret number changed was when it was supposed to when new game was pressed.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Think of it like a webpage that with any interaction or button click, the python script reruns from the top. So every variable is then reset. That is, except for session state, which saves anything that is saved into state.

- What change did you make that finally gave the game a stable secret number?

  I am assuming it would be adding that guard as previously mentioned.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

    I wan't to get a better habit at more meaningful and more often git commits. I sometimes have the habit of making very many changes before finally making a commit.

- What is one thing you would do differently next time you work with AI on a coding task?

  I want to try and make even more precise AI prompts. I think I would get a dual benefit from this. One would be more accurate responses and the other would be an increased capacity for learning. I could actually keep learning instead of mindlessly copy and pasting code.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

    I have increased confidence in using AI in a project capacity. Not only can I use it for ideas, I can also use it to get a layout on how the project works.
