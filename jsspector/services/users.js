const db = require("../db");

exports.find = function find(name) {
	// sql-injection
	return db.query("SELECT * FROM users WHERE name = '" + name + "'");
};
