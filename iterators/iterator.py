"""Here, we have created an iterator x_iterator with type <class 'list_iterator'>,
 out of the iterable [1, 2, 3] with type <class 'list'>. This iterator can be thought
 of as a stream of integers coming one after the other. To access the integers,
 we use the built-in next() method to iterate through it, one value at a time.
 Once accessed, the integer is removed from the stream, and the iteration count is
 stored as an internal variable, which allows the iterator to remember its place
 when the next() method is called again. Once the iteration is finished,
 it raises a StopIteration exception, since all the elements have been removed.
 This means the iterator can be traversed only once.Indeed, a for loop is a type of iterator.
 Before a for loop is executed, an iterator object is created in the background,
 then the iteration is performed until the StopIteration exception arises."""
import itertools

iterator_sample = [1, 2, 3, 4, 5, 6, 7, 8]
sample_iter = iter(iterator_sample)
print(sample_iter.__next__())
print(sample_iter.__next__())
print(sample_iter.__next__())
print(sample_iter.__next__())
print(sample_iter.__next__())
for i in sample_iter:
    print(i + 1)

"""They are designed to be memory efficient, so the functions in this module return iterators 
that provide the results in a stream of data. Since data is produced only when it is needed, 
iterables don’t need to be stored in memory"""

# iterator tools
# product()
matrix_x = [2, 5, 3]
matrix_y = [2, 5, 3]
print(list(itertools.product(matrix_y, matrix_x)))
print(list(itertools.permutations(matrix_y)))
print(list(itertools.accumulate(matrix_y)))
print(list(itertools.chain(matrix_y, matrix_x)))
print(list(itertools.compress(matrix_y, matrix_x)))
print(list(itertools.combinations_with_replacement(matrix_y, r=2)))
# print(list(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)])))

ball = itertools.permutations(['red', 'green', 'blue'])
for permutation in ball:
    print(permutation)

balls = itertools.combinations(['red', 'green', 'blue', 'yellow'], r=2)
for combination in balls:
    print(combination)

notes = [50, 20, 10, 70]
result = []
for i in range(1, 11):
    for combination in itertools.combinations_with_replacement(notes, i):
        if sum(combination) == 100:
            result.append(combination)
            print(combination)
print(len(result))

# https://docs.python.org/3/library/itertools.html
