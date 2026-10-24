# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

My music recommendation system recommends songs based on the user's favorite genre, favorite mood, and preferred energy level.

The system gives 2 points for a genre match, 1 point for a mood match, and up to 1 point for energy similarity.

It calculates scores for all 15 songs and recommends the top 5 songs with the highest scores.

One limitation is that the system may favor certain genres and miss other songs the user might enjoy.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Top recommendations:

Sunrise City - Score: 3.98
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.98)

Gym Hero - Score: 2.87
Because: Genre match (+2.0), Energy similarity (+0.87)

Rooftop Lights - Score: 1.96
Because: Mood match (+1.0), Energy similarity (+0.96)

Electric Dreams - Score: 1.85
Because: Mood match (+1.0), Energy similarity (+0.85)

Night Drive Loop - Score: 0.95
Because: Energy similarity (+0.95)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
## Evaluation: Three Music Profiles

```text
High-Energy Pop



Chill Lofi



Intense Rock
```


