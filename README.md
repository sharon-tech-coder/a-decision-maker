# A Decision Maker

An app that facilitates and helps decision making. 

## Features
- input a decision that user need to make
- input pros and cons
- assign weights to pros and cons
- calculate and display the scores for each options
- filter and display high-scoring options
- saves the decision and allows a revisit and changes
- what-if simulator which generates a decision tree for different scenarios
- a random mode which selects a random option from the provided inputs

## Data Collection Workflow
- name 
- decision to make
- options (2-4)
- choose mode
    | Logic Mode | Random Mode | Intuition Mode |
    - Logic Mode
        0. Blurb: Use your logic to sort out what's the best for you. Let's think of 1-3 pros and cons. 
        1. For option[x], list pros (1-3)
        2. Assign weights to individual pros
        3. For option[x], list cons (1-3)
        4. Assign weights to individual cons
        5. Calculate the weights and print the result based on descending scores of weights
        6. Feedback: Looks like option[a] is your top choice based on seriously reflecting on the pros and cons associated with it. And option[b] could be a plan B.
        7. Try Random Mode or Inituition Mode
    - Random Mode 
        0. Blurb: Press "Start" to get your answer.
        1. Feedback: This is what We choose for you: {random select from options}. Are you happy with the result? (Y/N)
        - Y: Looks like the answer is within you already. Glad I can speak your mind.
        - N: Looks like the answer is within you already. Why not follow your heart?
        2. Try Logic Mode or Intuition Mode
    - Intuition Mode
        0. Blurb: Use your imagination to think about what if you have gone with respective options in your life.
        1. What if you have chosen option[x]? How will your life be different?
        2. Looking ahead, how will that change you in 2 years? 
        3. How will that change you in 5 years? 
        4. How will that change you in 10 years? 
        5. At your deathbed, considering the option you chose at this point of your life, how will you feel?
        6. Feedback: If you choose option[x], the following is what you will be experiencing. In 2 years - {input}. In 5 years - {input}. In 10 years - {input}. At deathbed - {input}. Hopefully that provides you an insight into what's the best for you. But at the end of the day, you are the one to decide what you want for yourself. Follow your heart!
        7. Try Logic Mode or Random Mode
- Back to decision