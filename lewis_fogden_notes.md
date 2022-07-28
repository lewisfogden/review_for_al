# Python Programming Exercises Gently explained
Review by Lewis Fogden (lewisfogden@hotmail.com / @lewisfogden on twitter)

## General comments

I've read over the introduction sections and worked through the exercises noted below.  Reads really well, neatly structured with progressive help.

## Style/Formatting
 
 - font jumps between serif and non-serif e.g. page 6 / page 7
 - PEP008 recommends functions_with_spaces rather than camelCase https://peps.python.org/pep-0008/#function-and-variable-names (completely your choice though, they are just function names!)

## Exercises 

### Exercise 1

 - input([request]) is slightly better than print([request]) then input([blank]) as the question is stored with the response.

e.g.
```python
print("Hello, world!")
name = input("What is your name? ")
print("Hello,", name)
```

 - Link to https://invpy.com/helloworld.py doesn't work, assume this will be fixed before publication :)


### Exercise 2

- p12 typo: `degreesCelsisus` should be `degreesCelcius` (or `degrees_celcius` by PEP008)
- Special Cases/Gotchas - I get an exact solution of 42.0 for this (which just shows the risks of floating point numbers!)
- Can also use a tolerance to deal with checking floating point numbers are sufficiently accurate, e.g. for temperature one decimal place is probably sufficient.


### Exercise 42: BubbleSort

- Might be better to define bubble sort earlier?  (not that it mattters, someone might accidentally invent a new sorting algorithm!)
- on page 141, the `j` loop should start from `i+1`, otherwise you are comparing `i` with itself?
- maybe worth another assert as the two there aren't particularly good challenge (I added a bug in my code and they still passed when they should have failed)

e.g. assert... [7, 5, 4, 9, 2, 6, 6, 9, 0, 2, 8, 9, 2, 7, 5, 7, 4, 8, 5, 5]


### Exercise 15: Median

- p53: pedantic: Median is a measure of average, maybe replace average with mean.
- p53: passing an empty list to `average()` - should be `median()`?
- p54: suggest using sorted() rather than list.sort() method as it will mutate the original list (which may not be desired)
- p54: median would suit a simple diagram, I've included something in the example (ex15.py)

### Exercise 31: Convert Integers to Strings

- see amendments to code, e.g. using a string "0123456789" rather than dictionary is more concise.  No functional difference though, and dictionaries are generally the right thing to use for lookups.

### Exercise 32: Strings to Integers

- p108 very pedantic (sorry) - text file won't have have a .read() method, but a text file *object* opened with open('name.txt', 'r') would.
- fonts/text go a little wonky on p109 e.g. `Before going into the algo...ematics` has what looks like an image for `rithm, let's discuss the math` in it.  (I couldn't select it)
- Although it works, solution design is quite complicated on this one, maybe rather than using powers of 10 (which might scare people a bit), could built it up using iteration:

    * could consider thinking what happens if you have the string `4`, then the string `41`, then the  `410`, then the  `4109`, then finally `41096`, and what happens to the number as you progress
    * `4` goes to 4, and you can store this in `number`
    * if there is another number following `1`, then the 4 becomes 40, and you add on 1, to get 41. 
    * then you find another number following which is `0`, you multiply 41 up to get 410, and then add on 0.
    * continue until you run out of numbers to add on the end.

- The solution template is missing underscores in the gaps ___
- see ex32.py for my solution.

### Exercise #33: Comma-Formatted Numbers

My brain wasn't in gear for this one and I made a mess of it!  I read the guide and solution and it worked.

Lazy me did a f-string test:

```python
def commaFormat_f(number):
    # f string version
    return f"{number:,}"
```

This could be used for asserts?

---
Comments above to 28/07/2022 23:29
---

