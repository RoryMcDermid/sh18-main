const db = require("../database/databaseConfig");

exports.getAllSystems = (req, res) => {
  let sql = "SELECT * FROM SYSTEMS";
  console.log(db);
  let query = db.query(sql, (error, results) => {
    if (error) throw error;
    res.send(results);
  });
};

exports.getSystem = (req, res) => {
  let sql = `SELECT * FROM SYSTEMS WHERE SYSTEM_ID = ${req.params.id}`;
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};

exports.getAllSensorsInSystem = (req, res) => {
  let sql = `SELECT * FROM SENSORS_FOR_${req.params.systemid}`;
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};

exports.getDataFromSensors = async (req, res) => {
  let sql = "";
  console.log(req.params.sensorids);
  if (req.params.sensorids.indexOf(",") > -1) {
    const queries = req.params.sensorids.split(",").map(async (sensorId) => {
      sql = `SELECT * FROM READINGS_FOR_${sensorId} WHERE READING_DATE>='${req.query.startDate}' AND READING_DATE<'${req.query.endDate}'`;
      return new Promise((resolve, reject) => {
        db.query(sql, (error, result) => {
          if (error) reject(error);
          if (result) {
            resolve(result);
          }
        });
      });
    });
    const responses = await Promise.all(queries);
    res.send(responses);
  } else {
    sql = `SELECT * FROM READINGS_FOR_${req.params.sensorids} WHERE READING_DATE>='${req.query.startDate}' AND READING_DATE<'${req.query.endDate}'`;
    let query = await new Promise((resolve, reject) => {
      db.query(sql, (error, result) => {
        if (error) reject(error);
        if (result) {
          resolve([result]);
        }
      });
    });
    res.send(query);
  }
};
