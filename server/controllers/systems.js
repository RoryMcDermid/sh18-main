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

exports.getFifteenMinDataFromSensors = async (req, res) => {
  let sql = "";
  if (Object.keys(req.query).length === 0) {
    const responsesArray = [];
    if (req.params.sensorids.indexOf(",") > -1) {
      const queries = req.params.sensorids.split(",").map(async (sensorId) => {
        sql = `SELECT * FROM iter_1_${sensorId}`;
        return new Promise((resolve, reject) => {
          db.query(sql, (error, result) => {
            if (error) reject(error);
            if (result.length != 0) {
              resolve(result);
            }
          });
        });
      });
      const responses = await Promise.all(queries);
      res.send(responses);
    } else {
      sql = `SELECT * FROM iter_1_${req.params.sensorids}`;
      let query = await new Promise((resolve, reject) => {
        db.query(sql, (error, result) => {
          if (error) reject(error);
          if (result.length != 0) {
            resolve([result]);
          }
        });
      });
      res.send(query);
    }
  } else {
    sql = `SELECT * FROM iter_1_${req.params.sensorid} WHERE DATE_OF_RECORD>='${req.query.startDate}' AND DATE_OF_RECORD<'${req.query.endDate}'`;
    let query = await new Promise((resolve, reject) => {
      db.query(sql, (error, result) => {
        if (error) reject(error);
        resolve(result);
      });
    });
    res.send(query);
  }
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
