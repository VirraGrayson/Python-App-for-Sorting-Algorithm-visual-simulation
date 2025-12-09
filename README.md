# Insertion Sort Algorithm

## Problem Breakdown & Computational Thinking (You can add a flowchart and write the four pillars of computational thinking briefly in bullets)


### Decomposition:
- Select a variable from the list (starting at the beggining with index 0)
- Compare the chosen variable to all those before it in the list.
- Move the chosen variable if it is smaller than some variables before it in the list, inserting it in the correct position.

### Pattern Recognition:
- Each iteration picks the next variable in the list (starting at index 0).
- The chosen variable is compared to all those before it in the list (which means they have already been sorted), using a loop.
- Each time it is compared to another variable, check if the given variable is smaller.
- If it is smaller, swap the position of both values, then compare the given variable to the next in the list
- If the given variable is instead larger or equal to the compared other variable, than mark the given variable as "sorted" and move on to the next up the list.

### Abstraction:
- Show the chosen variable being moved to its new index position, or showing that it didn't move and is already sorted.
- Show the comparison of each number the chosen variable is compared to before reaching its "sorted position".
- Show which numbers are currently concidered "sorted" and which are "unsorted".

### Algorithm Design:
- Input:
  - User inputs a list of numbers in a text box, or generates a random list.
  - Add input safties to insure no errors occure if invalid characters are inputed.
- Processing:
  - Apply insertion sort to the input list.
  - At each step of the sort, record the current list state and the positions of moved elements.
- Output:
  - Display the list each time a variable is shifted to its sorted position, using colors to diferentiat the two states
  - Print some form of small explination of what just occured.

## Steps to Run

### Manual Input

1. Type your list of numbers into the box labeled "input list", making sure to add a comma between each number.
2. Click the "Sort" button.

### Random Input

1. Manualy set the maximum and minumum potential values for the randomized numbers, as well as how many numbers you would liek to generate.
2. Clcik the "Randomize" button.
3. Hit the "Sort" button.

## Hugging Face Link

## Demo video/gif/screenshot of test

### Standard Tests

Tested: Random assortment of positive numbers | Result: Produced correctly sorted list

<img width="1683" height="902" alt="image" src="https://github.com/user-attachments/assets/55a7b0ef-ea6c-4429-a064-bd2af8fd3054" />

Tested: Random assortment of numbers including negatives | Result: Produced correctly sorted list

<img width="1677" height="922" alt="image" src="https://github.com/user-attachments/assets/73644f14-0f3d-4c18-b0f2-0a63ef323390" />

Tested: Random assortment of numbers including negatives and floating point numbers | Result: Produced correctly sorted list

<img width="1673" height="893" alt="image" src="https://github.com/user-attachments/assets/0f24d770-8bf8-4c91-8d1b-5b7a62589d8b" />


### Potential Error Tests

Tested: Inputting invalid characters (e.g. none numbers) | Result: Outputed error message (Not a code failing error message, just a failsafe when given inavalid inputs)

<img width="1694" height="288" alt="image" src="https://github.com/user-attachments/assets/37b177a2-b80e-4bbf-a76a-e6d27e8a201d" />

Tested: Setting random minimum value to be larger than the random maximum value | Result: Outputed error message (Not a code failing error message, just a failsafe)

<img width="1506" height="329" alt="image" src="https://github.com/user-attachments/assets/a526c045-7cbb-4df3-b44e-f4178d097403" />

Tested: Giving more than 20 numbers in the input | Result: Sorts the first 20 given numbers, and ignores any that follow

<img width="1480" height="332" alt="image" src="https://github.com/user-attachments/assets/f2b3b9e1-4b7e-4230-8051-8ad02784ae4f" />


## Author & Acknowledgment
