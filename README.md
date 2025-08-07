# HTML to PDF Converter

This is a simple command-line application to convert an HTML file to a PDF document.

## Requirements

*   Python 3
*   pip (usually comes with Python)

## Installation

Before you can use the converter, you need to install its dependencies.

1.  **Download the code:**
    *   Download the project files to a folder on your computer. You can do this by clicking the "Code" button on the repository page and selecting "Download ZIP". Unzip the downloaded file.

2.  **Windows: Install GTK3 Dependencies:**
    *   WeasyPrint requires some extra libraries on Windows. The easiest way to install them is with MSYS2.
    *   **a. Install MSYS2:** Download and install it from [msys2.org](https://www.msys2.org/).
    *   **b. Open the MSYS2 terminal:** From the Start Menu, open "MSYS2 MSYS".
    *   **c. Update the package database:** Run `pacman -Syu` and follow the prompts. You may need to close and reopen the terminal to complete the update.
    *   **d. Install GTK3:** Run the following command in the MSYS2 terminal:
        ```bash
        pacman -S mingw-w64-x86_64-gtk3
        ```
    *   **e. Add MSYS2 to your PATH:** You need to add the MSYS2 `bin` folder to your Windows environment variables so that Python can find the libraries.
        *   Press the Windows key, type "environment variables", and select "Edit the system environment variables".
        *   Click the "Environment Variables..." button.
        *   Under "System variables", find the "Path" variable, select it, and click "Edit...".
        *   Click "New" and add the path to your MSYS2 `mingw64/bin` directory. By default, this is `C:\msys64\mingw64\bin`.
        *   Click "OK" on all the windows to save the changes.
        *   **Important:** You will need to close and reopen any open command prompt or terminal windows for this change to take effect.

3.  **Open a terminal (command prompt):**
    *   **Windows:** Press `Win + R`, type `cmd`, and press Enter.
    *   **macOS/Linux:** Open your terminal application.

4.  **Navigate to the project directory:**
    *   In the terminal, use the `cd` command to move to the folder where you downloaded the project files.

5.  **Install the Python dependencies:**
    *   Once you are in the correct directory, run the following command:
        ```bash
        pip install -r requirements.txt
        ```

## Usage

To convert an HTML file to a PDF, you will run the `converter.py` script from your terminal.

1.  **Make sure you are in the project directory in your terminal.** (See step 3 in the Installation section).

2.  **Run the conversion command:**
    *   Use the `python` command followed by `converter.py`, the name of your input HTML file, and the name you want for your output PDF file.

### Example

Let's say you want to convert the included `sample.html` file into a PDF named `output.pdf`. You would run this command:

```bash
python converter.py sample.html output.pdf
```

After running the command, you will see a new file named `output.pdf` in the same folder.
