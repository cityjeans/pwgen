<!DOCTYPE html>
<html lang="en-US">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width">
		<title>Password Generator!</title>
	</head>
	<body>
		<form>
			<input type="checkbox" name="uppercase">
			<label for "uppercase">Uppercase</label>
			<input type="checkbox" name="numbers">
			<label for "numbers">Numbers</label>
			<input type="checkbox" name="symbols">
			<label for "symbols">Symbols</label>
			<input type="checkbox" name="words">
			<label for "words">Words</label>
			<input type="submit" name="generate">
		</form>
		<?PHP 
		if (array_key_exists('QUERY_STRING', $_SERVER))
		{
			$args = "";

			if (str_contains($_SERVER['QUERY_STRING'], 'generate'))
			{
				if (str_contains($_SERVER['QUERY_STRING'], 'uppercase'))
				{
					$args .= 'u';
				}
				if (str_contains($_SERVER['QUERY_STRING'], 'numbers'))
				{
					$args .= 'd';
				}
				if (str_contains($_SERVER['QUERY_STRING'], 'symbols'))
				{
					$args .= 's';
				}
				if (str_contains($_SERVER['QUERY_STRING'], 'words'))
				{
					$args .= 'w';
				}
				if (!empty($args)) 
				{
					echo shell_exec("./pwgen.py '-$args'");
				}
				else
				{
					echo shell_exec("./pwgen.py ");
				}
			}
		}
		else
		{
			echo "Select password parameters and press submit to generate your password";
		}
		?>
	</body>
</html>
