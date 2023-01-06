# container_size: A vector of length 3 describing the size of the container in the x, y, z dimension.
# item_size_set:  A list records the size of each item. The size of each item is also described by a vector of length 3.

#container_size = [587, 233, 220]
container_size = [10,10,10]
lower = 1
higher = 5
resolution = 1
item_size_set = []
for i in range(lower, higher + 1):
    for j in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
        for k in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
                item_size_set.append((i * resolution, j * resolution , k *  resolution))
# for i in range(20):
#     item_size_set.append((2,2,2))
# for i in range(20):
#     item_size_set.append((3,3,3))
# for i in range(20):
#     item_size_set.append((1,1,1))
# for i in range(20):
#     item_size_set.append((4, 4, 4))
# for i in range(20):
#     item_size_set.append((5, 5, 5))
# for i in range(4):
#     item_size_set.append((3,2,2))
# for i in range(2):
#     item_size_set.append((2,7,2))
# for i in range(4):
#     item_size_set.append((2,2,4))
# for i in range(4):
#     item_size_set.append((1,2,3))
# for i in range(1):
#     item_size_set.append((6,2,4))
# for i in range(2):
#     item_size_set.append((3,2,3))
# for i in range(4):
#     item_size_set.append((2,2,3))
# for i in range(10):
#     item_size_set.append((2,2,2))
# for i in range(4):
#     item_size_set.append((1,3,3))
# for i in range(1):
#     item_size_set.append((7,2,4))
# for i in range(2):
#     item_size_set.append((3,2,5))
# for i in range(4):
#     item_size_set.append((3,1,4))
# for i in range(5):
#     item_size_set.append((6,3,2))
# for i in range(1):
#     item_size_set.append((5,4,5))


# If you want to sample item sizes from a uniform distribution in continuous domain,
# type --sample-from-distribution in your command line.
