
# Cut scenes in pygame

These scripts demonstrate a simple method of writing and managing cut scenes in python/pygame.

Video explanation can be found [here](https://www.youtube.com/watch?v=Mp57mHfOXTw)

## Cut Scene Manager

A utility class for interfacing between the main game loop and cut scenes

## Cut Scene Structure

Cut scenes are defined as classes with methods **update** and **draw**. The general structure is to partition these methods into different *steps*, where each *step* defines a part of the cut scene.
