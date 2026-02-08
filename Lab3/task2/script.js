    const form = document.getElementById('todo-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    const createTaskElement = (taskText) => {
      const listItem = document.createElement('li');

      const taskContent = document.createElement('div');
      taskContent.className = 'task-content';

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';

      const textSpan = document.createElement('span');
      textSpan.className = 'task-text';
      textSpan.textContent = taskText;

      const deleteButton = document.createElement('button');
      deleteButton.className = 'delete-button';
      deleteButton.textContent = 'Delete';

      checkbox.addEventListener('change', () => {
        textSpan.classList.toggle('done', checkbox.checked);
      });

      deleteButton.addEventListener('click', () => {
        taskList.removeChild(listItem);
      });

      taskContent.appendChild(checkbox);
      taskContent.appendChild(textSpan);

      listItem.appendChild(taskContent);
      listItem.appendChild(deleteButton);

      return listItem;
    };

    const handleFormSubmit = (event) => {
      event.preventDefault();

      const taskText = taskInput.value.trim();
      if (!taskText) return;

      const taskElement = createTaskElement(taskText);
      taskList.appendChild(taskElement);

      taskInput.value = '';
      taskInput.focus();
    };

    form.addEventListener('submit', handleFormSubmit);