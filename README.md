# File Organizer

## Overview

This is a simple Python script that organizes files from the `Downloads` folder into categorized subfolders inside `Documents`. It uses **OS** and **shutil** modules to move and organize files based on predefined keyword mappings.

The way I coded this is not the most efficient way of creating a file organizer.
I created a bit more simple code that that is broken up into multiple functions, and would be better for reusability.
This is my first time using OS and shutil, so when I have more familiarity withe the modules then I will be able to use less code and create more complex functions.

## Features

✅ Moves all files from `Downloads` to `Documents`.  
✅ Creates folders for different file categories.  
✅ Automatically sorts files based on keywords in their names.  
✅ Ensures folders exist before moving files.

## How It Works

1. **Move all files** from `Downloads` to `Documents`.
2. **Create folders** for each category based on predefined keywords.
3. **Check filenames** for category keywords.
4. **Move files** into their respective folders.

## Installation & Usage

1. Clone or download the script.
2. Modify `SOURCE_DIRECTORY` and `DESTINATION_DIRECTORY` paths in the script.
3. Run the script using:
   ```sh
   python file_organizer.py
   ```
