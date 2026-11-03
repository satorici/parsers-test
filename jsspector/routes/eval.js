const router = require("express").Router();

router.get("/eval", (req, res) => {
	// code-injection
	res.send(eval(req.query.code));
});

router.get("/fn", (req, res) => {
	// code-injection
	res.send(Function(req.query.code)());
});

module.exports = router;
