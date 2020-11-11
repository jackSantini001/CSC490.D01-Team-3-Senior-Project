<?php
$server_username = "";
$server_password = "";
$server_host = "";
$database = '';

$conn = mysqli_connect($server_host,$server_username,$server_password,$database) or die("no connect");
mysqli_query($conn,"SET NAMES 'UTF8'");