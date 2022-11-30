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
app.get("/systems", (req, res) => {
    let sql = 'SELECT * FROM systems';
    let query = db.query(sql, (error, results) => {
        if (error) throw error;
        res.send(results);
    })
});

// Get data for single system
app.get("/systems/:id", (req, res) => {
    let sql = `SELECT * FROM systems WHERE SYSTEM_ID = ${req.params.id}`;
    let query = db.query(sql, (error, result) => {
        if (error) throw error;
        res.send(result);
    })
});

// Get sensors for single system
app.get("/systems/:systemid/sensors", (req, res) => {
    let sql = `SELECT * FROM sensors_for_${req.params.systemid}`;
    let query = db.query(sql, (error, result) => {
        if (error) throw error;
        res.send(result);
    })
});

// Get 15 min interval sensor data
app.get("/systems/:systemid/sensors/:sensorid", (req, res) => {
    let sql = `SELECT * FROM iter_1_${req.params.sensorid}`;
    let query = db.query(sql, (error, result) => {
        if (error) throw error;
        res.send(result);
    })
});

// Get 15 min interval sensor data
app.get("/systems/:systemid/sensors/:sensorid/15min", (req, res) => {
    let sql = `SELECT * FROM iter_1_${req.params.sensorid}`;
    let query = db.query(sql, (error, result) => {
        if (error) throw error;
        res.send(result);
    })
});

// Get 1 hour interval sensor data
app.get("/systems/:systemid/sensors/:sensorid/1hour", (req, res) => {
    let sql = `SELECT * FROM iter_2_${req.params.sensorid}`;
    let query = db.query(sql, (error, result) => {
        if (error) throw error;
        res.send(result);
    })
});

// Get 4 hours interval sensor data
app.get("/systems/:systemid/sensors/:sensorid/4hour", (req, res) => {
    let sql = `SELECT * FROM iter_3_${req.params.sensorid}`;
    let query = db.query(sql, (error, result) => {
        if (error) throw error;
        res.send(result);
    })
});

// Get 1 day interval sensor data
app.get("/systems/:systemid/sensors/:sensorid/1day", (req, res) => {
    let sql = `SELECT * FROM iter_4_${req.params.sensorid}`;
    let query = db.query(sql, (error, result) => {
        if (error) throw error;
        res.send(result);
    })
});



app.listen(5000, () => {console.log("Server started on port 5000...")})