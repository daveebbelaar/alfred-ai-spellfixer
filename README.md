# Alfred AI SpellFixer

This repository contains two Alfred workflows for spell-checking and correcting text using AI models from Anthropic (Claude) and OpenAI. Follow the steps below to set up and configure the workflows.

![alt text](</images/CleanShot 2024-07-20 at 13.14.24@2x.png>)

## Requirements

- Python 3
- [Aflred](https://www.alfredapp.com)
- [Alfred Powerpack](https://www.alfredapp.com/shop/)
- Large Language Model:
  - [OpenAI API Key](https://openai.com/index/openai-api/)
    - Create new api key [here](https://platform.openai.com/api-keys)
  - [Anthropic API Key](https://console.anthropic.com)
  
### Installing Python via Command Line Tools

1. Install the [command line tools](https://mac.install.guide/commandlinetools/) by running this in the terminal:

```bash
xcode-select --install
```   

2. Than install the request library with pip via:

```bash
/usr/bin/python3 -m pip install --user requests
```

## Installation

1. **Open the Workflows:**
   - Download either the `Claude Spellfix.alfredworkflow` or `OpenAI Spellfix.alfredworkflow` from this repository.
   - Double click the file to import it into Alfred.

2. **Set the Hotkey:**
   - Open Alfred Preferences.
   - Go to the "Workflows" tab.
   - Select the `Claude Spellfix` or `OpenAI Spellfix` workflow.
   - Set a hotkey to trigger the workflow.

3. **Update the Environment Variables:**
   - Click the `{X}` button in the top right corner of Alfred Preferences.
   - Go to "Environment Variables."
   - Set `ANTHROPIC_API_KEY` for the Claude workflow or `OPENAI_API_KEY` for the OpenAI workflow, depending on which one you are configuring.
   - Optionally, you can also adjust the model in the environment variables section.

4. **Check and Customize Python Scripts:**
   - If you want to change the prompts used for spell-checking and correction, you can edit the Python scripts located in the `src` directory and update them in the workflow.
     - `src/claude_spellfixer.py`
     - `src/openai_spellfixer.py`
5. **Select the right Python version**
   - Make sure the correct python version is selected. It defaults to `usr/bin/python3` (see image below)

![Python installation](</images/CleanShot 2024-09-23 at 19.25.05@2x.png>)


## How to Use

This workflow allows you to highlight text anywhere on your Mac, trigger the workflow with a keyboard shortcut, and automatically spell-check and correct the text using AI. The corrected text will then replace the original text.

```text
The quick brown fox jumpd over the lazy dog. This is an exmple of a sentence with multiple erors. Lets see how well the AI can correkt this text.
```

Now you are ready to use the Alfred AI Spellfix workflows to quickly correct text using the power of AI models in any app.

## Does this work on Windows?

You can most likely make this work on Windows by using something like [Wox](https://github.com/Wox-launcher/Wox). Let me know via the issues or comments if you found a solution!