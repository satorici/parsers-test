const express = require("express");
const users = require("./routes/users");
const files = require("./routes/files");
const code = require("./routes/eval");

const app = express();
app.use("/api/v1", requireAuth, users);
app.use("/api/v1", requireAuth, files);
app.use("/api/v1", requireAuth, code);
module.exports = app;
