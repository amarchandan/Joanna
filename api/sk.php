<?php
error_reporting(0);
date_default_timezone_set('America/Buenos_Aires');

function GetStr($string, $start, $end)
{
  $string = ' ' . $string;
  $ini = strpos($string, $start);
  if ($ini == 0) return '';
  $ini += strlen($start);
  $len = strpos($string, $end, $ini) - $ini;
  return trim(strip_tags(substr($string, $ini, $len)));
}
$skval = '100';
    $sk = $_GET['sk'];


############[1 Req]#############

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.stripe.com/v1/tokens');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, "card[number]=5278540001668044&card[exp_month]=10&card[exp_year]=2024&card[cvc]=252");
curl_setopt($ch, CURLOPT_USERPWD, $sk. ':' . '');
$headers = array();
$headers[] = 'Content-Type: application/x-www-form-urlencoded';
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$r1 = curl_exec($ch);
$msg = Getstr($r1,'"message": "','"');

############[2 Req]#############

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.stripe.com/v1/balance');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_USERPWD, $sk. ':' . '');
$r2 = curl_exec($ch);
$curr = Getstr($r2,'"currency": "','"');
  $balance = trim(strip_tags(getStr($r2,'{
  "object": "balance",
  "available": [
    {
      "amount":',',')));
$pending = trim(strip_tags(getStr($r2,'"livemode": true,
  "pending": [
    {
      "amount":',',')));
if(strpos($r2,'usd')) {
  $currn = '$';
  $currf = '🇺🇸';
  $currs = 'USD';
  $pending = $pending / $skval;
  $balance = $balance / $skval;
}
elseif(strpos($r2,'inr')) {
  $currn = '₹';
  $currf = '🇮🇳';
  $currs = 'INR';
  $pending = $pending / $skval;
  $balance = $balance / $skval;
}
elseif(strpos($r2,'cad')) {
  $currn = '$';
  $currf = '🇨🇦';
  $currs = 'CAD';
  $pending = $pending / $skval;
  $balance = $balance / $skval;
}
elseif(strpos($r2,'aud')) {
  $currn = 'A$';
  $currf = '🇦🇺';
  $currs = 'AUD';
  $pending = $pending / $skval;
  $balance = $balance / $skval;
}
elseif(strpos($r2,'aed')) {
  $currn = 'د.إ';
  $currf = '🇦🇪';
  $currs = 'AED';
  $pending = $pending / $skval;
  $balance = $balance / $skval;
}
elseif(strpos($r2,'sgd')) {
  $currn = 'S$';
  $currf = '🇸🇬';
  $currs = 'SGD';
  $pending = $pending / $skval;
  $balance = $balance / $skval;
}
elseif(strpos($r2,'nzd')) {
  $currn = '$';
  $currf = '🇳🇿';
  $currs = 'NZD';
  $pending = $pending / $skval;
  $balance = $balance / $skval;
}
elseif(strpos($r2,'eur')) {
  $currn = '€';
  $currf = '🇪🇺';
  $currs = 'EUR';
  $pending = $pending / $skval;
  $balance = $balance / $skval;
}
elseif(strpos($r2,'gbp')) {
  $currn = '£';
  $currf = '🇬🇧';
  $currs = 'GBP';
  $pending = $pending / $skval;
  $balance = $balance / $skval;
}
else {
  $pending = $pending / $skval;
  $balance = $balance / $skval;
  $currn = 'N/A';
  $currf = 'N/A';
  $currs = $curr;
}
#############[Responses Balance Pending Amount  ]#############

if (strpos($r1, "rate_limit")) {
  echo "┠ Status - RATE LIMIT ⚠️<br>┠ Response - Request rate limit exceeded.<br>┠ Balance - $balance $currn<br>┠ Pending Amount - $pending $currn<br>┠ Currency - $currs $currf </b>";
}
elseif (strpos($r1, "tok")) {
  echo "┠ Status - LIVE KEY ✅<br>┠ Response - Your card was declined.<br>┠ Balance - $balance $currn<br>┠ Pending Amount - $pending $currn<br>┠ Currency - $currs $currf </b>";
}
elseif (strpos($r1, "Your card was declined.")) {
  echo "┠ Status - LIVE KEY ✅<br>┠ Response - Your card was declined.<br>┠ Balance - $balance $currn<br>┠ Pending Amount - $pending $currn<br>┠ Currency - $currs $currf </b>";
}
elseif (strpos($r1, "Invalid API Key provided")) {
  echo "┠ Status - INVALID KEY ❌<br>┠ Response - Invalid API Key Provided. </b>";
}
elseif (strpos($r1, "testmode_charges_only")) {
  echo "┠ Status - DEAD KEY ❌<br>┠ Response - Your account cannot currently make live charges. <br>┠ Balance - $balance $currn<br>┠ Pending Amount - $pending $currn<br>┠ Currency - $currs $currf </b>";
}
elseif (strpos($r1, "api_key_expired")) {
  echo "┠ Status - EXPIRED KEY ❌<br>┠ Response - Expired API Key Provided. </b>";
}
else {
  echo "┠ Status - Response NOT LISTED<br>┠ Response - $msg <br>┠ Balance - $balance $currn<br>┠ Pending Amount - $pending $currn<br>┠ Currency - $currs $currf </b>";
}

curl_close($ch);
ob_flush();
?>