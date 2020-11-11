<?php
session_start();
include_once "header.php";
?>
<?php
    if(isset($_SESSION['username'])){
		header('Location: trivia.php');
	}else{
		header('Location: login.php');
	}
?>
<?php 
include_once "footer.php";
?>