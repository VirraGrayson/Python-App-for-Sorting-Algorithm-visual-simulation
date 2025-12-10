import gradio as gr
import random

def insertion_sort_colored(arr):
    steps = []  # will store each visual step of the sort
    explanation = "The first number is always concidered as 'sorted', as there are no numbers before it to compare with"
    steps.append(color_step(arr, 0, None, explanation))  # first element is treated as sorted

    # go through the list starting from the second number
    for i in range(1, len(arr)):
        key = arr[i]          # value we want to insert into the right spot
        j = i - 1             # pointer to check previous numbers
        last_changed = None   # keeps track of where movement happened
        compared = []         # text used later for explanation
        change_times = 0

        # shift numbers to the right until correct spot for key is found
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # move number right
            last_changed = j + 1  # mark the moved position
            j -= 1

        last_changed = j + 1
        arr[j + 1] = key  # place key into its new spot

        # if the number actually moved then build an explanation
        if j + 1 != i:

          # build comparison text for visual output
          for k in range(0, i-j-1):
            compared.append(f"<span style='color:orange; font-weight:bold'>{arr[j+1]}</span> < {arr[i-k]}")

          # final comparison shown in output
          if j >= 0 and j != j+1:
           compared.append(f"<span style='color:orange; font-weight:bold'>{arr[j+1]}</span> > {arr[j]}")
          elif j >= 0 and j == j+1:
           compared.append(f"<span style='color:orange; font-weight:bold'>{arr[j+1]}</span> = {arr[j]}")

          explanation = f"{' | '.join(compared)} <br> Old index {i} → New index {j+1}."

        else:
          explanation = f"{key} stayed in place."  # when nothing changed

        steps.append(color_step(arr, i, last_changed, explanation))  # store update for display

    return "<br><br>".join(steps)  # send back full visual history


def color_step(arr, sorted_index, last_changed, message=""):
    result = []
    for idx, num in enumerate(arr):

        # decide color based on sorted status
        if idx == last_changed:
            color = "orange"       # moved number
            weight = "bold"
        elif idx <= sorted_index:
            color = "green"        # sorted section
            weight = "bold"
        else:
            color = "red"          # still unsorted
            weight = "normal"

        # make floats display without .0 if possible
        if num.is_integer() == True:
          num = int(num)

        result.append(f"<span style='color:{color}; font-weight:{weight}'>{num}</span>")

    return " ".join(result) + f"<br><small>{message}</small>"  # one line of colored numbers + explanation


def nums(user_input):
  # runs when user enters numbers manually
  if user_input != "":
    numbers = []

    try:
      # convert input into a list of numbers
      for n in user_input.split(","):
        if len(numbers) >= 20:
            break
        numbers.append(float(n.strip()))

    except (TypeError, ValueError):
        return ("⚠️Input Contains Invalid Character!")

    return insertion_sort_colored(numbers)  # process sorting visuals


def generate_list(amount, min, max):
  # creates random list of numbers
  try:
    arr = random.sample(range(int(min), int(max)), int(amount))
    text = ", ".join(str(x) for x in arr)
    return text, None
  except (TypeError, ValueError):
        return "", "⚠️Minimum random number is greater than maximum!"


# resets input + output boxes
def clear():
  output = ""
  input = ""
  return output, input


# ---------------- GUI Layout ----------------
with gr.Blocks() as demo:

    input = gr.Textbox(label="Input List (MAX 20 numbers)", placeholder="1, 2, 3, 4, 5...", max_lines=1)
    output = gr.HTML(label="Sorting Steps with Colors")

    with gr.Row():
      run_btn = gr.Button("Sort")
      random_btn = gr.Button("Randomize")
      clear_btn = gr.Button("Clear")

    with gr.Row():
      random_amount = gr.Number(label="Amount Of Random Numbers (1-20)", value=10, precision=0, interactive=True, maximum=20, minimum=1)
      random_min = gr.Number(label="Minimum Value Of Random Numbers", value=1, precision=0, interactive=True, maximum=9998, minimum=-9999)
      random_max = gr.Number(label="Maximum Value Of Random Numbers", value=100, precision=0, interactive=True, maximum=9999, minimum=-9998)

    # button actions
    run_btn.click(fn=nums, inputs=input, outputs=output)
    random_btn.click(fn=generate_list, inputs=[random_amount,random_min,random_max], outputs=[input,output])
    clear_btn.click(fn=clear, inputs=None, outputs=[output,input])

demo.launch()
