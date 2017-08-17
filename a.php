<?php

$myFile = "/home/pi/www/html/x.txt";
$fh = fopen($myFile, 'r');
$theData = fread($fh,10);
fclose($fh);
$myFile = "/home/pi/www/html/y.txt";
$fh = fopen($myFile, 'r');
$theData1 = fread($fh,10);
fclose($fh);

echo nl2br("Party1   $theData\n");
echo nl2br("Party2   $theData1\n");

if($theData1>$theData)
 {
  $diff=$theData1-$theData;
  echo nl2br("difference=$diff\n");
  echo nl2br("Party 2 wins with difference of votes=$diff\n");
 }
else if($theData1-$theData!=0)
{
$diff=$theData-$theData1;
echo $diff;
echo nl2br("Party 1 wins with difference of votes=$diff\n");
}
else 
echo nl2br("Tie");
?>
