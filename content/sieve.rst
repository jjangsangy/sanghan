========================================
Prime Sieves and Python Data Structures
========================================
:date:      08-29-2014
:slug:      sieve
:category:  Programming
:Tags:      Python


Recently, I’ve been working through `Project Euler`_ problems
in order to improve my core programming skills.

One of those recurring problems requires an
efficiently calculating and testing for prime numbers. The first
algorithm that comes to mind is `The Sieve of Eratosthenes`_.
The Sieve, is one of many prime sieves, and is a simple yet time efficient algorithm
for finding all the primes below a certain limit. It can be shown to
have a time complexity of :math:`\mathcal{O}(n\log{}\log{}n)`.

The Algorithm
-------------
1. Make a table one entry for every number :math:`2 \leq n \leq limit`
2. Starting at 2, cross out all multiples of 2, not counting 2 itself.
3. Move up to the next number that hasn't been crossed out
4. Repeat Step 2-3 up till :math:`\sqrt n`

Visually we can depict each loop removing values from the list
of real numbers until all that is left are the primes.

|sieve|

Unfortunately, this solution starts to become less
viable for larger problem sizes. Since it requires a table of every
number to the last integer in memory, the space complexity of sieves generally
grows in the order of :math:`\mathcal{O}(n)`. In order to deal with memory issues
there is a set of Sieve algorithms called :code:`segmented sieves` which distribute
the problem into smaller subsets.

.. pull-quote::

    Here's how it would look in Python.

The Code
----------

General Case
~~~~~~~~~~~~~~~~~

.. code-block:: python

    def sieve(n: int) -> list:
        """Sieve away and only primes are left."""
        primes = 2*[False] + (n-1)*[True]
        for i in range(2, (n**0.5+1)):
            for j in range(i*i, n+1, i):
                primes[j] = False
        return [prime for prime, check in enumerate(primes) if check]

It's important to notice we implement :code:`lists` as the main data structure.
Remember although the algorithm requires an in memory table containing,
we have the freedom to construct it using
whatever tools the runtime affords. Here is an example of another sieve
but with it's guts swapped with unordered :code:`sets`.

Sets: Unordered Collections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def set_sieve(n: int) -> set:
        """
        Sets are mutable, unordered, hash collections which are useful
        for quick membership testing.
        """
        primes = set(range(2, n+1))
        for i in range(2,int(n**0.5+1)):
            if i in primes:
                primes -= set(range(i*i, n+1, i))
        return primes

The primary difference you see with using :code:`sets` and :code:`lists`, is the
lack of a list-comprehension for composing the function return value. Also the
second for-loop substituted with the binary :code:`-=`, assignment operator, which for
set objects has been overloaded with a :code:`difference update` expression or
the set mathematical compliment :math:`\forall \{x|x \in A \subset \notin B\}`.
Sets are a great way represent mathematical operations and carry out membership testing
on unordered groups of objects.


Insertion Sets:
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def set_insertion_sieve(n: int) -> set:
        """
        Performing insertion over deletion utilizing
        constant time nature of hashable collections.
        """
        factors = set()
        for i in range(2,int(n**0.5+1)):
            if i not in factors:
                factors |= set(range(i*i, n+1, i))
        return set(range(2,n+1)) - factors


Lists are a great general purpose data-structure, and is likely the first
tool to reach for in the arsenal. However, it's generality is also probably
it's main weakness.
While fundamentally the choice data structure is orthoganal to program
correctness, it's important for real runtime performance to use the best
tool to fit the job.


Numpy
~~~~~~
.. code-block:: python

    import numpy as np

    def np_sieve(n: int) -> np.ndarray:
        """
        Numpy n-dimmensional array are continguous strides
        of memory with fixed width statically typed elements.
        Ndarrys are a  random access data-structure unlike
        pythons built-in doubly linked-lists.
        """
        primes = np.ones(n+1, dtype=np.bool)
        for i in np.arange(2, n**0.5+1, dtype=np.uint32):
            if primes[i]:
                primes[i*i::i] = False
        return np.nonzero(primes)[0][2:]


Testing for Primality
----------------------

.. code-block:: python

    def all_primes(primes: iter) -> bool:
        for prime in primes:
            if any(prime % n == 0 for n in range(2, prime)):
                return False
        return True

.. code-block:: python

    >>> all_primes(np_sieve(10**3))
    True

.. code-block:: python

    >>> all_primes(set_sieve(10**3))
    True

.. code-block:: python

    >>> all_primes(set_insertion_sieve(10**3))
    True


A Timer
-------

.. code-block:: python

    import time
    from contextlib import contextmanager

    @contextmanager
    def timer(label):
        start = time.time()
        try:
            yield
        finally:
            end = time.time()
        print('{label}: {time:03.3f} sec'.format(
            label=label, time=end-start)
        )

Performance Testing
--------------------

.. code-block:: python

    >>> with timer('set_sieve'):
            set_sieve(10**6)

    set_sieve: 0.735 sec

.. code-block:: python

    >>> with timer('set_insertion_sieve'):
            set_insertion_sieve(10**6)

    set_factor_sieve: 0.587 sec

.. code-block:: python

    >>> with timer('numpy'):
            np_sieve(10**6)

    numpy: 0.008 sec

.. |sieve| image:: {filename}/img/sieve.jpg

.. _Project Euler:
   https://projecteuler.net


.. _The Sieve of Eratosthenes:
   http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
