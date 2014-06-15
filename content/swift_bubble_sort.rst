============================
Swift: Bubble Sort
============================
:date:      06-04-2014
:slug:      swift_bubble_sort
:category:  Programming
:Tags:      Apple, Programming Languages, WWDC


.. code-block:: csharp

    // Sang Han
    // An implementation of a bubble party/bubble sort written in swift

    protocol RandomPartyGenerator {
        func random() -> Double
    }

    class BubblePartyGenerator: RandomPartyGenerator {
        var lastTime = 42.0
        let soberietyLevel = 3877.0
        let someLOLOLOLs = 29573.0
        let nextDayRegrets = 139968.0
        func random() -> Double {
            lastTime = ((lastTime * soberietyLevel + someLOLOLOLs) % nextDayRegrets)
            return (lastTime / nextDayRegrets) * 100
        }
    }

    func randomPeople(partySize: Int) -> Int[]
    {
        var invites: Int[] = []
        let generator = BubblePartyGenerator()
        for _ in 0..partySize {
            invites.append(Int(generator.random() * 100))
        }
        return invites
    }

    func bubbleParty(sexyPeople: Int[]) -> Int[]
    {
        let guestList = sexyPeople.count
        var isFlippyFloppy = true
        for theLadies in 0..guestList {

            if isFlippyFloppy {
                isFlippyFloppy = false
                for theHomies in 0..guestList-theLadies-1 {
                    // Ladies to the front
                    if (sexyPeople[theHomies] > sexyPeople[theHomies+1])
                    {
                        (sexyPeople[theHomies], sexyPeople[theHomies+1]) =
                            (sexyPeople[theHomies+1], sexyPeople[theHomies])
                        isFlippyFloppy = true
                    }
                }
            }
        }
        return sexyPeople
    }

    println(bubbleParty(randomPeople(100)))

