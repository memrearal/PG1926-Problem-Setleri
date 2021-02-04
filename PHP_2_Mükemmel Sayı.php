<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$sayi = $_POST["sayi"];
	$toplam = 0;
	for($i = 1;$i<$sayi;$i++){
		if($sayi%$i == 0){
			$toplam = $toplam + $i;
		}
	}
	if($toplam == $sayi){
		echo "<script>alert('Girdiğiniz sayı Mükemmel Sayı!');</script>";
	}else{
		echo "<script>alert('Girdiğiniz sayı Mükemmel Sayı değildir.');</script>";
	}
}
?>
<html>
	<head>
		<meta charset="UTF-8">
        <meta name="description" content="PHP, HTML ve CSS ile yapılmış mükemmel sayı doğrulama sistemi.">
        <meta name="keywords" content="HTML, CSS, PHP, Mükemmel, Sayı">
        <meta name="author" content="memrearal">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mükemmel Sayı Doğrulama Sistemi</title>
	</head>
	<body>
		<form action="" method="post">
			<p>SAYI <input type="number" name="sayi" /></p>
			<p><input type="submit" /></p>
		</form>
	</body>
</html>
