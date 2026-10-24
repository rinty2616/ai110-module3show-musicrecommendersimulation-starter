# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

## 2. Intended Use

My music recommendation system suggests songs based on a user's favorite genre, favorite mood, and preferred energy level.

This project is designed for classroom learning. It shows how a simple recommendation algorithm works.

It is not intended to replace professional music recommendation systems such as Spotify.

## 3. How the Model Works

My program reads songs from a CSV file and compares them with a user's music preferences.

It gives:
- 2 points for a matching genre.
- 1 point for a matching mood.
- Up to 1 point based on energy similarity.

The highest possible score is 4 points.

The program calculates a score for every song, ranks the songs from highest to lowest, and recommends the top 5.

I implemented the scoring and ranking functions from the starter project.

## 4. Data

My dataset contains 15 songs.

The original dataset included 10 songs, and I added 5 more songs to increase diversity.

The dataset includes pop, rock, lofi, jazz, reggae, EDM, country, R&B, classical, and other genres.

Each song contains information such as genre, mood, energy, tempo, valence, danceability, and acousticness.

My current scoring algorithm uses genre, mood, and energy.

One limitation is that 15 songs are not enough to represent everyone's music preferences.

## 5. Strengths

My system works well when a song closely matches the user's preferences.

For the High-Energy Pop profile, **Sunrise City** ranked first with 3.92 points.

For the Chill Lofi profile, **Library Rain** ranked first with 3.95 points.

For the Intense Rock profile, **Storm Runner** ranked first with 3.96 points.

These results make sense because the top songs closely match the requested genre, mood, and energy.

The system also explains why it recommends each song.

## 6. Limitations and Bias

My system gives more importance to genre than mood, which may create a filter bubble.

Some genres have only one song in the dataset, so users who enjoy those genres have fewer choices.

The algorithm does not currently use listening history, likes, or skips.

It also does not use all the available song features, such as danceability and acousticness.

These limitations may prevent the system from recommending other songs a user could enjoy.

## 7. Evaluation

I tested my recommendation system with three different user profiles:

1. High-Energy Pop
2. Chill Lofi
3. Intense Rock

I checked the top 5 songs for each profile and compared their scores.

**Comparison 1: High-Energy Pop vs. Chill Lofi**

High-Energy Pop recommended Sunrise City first, while Chill Lofi recommended Library Rain. This makes sense because the users prefer different music styles and energy levels.

**Comparison 2: High-Energy Pop vs. Intense Rock**

High-Energy Pop recommended Sunrise City first, while Intense Rock recommended Storm Runner. Both profiles prefer high energy, but different genres and moods produce different recommendations.

**Comparison 3: Chill Lofi vs. Intense Rock**

Chill Lofi recommended softer, lower-energy music, while Intense Rock recommended louder, higher-energy music.

**Scoring Experiment**

I also tested what happened when I changed the scoring weights.

Original scoring:
- Genre: 2 points
- Mood: 1 point
- Energy: up to 1 point

Experimental scoring:
- Genre: 1 point
- Mood: 1 point
- Energy: up to 2 points

For the Intense Rock profile, Storm Runner's score changed from 3.96 to 3.92, while Gym Hero increased from 1.98 to 2.96.

For the Chill Lofi profile, Spacewalk Thoughts moved above Focus Flow when energy became more important.

This showed me that changing the scoring weights can change the recommendations and rankings.

After my experiment, I restored the original scoring rules.

I also ran automated Python tests, and both tests passed.

## 8. Future Work

If I improve this project, I would:

1. Add more songs and genres to the dataset.
2. Include user likes, skips, and listening history.
3. Improve the scoring system to provide more diverse recommendations.

These improvements could make the recommendations more personalized.

## 9. Personal Reflection

During this project, I learned how a music recommendation system uses data and scoring rules to suggest songs.

I learned how to load data from a CSV file, calculate scores, and rank songs using Python.

AI tools helped me understand the code, build the functions, and troubleshoot errors. I checked the results by running the program and testing it myself.

I also learned how to fix import errors and problems caused by using different preference names in my Python files.

The most surprising part was seeing how changing a few scoring numbers could affect song recommendations.

This project helped me understand how simple algorithms can create personalized experiences.

In the future, I would like to add more songs and use real user feedback to improve my recommendation system.