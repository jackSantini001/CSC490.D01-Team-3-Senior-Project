<?php
class DBConnection{
 	private $hostname = 'localhost';
 	private $username_db = 'galaxyna_dean';
 	private $password_db = 'Db_dean123';
 	private $database = 'galaxyna_dean';

 	protected $connection;

 	public function connect(){
 		if(!isset($this->connection)){
 			$this->connection = new mysqli($this->hostname,$this->username_db,$this->password_db,$this->database);
 			mysqli_set_charset($this->connection, 'utf8');
 			if(!$this->connection){
 				echo "Connection failed!";
 				exit;
 			}
 		}
 		return $this->connection;
 	}
 }
class db_function extends DBConnection{
    public function __construct(){
        parent::connect();
    }
    public function login_connect(){    
        $username = strip_tags($_POST["username"]);
        $password = strip_tags($_POST["password"]);
        if ($username == "" || $password =="") {
        	echo "<div class='center error'>Username and password cannot be left blank !</div>";
        }else{
        	$sql = "SELECT * FROM user_trivia WHERE username = '$username' and password = '$password' ";
        	$query = $this->connection->query($sql);
        	$num_rows = mysqli_num_rows($query);
        	if ($num_rows == 0) {
        		echo "<div class='center error'>Username or password is incorrect !</div>";
        	}else{
        		$_SESSION['username'] = $username;
                header('Location: http://team3seniorprojectscsc490.com/trivia.php');
        	}
        }
    }
    public function register_connect(){
  		$username = strip_tags($_POST["username"]);
  		$password = $_POST["password"];
 		$name = $_POST["name"];
  		$email = $_POST["email"];
		if ($username == "" || $password == "" || $name == "" || $email == "") {
		    echo "<div class='center error'>Please enter your full information</div>";
  		}else{
  			$sql="select * from user_trivia where username='$username'";
  			$kt = $this->connection->query($sql);
			if(mysqli_num_rows($kt)  > 0){
				echo "Account already exists!";
			}else{
				$sql = "INSERT INTO user_trivia(
					username,
					password,
					name,
				    email
					) VALUES (
					'$username',
					'$password',
				    '$name',
					'$email'
					)";
				$this->connection->query($sql);
		   		echo "<div id='notifi'>Register complete!Navigation...</div>";
		   		$_SESSION['username']=$username;
		   		header('refresh:3 ;url=http://team3seniorprojectscsc490.com/index.php');
				}
		  }
    }
}

?>