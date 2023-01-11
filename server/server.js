const express = require("express");
const app = express();
const cors = require("cors");

// cors
app.use(cors());

// import routes
const systemRoutes = require("./routes/systems");
app.use(systemRoutes);

app.listen(5000, () => {
  console.log("Server started on port 5000...");
});
