<?php include_once "inc/header.php"; ?>
<?php
	if (isset($_POST["btn_submit_login"])) {
    	include_once "connection.php";
    	$connect = new db_function();
    	$connect->login_connect();
	}
	if (isset($_POST["btn_submit_register"])) {
	    include_once "connection.php";
    	$connect = new db_function();
    	$connect->register_connect();
	}
?>
<div id='content'>
	<div class="login w3_login">
        <h2 class="login-header w3_header">Log in</h2>
        <div class="w3l_grid">
            <form class="login-container" action="login.php" method="post">
                <input type="text" name="username" id="username" placeholder="Username" required>
                <input type="password" name="password" id="password" placeholder="Password" required>
                <input type="text" name="name" id="name" class="hidden" placeholder="Name">
                <input type="email" name="email" id="email" class="hidden" placeholder="Email">
                <input type="submit" name="btn_submit_login" id="submit-login" value="Login">
                <input type="submit" name="btn_submit_register" id="submit-register" class="hidden" value="Register">
            </form>
    		<!---728x90--->
            <div class="bottom-text w3_bottom_text">
                <p>No account yet? <a href="#" onclick='register()'>Sign up</a></p>
                <h4> <a href="#">Forgot your password?</a></h4>
            </div>
        </div>
    </div>
</div>
<?php include_once "inc/footer.php"; ?>