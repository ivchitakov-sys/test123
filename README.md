# HTML to PDF Converter

This is a simple command-line application to convert an HTML file to a PDF document.

## Requirements

*   Python 3
*   pip (usually comes with Python)

## Installation

Before you can use the converter, you need to install its dependencies.

1.  **Download the code:**
    *   Download the project files to a folder on your computer. You can do this by clicking the "Code" button on the repository page and selecting "Download ZIP". Unzip the downloaded file.

2.  **Open a terminal (command prompt):**
    *   **Windows:** Press `Win + R`, type `cmd`, and press Enter.
    *   **macOS:** Open the "Terminal" application (you can find it in Applications > Utilities).
    *   **Linux:** Open your distribution's terminal application.

3.  **Navigate to the project directory:**
    *   In the terminal, use the `cd` command to move to the folder where you downloaded the project files. For example, if you downloaded the files to a folder named `html-to-pdf-converter` on your desktop, you would type:
        ```bash
        cd Desktop/html-to-pdf-converter
        ```

4.  **Install the dependencies:**
    *   Once you are in the correct directory, run the following command to install the necessary Python packages:
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
