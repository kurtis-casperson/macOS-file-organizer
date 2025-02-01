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
   python main.py
   ```

### **🚀 How to Create a Command to Run `main.py` from the Terminal on macOS**

If you want to be able to **run `main.py` from anywhere** in the terminal using a simple command, follow these steps:

---

### **1️⃣ Make Sure `main.py` is Executable**

First, you need to **give execute permissions** to the script:

```sh
chmod +x /path/to/main.py
```

Replace `/path/to/main.py` with the actual path to your script.

Example:

```sh
chmod +x ~/python-projects/file-organizer/main.py
```

---

### **2️⃣ Create a Terminal Command (Alias)**

To run `main.py` from anywhere, set up an **alias** in your shell configuration file.

1️⃣ **Open your shell profile (`.zshrc` for macOS default shell)**

```sh
nano ~/.zshrc
```

_(If you're using Bash, use `nano ~/.bash_profile` instead.)_

2️⃣ **Add this line at the bottom to create a shortcut command:**

```sh
alias fileorganizer="python3 ~/python-projects/file-organizer/main.py"
```

3️⃣ **Save the file** (`Ctrl + X`, then `Y`, then `Enter`).

4️⃣ **Apply the changes**:

```sh
source ~/.zshrc
```

---

### **3️⃣ Run Your Script Using the Alias**

Now, you can run your script from **anywhere in the terminal** by simply typing:

```sh
fileorganizer
```

✔ **This works globally**, so you don’t need to navigate to the script’s directory first.

---

### **4️⃣ (Optional) Run Without `python3` (Directly as a Command)**

If you want to run it **without `python3`**, do this:

1. Add this **shebang line** at the top of `main.py`:
   ```python
   #!/usr/bin/env python3
   ```
2. Modify the alias in `.zshrc`:
   ```sh
   alias fileorganizer="~/python-projects/file-organizer/main.py"
   ```
3. Apply changes:
   ```sh
   source ~/.zshrc
   ```
4. Now just type:
   ```sh
   fileorganizer
   ```
   ✔ Runs the script **without needing to type `python3`**.

---

### **🚀 Summary**

| **Goal**                       | **Command**                                                              |
| ------------------------------ | ------------------------------------------------------------------------ |
| Give script execute permission | `chmod +x ~/python-projects/file-organizer/main.py`                      |
| Open shell profile             | `nano ~/.zshrc`                                                          |
| Add alias                      | `alias fileorganizer="python3 ~/python-projects/file-organizer/main.py"` |
| Apply changes                  | `source ~/.zshrc`                                                        |
| Run script from anywhere       | `fileorganizer`                                                          |
