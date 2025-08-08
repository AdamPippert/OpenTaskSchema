DSPy2OTS script - convert a set of tasks defined in a .dspy file to a decomposed OTS object

## Instructions:

1. **Install dependencies**: Make sure you have `python-dotenv` and `openai` libraries installed (`pip install 
python-dotenv openai`).

2. **Set up OpenAI API key**: Create a `.env` file in the same directory as your script with the following 
content, replacing `your_api_key` with your actual OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key
   ```

3. **Prepare .dspy file**: Save your tasks in a `.dspy` format (e.g., `reasoning_questions.dspy`) with each 
task on a separate line, starting with "Task" followed by an ID and title separated by a colon (`Task <ID>: 
<Title>`).

4. **Run the script**: Execute `python dspy2ots.py` in your terminal or command prompt to generate the OTS 
file named `reasoning_questions_ots.json`.
