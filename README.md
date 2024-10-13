
This is a fun Python-based game where you compare the number of followers of two random celebrities, social media personalities, or public figures. The game challenges the player to guess who has more followers. The game continues until the player makes a wrong guess.

## How to Play

1. The game will display two random personalities (with descriptions and countries) from the dataset provided.
2. You are asked to guess which of the two has more followers, by choosing option `A` or `B`.
3. If you guess correctly, your score increases, and a new personality is randomly selected to continue the game.
4. If you guess incorrectly, the game ends, and your final score is displayed.

### Example

```text
A: ('Celebrity Name 1', 'Description 1', 'Country 1')
VS
B: ('Celebrity Name 2', 'Description 2', 'Country 2')
Who has more followers? A or B
```

If your guess is correct, you will see:

```text
You are right!
Score: 1
```

Otherwise, the game will end with:

```text
You are wrong!
Final score: [Your Score]
```

## Game Logic

- The game fetches data from `game_data`, which contains details about personalities and their follower counts.
- The comparison of follower counts is done by the `compare()` function, which returns which option has more followers.
- The player guesses which personality has more followers by inputting `A` or `B`.
- If the player guesses incorrectly or the follower counts are equal, the game ends.

