const express = require('express')
const app = express()
const mysql = require('mysql');

// Create connection
const db = mysql.createConnection({
    host: 'localhost',
    user: "root",
    password: "password",
    database: "moxie_energy"
});

// Connect
db.connect((error) => {
    if (error) throw error;
    console.log('Connected to MySql moxie_energy...')
});

// Get all systems data
app.get("/getsystems", (req, res) => {
    let sql = 'SELECT * FROM systems';
    let query = db.query(sql, (error, results) => {
        if (error) throw error;
        res.send(results);
    })
});

// Get single system data
app.get("/getsystems/:id", (req, res) => {
    let sql = `SELECT * FROM systems WHERE SYSTEM_ID = ${req.params.id}`;
    let query = db.query(sql, (error, result) => {
        if (error) throw error;
        res.send(result);
    })
});


app.listen(5000, () => {console.log("Server started on port 5000...")})