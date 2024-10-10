# hopflied-associative-memory-from-scratch
A rudimentary implementation of Hopfield network (aka Associative Memory) trained using Hebbian learning algorithm. This is to celebrate Hopfield-Hinton's winning of Noble Prize in Physics 2024. Also to remind me that how poor I was at googling back in 2012.

Deliberately used very declarative style and put everything inside the notebook. This is just a demo to color the differences between modern learning and how learning used to look like in the 80s. 

Hopfield networks are known to perform poorly with random patterns. Due to the associative memory, the location of the prominent aspects of the pattern within a string (or image for that matter) influences the performance a lot. The symmetry, strong internal organization all affect the updates via Hebbian learning, sunsequently affects the performance of the retrieval.

This is a good study on the recent advancements in Hopfield networks: https://www.nature.com/articles/s42254-023-00595-y
