# simple-ascii-player
Simple ASCII video player made with `Python`, `OpenCV` and `NumPy`.
A casual project that **you can learn and make it better** than mine within a day.

# Reminder
If you're going to run this code. Make sure you have installed `requirements.txt` with command below.<br>
**`pip install -r requirements.txt`**

# How it works?
This is a brief explaination of code.

## Loading file and define target width for rendering
Before you'll play anything you need user to input something to program which is video file. I use OpenCV for media loading and processing frames.
> Because it's OpenCV, instead of just video you may want to go for something cooler by connecting to camera from your device or network later on.

For this basic project I want user to input target `width` of output by themselves, `width` will be used for calculating later.

## Processing frame and dimensions
Use OpenCV `read()` method to read frame data from file. Then get dimensions of frame (width, height) and change frame color format to `BGR2GRAY`.
> For simplicity we'll have our frame as grayscale because the whole frame is just array of number from 0-255 so it's easier to convert to ASCII characters but you can have it be color if you want.

Next I calculate aspect ratio with this formula : **`aspect_ratio = height / width`**
Now that I've got aspect ratio of the frame, I can calculate output height with this formula : **`target_height = int(target_width * aspect_ratio * 0.5)`**
Because in terminal characters are roughly twice as tall as they're wide, I don't want the output to be **stretched** so I multiply it by 0.5

## Turning frame to characters
I resize frame to target dimensions as I have calculated it, this make it easier because every pixels of frame matches target dimensions.
Then I turn each pixels in frame to chars indice with this formula : **`char_indices = (gray / 255.0 * (num_chars - 1)).astype(int)`**

## Printing
Now I can simply loop through each row and print them out.

# Thank you :D
You've come this far. I hope you got something from this simple repo. Thank you so much for coming by. Have a great day!
