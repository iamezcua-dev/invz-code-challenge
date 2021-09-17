# INVZ Code Challenge

## EVOLUTION GAME

In a 6 X 6 board with cells, a cell can be either DEAD or ALIVE (use 0 or 1).

At each iteration of the game, a DEAD cell can become ALIVE if there are 2 or more ALIVE cells adjacent to it (
horizontally or vertically).

* e.g. with 3 x 3 grid:

```text
   0 0 1 -> 0 1 1
   0 1 0    1 1 1
   1 0 0    1 1 0
```

Note: ALIVE cells cannot become DEAD (i.e. once ALIVE they remain ALIVE for the duration of the game).

## The Challenge ...

1. Create an application that starts with a 6 X 6 board with 10 alive cells (randomly distributed);
2. Run the game and "evolving" the board.
3. Print the board at each iteration (with a short delay).
4. Stop the game.
