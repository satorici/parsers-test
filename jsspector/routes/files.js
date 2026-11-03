const router = require("express").Router();
const fs = require("fs");
const { exec } = require("child_process");

router.get("/files", (req, res) => {
	// path-traversal
	res.send(fs.readFileSync(req.query.path));
});

router.get("/run", (req, res) => {
	// command-injection
	exec("ls " + req.query.cmd);
	res.end();
});

module.exports = router;
