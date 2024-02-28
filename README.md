# Boids
Boid simulation with Hunters

The Boids algorithm is a computational model for simulating the flocking behavior of birds, developed by Craig Reynolds in 1986. It simulates the collective motion of a group of entities (called "boids") by defining simple rules that govern their behavior. These rules are based on three main principles: separation, alignment, and cohesion.

Here's an overview of the key components and principles of the Boids algorithm:

Boid: Each individual entity in the simulation is referred to as a "boid." Boids are typically represented as points or objects in a two-dimensional space.

Separation: Boids try to maintain a minimum separation distance from nearby boids to avoid collisions and overcrowding. They adjust their velocity to steer away from other boids that are too close.

Alignment: Boids align their velocity with the average velocity of nearby boids. This encourages them to move in the same direction as their neighbors, promoting a sense of cohesion and group movement.

Cohesion: Boids are attracted to the center of mass of nearby boids. They adjust their velocity to move towards the average position of neighboring boids, promoting group cohesion and flocking behavior.

Implementation: The Boids algorithm is typically implemented as a simulation loop where each boid updates its position and velocity based on the three rules (separation, alignment, cohesion) and the positions and velocities of nearby boids. The algorithm is usually applied to a large number of boids to simulate complex collective behaviors.

Additional Behaviors: In addition to the core principles of separation, alignment, and cohesion, variations of the Boids algorithm may incorporate additional behaviors such as obstacle avoidance, goal-seeking behavior, predator evasion, or hierarchical flock structures.

Emergent Behavior: By following simple rules based on local interactions with neighboring boids, complex collective behaviors emerge at the group level, such as flocking, swarming, schooling, herding, or milling patterns observed in nature.

The Boids algorithm has been widely used in computer graphics, artificial intelligence, robotics, and simulation systems to model and simulate collective behaviors in various applications, including video games, virtual environments, animation, robotics, and computational biology. It provides a simple yet effective framework for simulating realistic group behaviors inspired by nature.

![](https://github.com/PieterES/Boids/blob/main/video.gif)
