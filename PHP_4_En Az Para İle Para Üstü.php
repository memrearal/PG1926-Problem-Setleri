<?php
/*
    En az para ile para üstü problemi(knapsack problemi) çözümü
    @memrearal
    03.02.2021
    PG-1926 SOLUTIONS 
*/
if($_SERVER["REQUEST_METHOD"] == "POST"){
    $V = $_POST['paraUstu'];;
    if($V<0){
        die("Pozitif bir sayı giriniz.\r\n");
    }
    $deger = $V;
    $deger_A = 0;
    $deger_B = 0;
    $deger_C = 0;
    $deger_D = 0;
    $deger_E = 0;
    $deger_F = 0;
    for ($f = 0; $f < (int)($V/100)+1; $f++){
        for ($e = 0; $e < (int)($V/50)+1; $e++){
            if($e*50+$f*100>$V){
                continue;
            }
            for ($d = 0; $d < (int)($V/25)+1; $d++){
                if($d*25+$e*50+$f*100>$V){
                   continue;
                }
                for ($c = 0; $c < (int)($V/10)+1; $c++){
                    if($c*10+$d*25+$e*50+$f*100>$V){
                       continue;
                    }
                    for ($b = 0; $b < (int)($V/5)+1; $b++){
                        if($b*5+$c*10+$d*25+$e*50+$f*100>$V){
                           continue;
                        }
                        for ($a = 0; $a < (int)($V+1)+1; $a++){
                            if($a+$b*5+$c*10+$d*25+$e*50+$f*100>$V){
                               continue;
                            }
                            if($a*1 + $b*5 + $c*10 + $d*25 + $e*50 + $f*100 == $V){
                                if(($a+$b+$c+$d+$e+$f)<$deger){
                                    $deger = ($a+$b+$c+$d+$e+$f);
                                    $deger_A = $a;
                                    $deger_B = $b;
                                    $deger_C = $c;
                                    $deger_D = $d;
                                    $deger_E = $e;
                                    $deger_F = $f;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    echo "EN AZ VEREBİLECEGINIZ PARA ÜSTÜ: ".$deger."<br/>";
    if($deger_A > 0 ){echo $deger_A." tane 1 lira.<br/>";}
    if($deger_B > 0 ){echo $deger_B." tane 50 kuruş.<br/>";}
    if($deger_C > 0 ){echo $deger_C." tane 25 kuruş.<br/>";}
    if($deger_D > 0 ){echo $deger_D." tane 10 kuruş.<br/>";}
    if($deger_E > 0 ){echo $deger_E." tane 5 kuruş.<br/>";}
    if($deger_F > 0 ){echo $deger_F." tane 1 kuruş.<br/>";}
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta charset="UTF-8">
        <meta name="description" content="PHP, HTML ve CSS ile yapılan, en az kaç tane para ile para üstü ödeneceğini bulan sistem.">
        <meta name="keywords" content="HTML, CSS, PHP, Para, Üstü, En, Az">
        <meta name="author" content="memrearal">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>En az para ile para üstü bulma sistemi</title>
  </head>
  <body>
    <form action="" method="post">
      <p>Para üstü <input type="number" name="paraUstu" /></p>
      <p><input type="submit" /></p>
    </form>
  </body>
</html>