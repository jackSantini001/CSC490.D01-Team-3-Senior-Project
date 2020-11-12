<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CodeBreaker</title>
</head>
<body>
	<h1>CodeBreaker</h1>
    <h2>Encrypting Words Level Result</h2>

<?php

$word = $_POST["word"];
$score = 0;
$quest = "hello";
$ans = "pmttw";

function check_ans($word, $ans){
	if ($word == $ans){
		echo "Excellent work, that is correct!";
		echo "Good job on completing the introduction level!";
		return 5;
	}
	elseif($word != $ans){
		echo "Sorry, but that is not correct.";
		return 0;
	}
}

$point = check_ans($word, $ans);
$score += $point;
?>

<p> Let's see if you can figure out the encryption key! <p>
    <! <form action="codebreaker_level_2.php" method="post">
        
	<p>
	<p> The word you are encrypting is: "password" <p>
	<p> The encrypted version of that word is: zkccgybn <p>
            <label for="inputWord">Type the encryption key here:<sup>*</sup></label>
            <input type="text" name="word" id="inputWord">
        </p>
        
        <input type="submit" value="Submit!">
        <input type="reset" value="Reset">
    </form>	!>
</body>
</html>