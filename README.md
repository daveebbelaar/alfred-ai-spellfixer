# Alfred AI Spellfix

This repository contains two Alfred workflows for spell-checking and correcting text using AI models from Anthropic (Claude) and OpenAI. Follow the steps below to set up and configure the workflows.

![workflow](<images/CleanShot 2024-07-20 at 13.12.54@2x.png>)

## Installation

1. **Open the Workflows:**
   - Double-click the `Claude Spellfix.alfredworkflow` and `OpenAI Spellfix.alfredworkflow` files to import them into Alfred.

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
     - `src/claude_correction.py`
     - `src/openai_correction.py`


### Notes

- Ensure that you have Python installed on your system.
- The workflows require the `requests` Python library. Install it using:
```bash
pip install requests
```

Now you are ready to use the Alfred AI Spellfix workflows to quickly correct text using the power of AI models.