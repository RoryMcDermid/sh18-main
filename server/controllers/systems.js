const db = require("../database/databaseConfig");

exports.getAllSystems = (req, res) => {
  let sql = "SELECT * FROM systems";
  console.log(db);
  let query = db.query(sql, (error, results) => {
    if (error) throw error;
    res.send(results);
  });
};

exports.getSystem = (req, res) => {
  let sql = `SELECT * FROM systems WHERE SYSTEM_ID = ${req.params.id}`;
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};

exports.getAllSensorsInSystem = (req, res) => {
  let sql = `SELECT * FROM sensors_for_${req.params.systemid}`;
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};

exports.getFifteenMinDataFromSensors = (req, res) => {
  let sql = "";
  if (Object.keys(req.query).length === 0) {
    sql = `SELECT * FROM iter_1_${req.params.sensorid}`;
  } else {
    sql = `SELECT * FROM iter_1_${req.params.sensorid} WHERE DATE_OF_RECORD>='${req.query.startDate}' AND DATE_OF_RECORD<'${req.query.endDate}'`;
  }
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};

exports.getOneHourDataFromSensors = (req, res) => {
  if (Object.keys(req.query).length === 0) {
    sql = `SELECT * FROM iter_2_${req.params.sensorid}`;
  } else {
    sql = `SELECT * FROM iter_2_${req.params.sensorid} WHERE DATE_OF_RECORD>='${req.query.startDate}' AND DATE_OF_RECORD<'${req.query.endDate}'`;
  }
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};

exports.getFourHourDataFromSensors = (req, res) => {
  if (Object.keys(req.query).length === 0) {
    sql = `SELECT * FROM iter_3_${req.params.sensorid}`;
  } else {
    sql = `SELECT * FROM iter_3_${req.params.sensorid} WHERE DATE_OF_RECORD>='${req.query.startDate}' AND DATE_OF_RECORD<'${req.query.endDate}'`;
  }
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};

exports.getOneDayDataFromSensors = (req, res) => {
  if (Object.keys(req.query).length === 0) {
    sql = `SELECT * FROM iter_4_${req.params.sensorid}`;
  } else {
    sql = `SELECT * FROM iter_4_${req.params.sensorid} WHERE DATE_OF_RECORD>='${req.query.startDate}' AND DATE_OF_RECORD<'${req.query.endDate}'`;
  }
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};
