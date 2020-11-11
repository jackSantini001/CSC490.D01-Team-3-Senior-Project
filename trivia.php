<?php
session_start();
if (!isset($_SESSION['username'])) {
	 header('Location: index.php');
}
?>
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Trivia Game</title>
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<link href="trivia/trivia.css" rel="stylesheet" type="text/css" />
</head>
<body>
<audio loop="true" id="music-backg"><source src="/upload/sound/nhac-nen.mp3" type="audio/mpeg"></audio>
<audio id="music-true"><source src="/upload/sound/tra-loi-dung.mp3" type="audio/mpeg"></audio>
<audio id="music-false"><source src="/upload/sound/sai.mp3" type="audio/mpeg"></audio>
<div id="trivia">
<div id="header">
    <img src="/upload/img/team3.png"><div>Hello, <strong class="username"><?php echo $_SESSION['username']; ?></strong></div>
    <button id="openbtn" class="openbtn" onclick="openNav()">&larr;</button>
</div>
<div id="quiz">
    <h3>Welcome to Trivia Game</h3><strong>Levels:</strong>
    <ul>
        <li>Level 1 - Easy - It is displayed a list of answers to each quiz. Click the correct answer.</li>
        <li>Level 2 - Difficult - It is displayed a text box in which you must write the answer, then click on Send button.</li>
    </ul>
    <strong>Mode</strong>
    <ul>
        <li>Consecutive - The quiestions start from the quiz with index number added into a text field, and are added in their order till the last quiz.</li>
        <li>Random - The quizzes are choosed randomly, till the last quiz, without repeat.</li>
    </ul>
    <strong>Countdown Timer</strong> 
    <ul>
        <li>If that button is checked, you have 15 seconds to answer till the next quiz is added automatically.</li>
        <li>Click the Start button to start the quizzes. The Reset button resets the Trivia.</li>
    </ul>
</div>
<div id="box-r">
    <a href="javascript:void(0)" id='closebtn' class="closebtn" onclick="closeNav()">&times;</a>
    <div id="tcateg">Trivia Category:</div>
    <div id="answered">
        <h4>Quizzes: <em id="nqansw">0</em> of <span id="ntotalq"></span></h4>
        <span id="nca">0</span> - Correct answers<br/>
        <span id="nia">0</span> - Incorrect answers
    </div>
    <div id="qdata">
        <div class="choose-level">Choose level</div>
        <div id="box-level">
           <div class="level">
                <label for="level1"><input type="radio" name="level" id="level1" checked="checked" />Level 1</label>
                <label for="level2"><input type="radio" name="level" id="level2" />Level 2</label>
            </div>
            <div class="level">
                <label for="level3"><input type="radio" name="level" id="level1" />Level 3</label>
                <label for="level4"><input type="radio" name="level" id="level2" />Level 4</label>
            </div>
            <div class="level">
                <label for="level5"><input type="radio" name="level" id="level1" />Level 5</label>
            </div> 
        </div>
        <h4>Mode</h4>
        <label for="qindex"><input type="radio" name="qmode" id="qindex" checked="checked">Consecutive</label>
        <div id="startqn">From <input type="text" size="1" name="nquiz" id="nquiz" value="1" /> to <span id="totalq"></span></div>
        <label for="qrandom"><input type="radio" name="qmode" id="qrandom" />Random</label>
        <label for="qctimer"><input type="checkbox" id="qctimer" />Countdown Timer</label>
        <label for="is-music"><input type="checkbox" id="is-music"/>On Music?</label><hr/>
        <button id="squiz">Start</button>
        <button id="treset" disabled="disabled">Reset</button>
    </div>
</div>
<div class="clear"></div>
<div id="footer-icon"><img src="/upload/img/trivia-gif1.gif"></div>
</div>
<script type="text/javascript" src="trivia/trivia.js"></script>
<script type="text/javascript" src="trivia/myapp.js"></script>
</body>
</html>