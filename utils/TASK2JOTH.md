TASK2JOTH script - decompose a natural language description of a complex task into a JOTH object

### Instructions:

1. **Install dependencies**: Make sure you have `python-dotenv` and `openai` libraries installed (`pip install 
python-dotenv openai`).
2. **Set up OpenAI API key**: Create a `.env` file in the same directory as your script with the following 
content, replacing `your_api_key` with your actual OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key
   ```
3. **Run the script**: Execute `python task2joth.py` in your terminal or command prompt and provide a natural 
language description of a complex task when prompted. The script will generate sub-tasks using the OpenAI API 
and save them as a structured JSON Object Task-Hierarchy (JOTH) format named `task_joth.json`.
4. **Adjust parameters**: You can adjust the number of generated sub-tasks (`n`), the detail level of sub-tasks 
(`max_tokens`), and randomness (`temperature`) by modifying the parameters in the `get_subtasks()` function.
