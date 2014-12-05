============================
Swift: Bubble Sort
============================
:date:      06-04-2014
:slug:      swift_bubble_sort
:category:  Programming
:Tags:      Apple, Programming Languages, WWDC


.. code-block:: swift

    // Sang Han
    // An implementation of a bubble party/bubble sort written in swift

    import Foundation

    func exchange<T>(inout a: T, inout b: T)
    {
        let tmp = a
        a = b
        b = tmp
    }

    func bubbleSort(inout array: [Int]) -> [Int]
    {
        let length = array.count

        var count, pos: Int
        for (count=0; count<length-1; count++)
        {
            for (pos=0; pos<(length-count-1); pos++)
            {
                if (array[pos] > array[pos+1]) {
                    exchange(&array[pos], &array[pos+1])
                }
            }
        }
        return array
    }

    func sortMain(arrayLength: Int) -> [Int]
    {
        var array: [Int] = []
        for _ in 0..<arrayLength {
            array.append(
                Int(arc4random_uniform(UInt32(arrayLength*100)))
            )
        }
        return bubbleSort(&array)
    }

