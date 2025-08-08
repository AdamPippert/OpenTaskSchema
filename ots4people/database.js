   const sqlite3 = require('sqlite3').verbose();

   // Open a connection to the SQLite database (create it if not exists)
   const db = new sqlite3.Database('./tasks.db', (err) => {
     if (err) {
       console.error(err.message);
     } else {
       console.log("Connected to the tasks database.");
     }
   });

   module.exports = {
     createTable: function() {
       this.db.run(`
         CREATE TABLE IF NOT EXISTS tasks (
           id INTEGER PRIMARY KEY AUTOINCREMENT, 
           title TEXT NOT NULL, 
           status TEXT NOT NULL
         );
       `);
     },

     getTasks: function(callback) {
       this.db.all('SELECT * FROM tasks', [], callback);
     },

     addTask: function(task, callback) {
       const sql = 'INSERT INTO tasks (title, status) VALUES (?, ?)';
       this.db.run(sql, [task.title, task.status], function() {
         callback();
       });
     }
   };
