// Intentional ESLint findings for the dedicated parser (errors + warnings).
/* eslint-env es2021 */

// no-eval (error)
eval("console.log(1)");

// no-unused-vars (warn)
function unusedHelper(addOne) {
	// use-isnan (error)
	if (addOne != NaN) {
		// no-console (warn)
		console.log(addOne);
		return addOne++;
	}
	// consistent-return style issues
	return;
}

// no-implied-eval (error)
setTimeout("doSomething()", 100);

// semi missing intentionally at end of expression
void unusedHelper
