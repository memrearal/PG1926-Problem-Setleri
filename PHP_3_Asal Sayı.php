<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
  $sayi=$_POST['sayi'];
  if($sayi > 0){
    $asalMi=0;
    $i=2;
    do{
      if($sayi % $i == 0){
        $asalMi = 1;
      }
      $i++;
    }while($i<$sayi);
    if($asalMi != 1){
      echo "Sayı Asaldır";
    }else{
      echo "Sayı Asal Değildir";
    }
  }else{
    echo "Sayı Asal Değildir.";
  }
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta charset="UTF-8">
        <meta name="description" content="PHP, HTML ve CSS ile yapılmış girilen sayının asal sayı olup olmadığını doğrulama sistemi.">
        <meta name="keywords" content="HTML, CSS, PHP, Asal, Sayı">
        <meta name="author" content="memrearal">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Asal Sayı Doğrulama Sistemi</title>
  </head>
  <body>
    <form action="" method="post">
      <p>SAYI <input type="number" name="sayi" /></p>
      <p><input type="submit" /></p>
    </form>
  </body>
</html>