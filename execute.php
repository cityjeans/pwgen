<html>
<body>

<?php

$args ="";
$hasargs = False;

if (isset($_POST["uppercase"])) 
{
	$hasargs = True;
	$args .= 'u';
}
if (isset($_POST["numbers"])) 
{
	$hasargs = True;
	$args .= 'd';
}
if (isset($_POST["symbols"])) 
{
	$hasargs = True;
	$args .= 's';
}
if (isset($_POST["words"])) 
{
	$hasargs = True;
	$args .= 'w';
}
if (!empty($_POST["length"])) 
{
	$hasargs = True;
	$args .= 'l ' . $_POST["length"];
}
if ($hasargs) { $args = '-' . $args; }
$output = shell_exec("./pwgen.py $args");
echo "<pre>". $output."</pre>";
?>

</body>
</html>
