========================================
Prime Sieves and Python Data Structures
========================================
:date:      09-11-2014
:slug:      sieve
:category:  Programming
:tags:      Python, Prime Numbers, Sieve, Eratosthenes, Numpy, Project Euler, Algorithms, Data Structures


Recently, I’ve been working through `Project Euler`_ in order to improve my
core programming skills.

One of those recurring problems requires
efficiently calculating and testing for prime numbers. The first
algorithm that comes to mind is `The Sieve of Eratosthenes`_.
The Sieve, is one of many prime sieves, and is a simple yet time efficient algorithm
for finding all the primes below a certain limit.

The Algorithm
-------------
1. Make a table one entry for every number :math:`2 \leq n \leq limit`
2. Starting at 2, cross out all multiples of 2, not counting 2 itself.
3. Move up to the next number that hasn't been crossed out
4. Repeat Step 2-3 up till :math:`\sqrt(n)`

.. pull-quote::

    The Sieve of Eratosthenes can be shown to have a time
    complexity of :math:`\mathcal{O}(n\log{}\log{n})`.


Visually we can depict each loop removing values from the list
of real numbers until all that is left are the primes.

|sieve|

.. pull-quote::

    Unfortunately, this solution starts to become less
    viable for larger problem sizes.

Since it requires a table of every
number to the last integer in memory, the space complexity of sieves generally
grows in the order of :math:`\mathcal{O}(n)`. In order to deal with memory issues
there are sieve algorithms called :code:`segmented sieves` which map and distribute
the problem into smaller sizes and are computed in parallel.

.. pull-quote::

    Here's how a basic sieve would look in Python.

The Code
----------

.. pull-quote::

    I've written out the function definition using :code:`type annotations`,
    which explicitly describe the type of arguments a function take and what
    types they return. This is a great documentation tool built-in, but only
    available for Python 3 and not Python 2.

.. code-block:: python

   # Type Annotation Prototype
   def foo(x: type) -> type:


Sieve
~~~~~

.. code-block:: python

    def sieve(n: int) -> list:
        """Sieve away and only primes are left."""
        primes = 2*[False] + (n-1)*[True]
        for i in range(2, int(n**0.5+1)):
            for j in range(i*i, n+1, i):
                primes[j] = False
        return [prime for prime, checked in enumerate(primes) if checked]

It's important to notice we implement :code:`lists` as the main data structure.
Although the algorithm requires an in memory table,
we can construct it using
any tool. Here is another sieve
but with it's guts swapped with :code:`sets`.

Run it
--------

.. raw:: html

    <iframe src="https://trinket.io/embed/python/2c6fd7a0de"
    width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>



Sets: Unordered Collections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def set_sieve(n: int) -> set:
        """
        Sets are mutable, unordered collections which are useful
        for quick membership testing and math operations.
        """
        primes = set(range(2, n+1))
        for i in range(2,int(n**0.5+1)):
            if i in primes:
                primes -= set(range(i*i, n+1, i))
        return primes

In this example, the primary difference with using :code:`sets` and :code:`lists`, is the
lack of a list-comprehension for composing the function return value. As well, the
second for-loop is substituted with one :code:`-=`, binary assignment operator, which for
sets has been overloaded with a :code:`difference update` method or
the mathematical complement :math:`\forall \{\text{n}|\text{ n }\in \text{A : n }\notin\text{ B}\}`

Utilizing sets provides us a cleaner syntax for algorithms involving math.
In this example, we first create a :code:`universal set`, and iteriatively delete it's factors.
It would also be correct to construct a :code:`null set` and iteratively insert all factors first.
Once all factors have been collected, perform a removal from the universal set.

Insertion Sets:
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    def set_insertion_sieve(n: int) -> set:
        """Performing insertion over deletion"""
        factors = set()
        for i in range(2,int(n**0.5+1)):
            if i not in factors:
                factors |= set(range(i*i, n+1, i))
        return set(range(2,n+1)) - factors

Algorithmic Analysis
----------------------

The question is, is it really possible characterize runtime without
actually running a single benchmark? For much `larger programs`_, it might not be,
but for this isolated case, it's possible to make some good predictions.

Both :code:`set_sieve` and :code:`set_insertion_sieve` perform similar operations
until the second iterative block. Because set operations are primarily implemeneted as hashes, we can assert that
both set :code:`insertion` and set :code:`deletion` are :math:`\mathcal{O}(1)` time operations in relation to problem-size
and :math:`\mathcal{O}(n)` time operations in relation hash-size. Therefore, it's possible that
either of these soltuions could run faster because with each iteration of :code:`set_sieve`
the hash-size decreases, while :code:`set_insertion_sieve` hash size increases.

.. pull-quote::

    But what if we knew the proportion of primes vs non-primes in a series?

Prime Number Theorem
~~~~~~~~~~~~~~~~~~~~~~
Early intuition would have biased us about the general abundance of primes
and non-primes. But the prime number theorem is a mathematical proof
between the amount of primes and non-primes that exist in the set of real numbers.

$$
\\large\\lim_{x\\to \\infty} \\frac{\\pi\(x\)}{\\frac{x}{\\ln(x))}} = 1 \\tag{def}
$$

It's basic definition is that as we move across the x-axis of real numbers
:math:`\pi(x)` a function computing number of primes at x, we can expect as
:math:`x\to \infty` that :math:`\pi(x) \to \frac{x}{\ln(x)}`, and the entire
expression approaches 1.

$$
\\large \\pi\(x\) \\tag{asymtotic} \\thicksim \\large \\frac{x}{\\ln(x))}
$$

From the asymptotic expression, we can also express the function for
computing all factors of :math:`n` to then be

$$\\begin{align}
\\large\\lim_{n\\to \\infty} n\\left(1 - \\frac{1}{\\ln(n)}\\right) \\tag{factors}
\\end{align}$$

.. pull-quote::

    We find insertion actually runs faster by an order of
    :math:`\frac{1}{\ln(n)}`. But this is a diminishing optimization which
    converges back to the original :code:`sieve` speed at larger problem sizes.

Data Structures
-----------------
Lists and sets are general purpose data-structures
and are useful for solving many different problems.
However, their general nature cause them to be less useful
for specialized tasks, or when high performance is needed.

It's also easy to fall into the trap of using general tools when
better options are available.

`Maslow`_ tells us

.. pull-quote::

    *"If the only tool you have is a hammer everything looks like a nail."*

    The Psychology of Science (1964)

While the choice data
structure is orthoganal to correctness,
it's important to use the best tool
for the job.

.. pull-quote::

    So what is the most optimal data structure to perform these calculation?

Enter: The Array
~~~~~~~~~~~~~~~~~

.. code-block:: python

    import numpy as np

    def np_sieve(n: int) -> np.ndarray:
        """
        Sieve with it's guts swapped with numpy
        ndarray
        """
        primes = np.ones(n+1, dtype=np.bool)
        for i in np.arange(2, n**0.5+1, dtype=np.uint32):
            if primes[i]:
                primes[i*i::i] = False
        return np.nonzero(primes)[0][2:]

Numpy is a third party library containing array based data structures
and fast vectorizable methods for numerical operations.
Here we operate on numpy's :code:`n-dimmensional arrays`
which allocate fixed strides of memory containing :code:`statically typed` elements.
The downside of implementing a statically typed subset within a dynamically typed
language is to forego many of the niceties python has to offer.
However, the main benefit is random access to
individual array elements in memory, instantly without traversal.

Everything inside a numpy array must be homogenous,
and to be efficient we must know the exact length of the array beforehand.
This is because the task of extending or contracting an array once initialized
requires re-copying all elements into a new array of new length.
We also have to be strict when initializing :code:`bools` :code:`ints` and :code:`floats`
with proper :code:`fixed-widths` for memory allocation.

In our example we are filling up an array with :code:`8-bit bools` all set
to :code:`True`. We then iterate through
an array of factors set to :code:`32-bit unsigned integers`, and allocate
it's multiples as :code:`False`. Finally, we return all values from the
boolean array from 2 to the end which are still :code:`True`. However, unlike slicing
python lists which generates a whole new copy from the original, slicing numpy arrays
returns is an in-memory view and is a much cheaper operation. Therefore, the
vector operation :code:`primes[i*i::i]` is just an in-memory view of the
same :code:`primes` array requiring no more levels of indirection or
memory allocation to construct.

Running the Code
-----------------

.. raw:: html

   <iframe src="https://trinket.io/embed/python/7f6f9a989b"
   width="100%" height="550" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Testing for Primality
----------------------

So now that we've written the sieve in a bunch of different ways. How do we know that
each way is correct.

The most obvious way to figure if a number's prime, is to try dividing the number
by all the numbers between :math:`2 \leq x \leq n-1`.

.. code-block:: python

    def all_primes(primes: iter) -> bool:
        for prime in primes:
            if any(prime % n == 0 for n in range(2, int(prime**0.5))):
                return False
        return True

.. pull-quote::

    Now lets test to see if our sieves can correctly find the first 100 prime numbers

.. code-block:: python

   >>> all_primes(sieve(10**3))
   True

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
~~~~~~~~

Now knowing that our implementations are correct, lets see how fast they run.
We will construct a timer taking advantage of what is known as a :code:`context manager`.
Basically, a context manager allows us to use the :code:`with` construct
and will perform an operation before and after by overloading the :code:`__enter__`
and :code:`__exit__` methods. We can create a context manager
merely by using a decorator from the :code:`contextlib` module.

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

.. pull-quote::

    It's also possible to use Python's built in :code:`timeit` module, which can deal
    with much more complex and isolated timing instances.

Some Benchmarks
----------------

.. pull-quote::

    Now lets see how fast our seives can find the first million
    digits.

.. code-block:: python

   >>> with timer('sieve'):
           sieve(10**6)

   sieve: 0.454 sec

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

Things to Note
~~~~~~~~~~~~~~~
* Overall lists are better optimized than
  sets for inline operations.
* As we expected :code:`set_insertion_sieve` performed
  better than :code:`set_sieve`, but only marginally.
* Numpy :code:`arrays` are fast! They outperform other built in
  data structures by 2 orders of magnitude!


.. |sieve| image:: {filename}/img/sieve.jpg

.. _Project Euler:
   https://projecteuler.net

.. _Maslow:
   http://en.wiktionary.org/wiki/if_all_you_have_is_a_hammer,_everything_looks_like_a_nail

.. _prime number theorem:
   http://en.wikipedia.org/wiki/Prime_number_theorem

.. _The Sieve of Eratosthenes:
   http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

.. _larger programs:
   http://en.wikipedia.org/wiki/Travelling_salesman_problem
