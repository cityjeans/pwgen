<!DOCTYPE html>
<html lang="en-US">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width">
		<title>Password Generator!</title>
	</head>
	<body>
		<form action="execute.php" method="post">
			<input type="checkbox" name="uppercase"> Uppercase Letters<br>
			<input type="checkbox" name="numbers"> Numbers<br>
			<input type="checkbox" name="symbols"> Symbols<br>
			<input type="checkbox" name="words"> Words<br>
			<input type="number" name="length"> Length<br>
			<input type="submit" name="generate"><br>
		</form>
	</body>
</html>
