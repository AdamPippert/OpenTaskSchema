// app.js
const jsonDisplay = document.getElementById('jsonDisplay');
const jsonToggle = document.getElementById('jsonToggle');
const jsonOutput = document.getElementById('jsonOutput');

let tasks = [ /* your initial tasks array */ ];

// Function to format JSON for display
function formatJSON(json) {
  return JSON.stringify(json, null, 2); // Pretty-print JSON with indentation
}

// Update JSON display based on toggle state
jsonToggle.addEventListener('change', () => {
  jsonDisplay.classList.toggle('hidden');

  if (jsonDisplay.classList.contains('hidden')) {
    jsonOutput.textContent = '';
  } else {
    const formattedJSON = formatJSON(tasks);
    jsonOutput.textContent = formattedJSON;
  }
});

document.addEventListener('DOMContentLoaded', async () => {
    try {
        // Replace with your actual API endpoint or mock data source
        const response = await fetch('/path/to/your-tasks-api');

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const tasksData = await response.json();

        // Render tasks in the #tasks-container div on index.html
        renderTasks(tasksData);
    } catch (error) {
        console.error('Error fetching or rendering tasks:', error);
    }
});


function renderTasks(tasks) {
    const tasksContainer = document.getElementById('tasks-container');

    if (!tasks || tasks.length === 0) {
        tasksContainer.innerHTML = '<p>No tasks found.</p>';
        return;
    }

    tasks.forEach((task) => {
        new TaskRenderer(task).render();
    });
}


class TaskRenderer {
    constructor(taskData) {
        this.task = taskData;
    }


    render() {
        const taskInfo = document.createElement('div');
        taskInfo.classList.add('task-info');

        for (const [key, value] of Object.entries(this.task)) {
            if (!['id', 'type', 'status'].includes(key)) {
                const property = document.createElement('p');
                property.classList.add('task-property');

                // Handle arrays as strings
                if (Array.isArray(value) || typeof value === 'object') {
                    property.textContent = JSON.stringify(value, null, 2);
                } else {
                    property.textContent = value;
                }

                taskInfo.appendChild(property);
            }
        }

        document.getElementById('tasks-container').appendChild(taskInfo);
    }
}


// Content Script for injecting app.js into the iframe if needed
if (window.self !== window.top) {
    const script = document.createElement('script');
    script.src = window.location.origin === window.top.location.origin ? './app.js' : '../../../app.js'; 
    //  Adjust path accordingly
    document.head.appendChild(script);
}
