const router = require("express").Router();
const svc = require("../services/users");

router.get("/users/:id", (req, res) => svc.find(req.query.name));
module.exports = router;
