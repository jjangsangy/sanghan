=============================================
Swift Program is Swift, Except When it's Not
=============================================
:date:      06-11-2014
:category:  Programming
:slug:      swift_program_is_swift_except_when_its_not
:tags:      Apple, Programming Language, Benchmarks, Bubble Sort

|swift|

This past WWDC Apple revealed a brand new programming language called `Swift`_
to the masses and passed it out to Apple Developers packaged in the XCode 6 Beta.

Language Features
-----------------
* Type Inferencing and Automatic Reference Counting (ARC)
* Optional Bindings and Generic Functions
* Integration with Objective-C
* First-Class Functions and Closures

My initial impressions were pretty high. However, after some quick benchmarking
examples, those feelings later matured to an understanding of it's "beta"
characteristics. Many of the underlying optimization still have some kinks to
work through.

.. pull-quote::

   And by kinks, I mean some big fixes

Benchmarks
----------

.. pull-quote::

    Here are a couple examples of Bubble Sort written out in C, Python and Swift.

Swift Bubble Sort
~~~~~~~~~~~~~~~~~

.. code-block:: csharp
   :linenos: inline

    import Cocoa

    func bubbleSort(list: Int[]) -> Int[]
    {
        let length = list.count
        var count: Int
        var pos: Int

        for (count = 0; count < length-1; count++) {
            for (pos = 0; pos < (length-count-1); pos++) {
                if (list[pos] > list[pos+1]) {
                    (list[pos], list[pos+1]) =
                        (list[pos+1], list[pos])
                }
            }
        }
        return list
    }

    func sortMain(problem_size: Int) -> Int[]
    {
        var array: Int[] = []

        srandomdev()
        for _ in 0..problem_size {
            array += (random() % problem_size)
        }
        return bubbleSort(array)
    }

C Bubble Sort
~~~~~~~~~~~~~
.. code-block:: c
   :linenos: inline

    #include <stdio.h>
    #include <stdlib.h>

    void bubble_sort(long list[], long n)
    {
        long count, pos, temp;
        for (count = 0; count < (n-1); count++) {
            for (pos = 0; pos < (n-count-1); pos++) {
                if (list[pos] > list[pos+1])
                {
                    temp        =   list[pos];
                    list[pos]   =   list[pos+1];
                    list[pos+1] =   temp;
                }
            }
        }
    }

    int main(int argc, char *argv[])
    {
        long problem_size = strtoul(argv[1], NULL, 10);
        long array[problem_size];
        long count;

        sranddev();
        for (count = 0; count < problem_size; count++) {
            array[count] = rand() % problem_size;
        }

        bubble_sort(array, problem_size);

        for (count = 0; count < problem_size; count++) {
            printf("%ld\n", array[count]);
        }
        return 0;
    }

Python Bubble Sort
~~~~~~~~~~~~~~~~~~~
.. code-block:: python
   :linenos: inline

    import os, sys
    from random import randint

    def bubble_sort(a_list: Int<Array>): -> Int<Array>
        length = len(a_list)

        for count in range(0, length):
            for pos in range(0, length-count-1):
                if a_list[pos] > a_list[pos + 1]:
                    a_list[pos], a_list[pos+1] = \
                    a_list[pos+1], a_list[pos]
        return a_list

    def main(args: Int): -> Int<Array>
        if (len(args)-1):
            problem_size = int(args[1])
        else:
            problem_size = 10000
        array = [randint(0, problem_size) for num in range(0, problem_size)]

        return bubble_sort(array)


    if __name__ == '__main__':
        sys.exit(main(sys.argv))

Fast Swift:
-----------
.. pull-quote::

    Swift vs C vs PyPy

.. raw:: html

    <div class="plotly">
        <iframe id="igraph" style="border:none" src="https://plot.ly/~jjangsangy/82/" width="100%" height="100%"></iframe>
    </div>

.. pull-quote::

   Swift Program is Swift, It even beats C by a non-trivial margin in these tests.

Slow Swift:
-----------
.. pull-quote::

   Swift [-Ofast] vs Swift[-O3] vs CPython

One caveat however, is we used the [-Ofast] flag during compilation of the swift binaries like so.

.. code-block:: sh

    xcrun --sdk macosx swift -Ofast -o bubble_sort.swift bubble_sort

According to Apple's official documentation in the XCode 5.0 release notes:

.. pull-quote::

    A new optimization level -Ofast, available in LLVM, enables aggressive optimizations.
    -Ofast relaxes some conservative restrictions,
    mostly for floating-point operations,
    that are safe for most code.
    It can yield significant high-performance wins from the compiler

If we were to run the same code with normal compiler optimizations we start to see a completely
different picture than the one we started with

.. code-block:: sh

   xcrun --sdk macosx swift -O3 -o bubble_sort.swift bubble_sort

.. note::

   In order to save time, I've changed the problem sizes to be
   multiples of 1k rather than 10k, so that tests could
   finish reasonibly quick. Other than that nothing has changed.

.. raw:: html

    <div class="plotly">
        <iframe id="igraph" style="border:none" src="https://plot.ly/~jjangsangy/84/" width="100%" height="100%"></iframe>
    </div>


Modern, Safe and Powerful: Choose 2
-----------------------------------

|swift_principles|


According to a post on `Stacked Overflow`_

.. pull-quote::

   However, -Ofast changes the semantics of the language a lot — in my testing,
   it disabled the checks for integer overflows and array indexing overflows.
   For example, with -Ofast the following Swift code runs silently
   without crashing (and prints out some garbage):

.. code-block:: csharp

    let n = 10000000
    println(n*n*n*n*n)
    let x = Int[](count: n, repeatedValue: 10)
    println(x[n])

..

* With -Ofast I get pretty much what I would expect.
  The relevant part is a loop with 5 machine language instructions.

* With -O3 I get something that was beyond my wildest imagination.
  The inner loop spans 88 lines of assembly code.
  I did not try to understand all of it, but the most suspicious parts are 13 invocations of
  callq _swift_retain" and another 13 invocations of "callq _swift_release".
  That is, 26 subroutine calls in the inner loop!



.. _`Swift`: https://developer.apple.com/swift/
.. _`post`: http://sanghan.me/blog/2014/06/swift_bubble_sort/index.html
.. _`Stacked Overflow`: http://stackoverflow.com/questions/24101718/swift-performance-sorting-arrays



.. |swift| image:: {filename}/img/swift.jpg
.. |swift_principles| image:: {filename}/img/swift_principles.jpg
