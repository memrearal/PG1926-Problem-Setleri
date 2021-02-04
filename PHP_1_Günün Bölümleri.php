<?php
$saat = date('H');
if($saat >= "00" AND $saat < "06"){
	echo 'Esenlikler dilerim';
}elseif($saat >= "06" AND $saat < "10"){
	echo 'Günaydın';
}elseif($saat >= "10" AND $saat < "17"){
	echo 'İyi günler';
}elseif($saat >= "17" AND $saat < "20"){
	echo 'İyi akşamlar';
}else{
	echo 'İyi geceler';
}
?>