<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CodeBreaker</title>
</head>
<body>
    <h1>CodeBreaker </h1>
    <h2>Overview and Caesar Cipher Tool</h2>
    <h3>This tool will show you the concept of "Encryption."<h3>
    <h3>Encryption is the act of taking plaintext, the normal way of writing/typing messages, like writing "hello", and turning it into code, or encrypted text.<h3>
    <h3>In this tool, you will learn one of the most well known encryption methods: Subsitution; specfically, the Caesar Cipher.<h3>
    <h3>When you encrypt with a Caesar Cipher, you use a number(called a key) to shift letters. For example, if I want to encrypt the letter 'A' by a key of 3, I shift it by 3 places: A, B, C, and D. Now the secret encrypted letter is 'D'. <h3>
    <h3>Try it out! Put in a number key and a word you want to encrypt below.<h3>
    
    <form action="codebreaker_display.php" method="post">
        
	<p>
            <label for="inputKey">Type any positive integer:<sup>*</sup></label>
            <input type="text" name="key" id="inputKey">
        </p>
        <p>
            <label for="inputWord">Type a single word:<sup>*</sup></label>
            <input type="text" name="word" id="inputWord">
        </p>
        
        <input type="submit" value="Encrypt It!">
        <input type="reset" value="Reset">
    </form>
</body>
</html>