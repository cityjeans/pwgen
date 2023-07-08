<!DOCTYPE html>
<html lang="en-US">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width">
		<title>Password Generator!</title>
		<?PHP echo shell_exec("./pwgen.py '-wdu'");?>
	</head>
	<body>
		<form>
			<input type="checkbox" name="uppercase">
			<input type="checkbox" name="numbers">
			<input type="checkbox" name="symbols">
			<input type="checkbox" name="words">
		</form>
	</body>
</html>
