<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CodeBreaker</title>
</head>
<body>
	<h1>CodeBreaker</h1>
    <h2>Caesar Cipher Results</h2>

<?php

//$key= $_POST["key"];

$word= $_POST["word"];
$key = $_POST["key"];

$alphabet = array('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');

$char_array = str_split($word);
$enc_text = '';
$i = 0;

function encrypt($alphabet, $char_array, $i, $enc_text, $key){
foreach($char_array as $char) {
	$i = 0;
	while($char != $alphabet[$i]){
			$i++;
		}
	if ($i+$key >=26){
		$enc_text .= $alphabet[($i+$key)%26];
	}
	
	else {
		$enc_text .= $alphabet[$i+$key];
	}
	}
	return $enc_text;
}

echo "Your plaintext word was: " . $word;
echo "<br>";
echo "The number key you entered was:" . $key;
echo "<br>";
echo "Your resulting encrypted text is: " . encrypt($alphabet, $char_array, $i, $enc_text, $key);
echo "<br>";


?>    

<p> Thank you for using the Caesar Cipher Tool! </p>
<p> Now let's see if you can figure out encryption without it! <p>
    <form action="codebreaker_level_1.php" method="post">
        
	<p>
	<p> The word you are encrypting is: "hello" <p>
	<p> The key you are encrypting it with is: 8 <p>
            <label for="inputWord">Type the encrypted result:<sup>*</sup></label>
            <input type="text" name="word" id="inputWord">
        </p>
        
        <input type="submit" value="Submit!">
        <input type="reset" value="Reset">
    </form>	
</body>
</html>