const express = require("express");
const app = express();
const cors = require("cors");

// cors
app.use(cors());

// import routes
const systemRoutes = require("./routes/systems");
app.use(systemRoutes);
Text
app.listen(process.env.PORT, () => {
  console.log("Server started on port 5000...");
});
